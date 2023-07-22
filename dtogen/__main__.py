import argparse
from .dtogenerator import DtoGenerator


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


if __name__ == "__main__":
    dto_generator = DtoGenerator(
        "../dto_contract.yaml", "../out", "java", "com.example.hello"
    )
