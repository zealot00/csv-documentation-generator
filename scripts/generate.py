#!/usr/bin/env python3
"""CSV Documentation Generator - Main Entry Point

Generate Computerized System Validation (CSV) documentation
for pharmaceutical and medical device industries.

Usage:
    python3 generate.py vp --project "Project" --system "System v1.0" --category 4 --output ./output/
    python3 generate.py urs --project "Project" --system "System" --category 4 --bilingual true
    python3 generate.py all --project "Project" --system "System" --category 4 --output ./validation/
"""

import argparse
import sys
import os
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from config import Config, get_gamp_category_description
from template_loader import TemplateLoader
from word_generator import WordGenerator
from excel_generator import ExcelGenerator


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="CSV Documentation Generator - Generate validation documents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 generate.py vp --project "临床系统" --system "EDC v1.0" --category 4 --output ./output/
  python3 generate.py urs --system "CTMS" --bilingual true --output ./doc/
  python3 generate.py all --project "XX系统" --system "MES" --category 4 --output ./validation/
        """,
    )

    parser.add_argument(
        "doc_type",
        choices=[
            "vp",
            "urs",
            "fs",
            "ts",
            "ra",
            "iq",
            "oq",
            "pq",
            "rtm",
            "vsr",
            "checklist",
            "test-case",
            "all",
        ],
        help="Document type to generate",
    )

    parser.add_argument(
        "--project", "-p", default="[Project Name]", help="Project name"
    )

    parser.add_argument(
        "--system", "-s", default="[System Name v1.0]", help="System name and version"
    )

    parser.add_argument(
        "--category",
        "-c",
        type=int,
        default=4,
        choices=[1, 2, 3, 4, 5],
        help="GAMP category (1-5)",
    )

    parser.add_argument(
        "--bilingual",
        "-b",
        default=True,
        type=bool,
        help="Generate bilingual templates (default: True)",
    )

    parser.add_argument("--output", "-o", default="./output", help="Output directory")

    parser.add_argument(
        "--format",
        "-f",
        choices=["docx", "xlsx", "both"],
        default="both",
        help="Output format",
    )

    parser.add_argument("--doc-id", default="[DOC-XXX]", help="Document ID")

    parser.add_argument("--version", default="1.0", help="Document version")

    parser.add_argument("--author", default="[Author]", help="Document author")

    parser.add_argument("--reviewer", default="[Reviewer]", help="Document reviewer")

    parser.add_argument("--approver", default="[Approver]", help="Document approver")

    parser.add_argument(
        "--critical-functions",
        default="数据录入,审计追踪,权限控制",
        help="Critical functions (comma-separated)",
    )

    return parser.parse_args()


def generate_document(doc_type: str, config: Config):
    """Generate a single document"""

    # Get template loader
    template_loader = TemplateLoader()

    # Get document info
    doc_info = Config.get_document_info(doc_type)
    variables = config.get_variables()
    variables["DOC_TYPE_NAME"] = doc_info["name"]
    variables["DOC_TYPE_NAME_CN"] = doc_info["name_cn"]
    variables["DOC_TYPE"] = doc_type.upper()

    # Determine format
    format_type = doc_info.get("format", "docx")
    if config.format == "both":
        generate_formats = [format_type] if format_type != "both" else ["docx", "xlsx"]
    else:
        generate_formats = [config.format]

    output_files = []

    for fmt in generate_formats:
        if fmt == "xlsx":
            # Excel generation
            excel_gen = ExcelGenerator(config.output)
            output_file = excel_gen.generate(doc_type=doc_type, variables=variables)
            output_files.append(output_file)
            print(f"Generated: {output_file}")
        else:
            # Word generation
            try:
                template_content = template_loader.load_template(doc_type)
            except FileNotFoundError:
                print(f"Warning: Template not found for {doc_type}, using default")
                template_content = f"# {doc_info['name']}\n\nDocument: {config.project}\nSystem: {config.system}"

            word_gen = WordGenerator(config.output)
            output_file = word_gen.generate(
                doc_type=doc_type, content=template_content, variables=variables
            )
            output_files.append(output_file)
            print(f"Generated: {output_file}")

    return output_files


def generate_all(config: Config):
    """Generate all documents"""

    doc_types = [
        "vp",
        "urs",
        "fs",
        "ra",
        "iq",
        "oq",
        "pq",
        "vsr",
        "rtm",
        "checklist",
        "test-case",
    ]

    print(f"\nGenerating validation package for: {config.project}")
    print(f"System: {config.system}")
    print(f"Category: {config.category}")
    print(f"Output: {config.output}\n")

    all_files = []

    for doc_type in doc_types:
        try:
            files = generate_document(doc_type, config)
            all_files.extend(files)
        except Exception as e:
            print(f"Error generating {doc_type}: {e}")

    print(f"\n{'=' * 50}")
    print(f"Generated {len(all_files)} documents:")
    for f in all_files:
        print(f"  - {f}")

    return all_files


def main():
    """Main entry point"""
    args = parse_args()

    # Create output directory
    Path(args.output).mkdir(parents=True, exist_ok=True)

    # Create config
    config = Config(
        project=args.project,
        system=args.system,
        category=args.category,
        bilingual=args.bilingual,
        output=args.output,
        format=args.format,
        doc_id=args.doc_id,
        version=args.version,
        author=args.author,
        reviewer=args.reviewer,
        approver=args.approver,
        critical_functions=args.critical_functions,
    )

    print(f"CSV Documentation Generator")
    print(f"{'=' * 50}")

    # Generate documents
    if args.doc_type == "all":
        generate_all(config)
    else:
        generate_document(args.doc_type, config)

    print(f"\nDone! Files saved to: {args.output}")


if __name__ == "__main__":
    main()
