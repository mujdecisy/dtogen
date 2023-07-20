from unittest import TestCase
from dtogen.transformers.transformer_java import TransformerJava


class TestTransform(TestCase):
    def test_class_name_converter_when_class_name_is_all_lowercase(self):
        transformer = TransformerJava(None)
        class_name = "test"
        expected = "Test"
        actual = transformer.get_class_name(class_name)
        self.assertEqual(expected, actual)

    def test_class_name_converter_when_class_name_is_all_uppercase(self):
        transformer = TransformerJava(None)
        class_name = "TEST"
        expected = "Test"
        actual = transformer.get_class_name(class_name)
        self.assertEqual(expected, actual)

    def test_class_name_converter_when_class_name_is_mixed_case(self):
        transformer = TransformerJava(None)
        class_name = "testClass"
        expected = "TestClass"
        actual = transformer.get_class_name(class_name)
        self.assertEqual(expected, actual)

    def test_class_name_converter_when_class_name_is_mixed_case_with_non_alphanumeric_characters(
        self,
    ):
        transformer = TransformerJava(None)
        class_name = "test-class-123"
        expected = "TestClass123"
        actual = transformer.get_class_name(class_name)
        self.assertEqual(expected, actual)
