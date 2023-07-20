from unittest import TestCase
from dtogen.dtogenerator import DtoGenerator
from dtogen.interfaces import DtoGenArgs

class TestDtoGenerator(TestCase):
    def test_java_generator(self):
        dto_gen_args = DtoGenArgs()
        dto_gen_args.input_file = 'dto_contract.yaml'
        dto_gen_args.output_dir = 'test_dir'
        dto_gen_args.lang = 'typescript'
        dto_gen_args.java_package = 'com.example.hello'

        generator = DtoGenerator(dto_gen_args)
        generator.generate()