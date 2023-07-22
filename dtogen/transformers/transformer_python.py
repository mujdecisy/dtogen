from .transformer import __Transformer
from ..interfaces import NestedAttribute


class TransformerPython(__Transformer):
    def get_class_header(self, class_name: str) -> str:
        return f"class {self.get_class_name(class_name)}:"

    def get_class_footer(self) -> str:
        return "\n\n"

    def get_primitive_type(self, item: NestedAttribute) -> str:
        return {
            "integer": "int",
            "float": "float",
            "string": "str",
            "boolean": "bool",
        }[item.type]

    def get_array_type(self) -> str:
        return "List[<item>]"

    def get_map_type(self) -> str:
        return "Dict[<key>, <value>]"

    def get_attribute_line(self, attribute_name: str, attribute_type: str) -> str:
        return f"    {attribute_name}: {attribute_type}"
