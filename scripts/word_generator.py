"""Word document generator for CSV documentation"""

import os
from typing import Dict, Any, Optional
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn


class WordGenerator:
    """Generate Word documents from templates"""

    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate(
        self,
        doc_type: str,
        content: str,
        variables: Dict[str, str],
        filename: Optional[str] = None,
    ) -> str:
        """Generate Word document"""

        doc = Document()

        # Process variables
        for key, value in variables.items():
            content = content.replace(f"{{{key}}}", value)

        # Set document default font
        style = doc.styles["Normal"]
        style.font.name = "Calibri"
        style.font.size = Pt(11)
        style._element.rPr.rFonts.set(qn("w:eastAsia"), "微软雅黑")

        lines = content.split("\n")
        in_table = False
        table = None

        for line in lines:
            line = line.strip()

            if not line:
                # Empty line
                doc.add_paragraph()
                continue

            # Check for table start/end
            if line.startswith("|") and "|" in line[1:]:
                if not in_table:
                    # Start new table
                    cells = [c.strip() for c in line.split("|") if c.strip()]
                    if cells:
                        table = doc.add_table(rows=1, cols=len(cells))
                        table.style = "Table Grid"

                        # Add header row
                        header_cells = table.rows[0].cells
                        for i, cell_text in enumerate(cells):
                            if i < len(header_cells):
                                self._add_cell_text(
                                    header_cells[i], cell_text, is_header=True
                                )
                        in_table = True
                else:
                    # Add data row
                    cells = [c.strip() for c in line.split("|") if c.strip()]
                    if cells and len(cells) == len(table.columns):
                        row = table.add_row()
                        for i, cell_text in enumerate(cells):
                            if i < len(row.cells):
                                self._add_cell_text(row.cells[i], cell_text)
            elif in_table and not line.startswith("|"):
                # End table
                in_table = False
                table = None
            elif line.startswith("# "):
                # Heading 1
                heading = doc.add_heading(line[2:], level=1)
                self._format_heading(heading)
            elif line.startswith("## "):
                # Heading 2
                heading = doc.add_heading(line[3:], level=2)
                self._format_heading(heading)
            elif line.startswith("### "):
                # Heading 3
                heading = doc.add_heading(line[4:], level=3)
                self._format_heading(heading)
            elif line.startswith("- [ ]") or line.startswith("- [x]"):
                # Checklist
                self._add_checklist_item(doc, line)
            elif line.startswith("- ") or line.startswith("* "):
                # Bullet list
                self._add_bullet_item(doc, line)
            elif "=" in line and "=" in line[1:]:
                # Skip separator lines
                continue
            else:
                # Regular paragraph
                self._add_paragraph(doc, line)

        # Save document
        if filename is None:
            doc_type_info = {
                "vp": "Validation_Plan",
                "urs": "URS",
                "fs": "FS",
                "ts": "TS",
                "ra": "Risk_Assessment",
                "iq": "IQ",
                "oq": "OQ",
                "pq": "PQ",
                "vsr": "Validation_Summary_Report",
            }
            filename = f"{doc_type_info.get(doc_type, doc_type)}.docx"

        output_path = self.output_dir / filename
        doc.save(str(output_path))

        return str(output_path)

    def _add_cell_text(self, cell, text: str, is_header: bool = False):
        """Add text to table cell"""
        cell.text = text
        para = cell.paragraphs[0]

        if is_header:
            para.runs[0].bold = True
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Set cell padding
        cell_element = cell._element
        tc_pr = cell_element.get_or_add_tcPr()

    def _add_paragraph(self, doc: Document, text: str):
        """Add paragraph with text"""
        para = doc.add_paragraph(text)
        para_format = para.paragraph_format

        # Check for center alignment markers
        if ":" in text and text.strip().startswith(":"):
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    def _add_bullet_item(self, doc: Document, line: str):
        """Add bullet list item"""
        text = line[2:].strip()
        para = doc.add_paragraph(text, style="List Bullet")

    def _add_checklist_item(self, doc: Document, line: str):
        """Add checklist item"""
        text = line[4:].strip()
        para = doc.add_paragraph(text)
        # Note: Word doesn't have built-in checkbox in paragraph styles
        # Could add Unicode checkbox character

    def _format_heading(self, heading):
        """Format heading"""
        for run in heading.runs:
            run.font.bold = True
