from .transformer import __Transformer
from ..interfaces import NestedAttribute


class TransformerJava(__Transformer):
    def get_class_header(self, class_name: str) -> str:
        header = f"package {self.args.java_package};\n\n"
        header += f"public class {self.get_class_name(class_name)} {'{'}"
        return header

    def get_class_footer(self) -> str:
        return "}\n"

    def get_primitive_type(self, item: NestedAttribute) -> str:
        return {
            "integer": "Integer",
            "float": "Float",
            "string": "String",
            "boolean": "Boolean",
        }[item.type]

    def get_array_type(self) -> str:
        return "List<<item>>"

    def get_map_type(self) -> str:
        return "Map<<key>, <value>>"

    def get_attribute_line(self, attribute_name: str, attribute_type: str) -> str:
        return f"    public {attribute_type} {attribute_name};"
