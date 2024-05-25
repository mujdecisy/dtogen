import argparse
from dtogen.interfaces import DtoGenArgs
from .dtogenerator import DtoGenerator

def main():
    arg_parser = argparse.ArgumentParser(description="Generate DTOs from a YAML file")
    arg_parser.add_argument(
        "-i", "--input", metavar="INPUT", type=str, required=True, help="input YAML file"
    )
    arg_parser.add_argument(
        "-o", "--output", metavar="OUTPUT", type=str, required=True, help="output directory"
    )
    arg_parser.add_argument(
        "-l",
        "--lang",
        metavar="LANG",
        type=str,
        required=True,
        help="output language",
        choices=["python", "java", "typescript"],
    )
    arg_parser.add_argument(
        "--java-package", metavar="PACKAGE", type=str, help="Java package"
    )

    args = arg_parser.parse_args()

    if args.lang == "java" and not args.java_package:
        arg_parser.error("--java-package is required for java output")

    dtogen_args = DtoGenArgs()
    dtogen_args.input_file = args.input
    dtogen_args.lang = args.lang
    dtogen_args.output_dir = args.output
    dtogen_args.java_package = args.java_package

    dto_generator = DtoGenerator(dtogen_args)

    dto_generator.generate()
