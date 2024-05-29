from .transformer import __Transformer
from ..interfaces import Relation


class TransformerPython(__Transformer):
    def get_class_header(self, class_name: str) -> str:
        return f"class {self.get_class_name(class_name)}:"

    def get_relation_class_header(self, class_name: str) -> str:
        return self.get_class_header(class_name)

    def get_class_footer(self) -> str:
        return "\n\n"

    def get_relation_class_footer(self) -> str:
        return self.get_class_footer()

    def get_primitive_type(self, type_name: str) -> str:
        return {
            "integer": "int",
            "float": "float",
            "string": "str",
            "boolean": "bool",
            "class": "type",
            "object": "object",
        }[type_name]

    def get_array_type(self) -> str:
        return "List[<item>]"

    def get_map_type(self) -> str:
        return "Dict[<key>, <value>]"

    def get_attribute_line(self, attribute_name: str, attribute_type: str) -> str:
        return f"    {attribute_name}: {attribute_type}"

    def create_private_static_final_map_attr(self, relation: Relation, class_name: str) -> str:
        text = f"    __e1_e2 = {'{'}"
        text_reversed = f"    __e2_e1 = {'{'}"
        for item in relation.attributes:
            e1l = self.create_literal(item.entity1, relation.info.entity1.type)
            e2l = self.create_literal(item.entity2, relation.info.entity2.type)
            text += f"{e1l}: {e2l}, "
            text_reversed += f"{e2l}: {e1l}, "
        text += "}\n"
        text_reversed += "}\n"

        return text + text_reversed

    def create_mapper_function(self, relation: Relation, class_name: str) -> str:
        e1n = relation.info.entity1.name
        e2n = relation.info.entity2.name
        e1c = self.get_primitive_type(relation.info.entity1.type)
        e2c = self.get_primitive_type(relation.info.entity2.type)

        class_name = self.get_class_name(class_name)

        text = f"""
    @staticmethod
    def {e1n}_to_{e2n}(value: {e1c}) -> {e2c}:
        return {class_name}.__e1_e2[value]

    @staticmethod
    def {e2n}_to_{e1n}(value: {e2c}) -> {e1c}:
        return {class_name}.__e2_e1[value]
"""
        return text
