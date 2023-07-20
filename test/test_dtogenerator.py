import shutil

from unittest import TestCase
from dtogen.dtogenerator import DtoGenerator
from dtogen.interfaces import DtoGenArgs


CONTRACT_FILE_PATH = "test/dto_contract.yaml"


class TestDtoGenerator(TestCase):
    def tearDown(self) -> None:
        shutil.rmtree("out_dir")

    def test_java_generator(self):
        dto_gen_args = DtoGenArgs()
        dto_gen_args.input_file = CONTRACT_FILE_PATH
        dto_gen_args.output_dir = "out_dir"
        dto_gen_args.lang = "java"
        dto_gen_args.java_package = "com.example.hello"

        generator = DtoGenerator(dto_gen_args)
        generator.generate()

    def test_python_generator(self):
        dto_gen_args = DtoGenArgs()
        dto_gen_args.input_file = CONTRACT_FILE_PATH
        dto_gen_args.output_dir = "out_dir"
        dto_gen_args.lang = "python"

        generator = DtoGenerator(dto_gen_args)
        generator.generate()

    def test_typescript_generator(self):
        dto_gen_args = DtoGenArgs()
        dto_gen_args.input_file = CONTRACT_FILE_PATH
        dto_gen_args.output_dir = "out_dir"
        dto_gen_args.lang = "typescript"

        generator = DtoGenerator(dto_gen_args)
        generator.generate()
