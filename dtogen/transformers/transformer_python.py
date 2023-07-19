from dtogen.transformers.transformer import __Transformer
from dtogen.interfaces import NestedAttribute


class TransformerPython(__Transformer):
    def get_class_header(self, class_name: str) -> str:
        return f"class {self.get_class_name(class_name)}:"

    def get_class_footer(self) -> str:
        return "\n\n"

    def get_class_name(self, class_name: str) -> str:
        if len(class_name) < 3:
            raise ValueError("Class name must be at least 5 characters long")

        i = 1
        while i < len(class_name):
            if (class_name[i].isupper() and not class_name[i - 1].isupper()) or (
                class_name[i].islower() and not class_name[i - 1].islower()
            ):
                if not class_name[i - 1].isalpha():
                    class_name = class_name[:i-1] + "-" + class_name[i:]
                else:
                    class_name = class_name[:i] + "-" + class_name[i:]
                i += 2
            i += 1

        # split class name with non-alphanumeric characters
        class_name_alphanum = class_name.replace("[^\w^\d]+", "-")
        return "".join(
            [
                word[0].upper() + word[1:].lower()
                for word in class_name_alphanum.split("-")
            ]
        )

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
