from unittest import TestCase
from dtogen.dtogenerator import DtoGenerator

class TestDtoGenerator(TestCase):
    
    def test_java_generator(self):
        generator = DtoGenerator('dto_contract.yaml', 'testpackage', 'java')
        generator.generate()