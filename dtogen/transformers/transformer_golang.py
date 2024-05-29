from .transformer import __Transformer
from ..interfaces import Relation


class TransformerGolang(__Transformer):
    def get_class_header(self, class_name: str) -> str:
        return f"type {self.get_class_name(class_name)} struct {'{'}"

    def get_relation_class_header(self, class_name: str) -> str:
        return ""

    def get_class_footer(self) -> str:
        return "}\n\n"

    def get_relation_class_footer(self) -> str:
        return ""

    def get_primitive_type(self, type_name: str) -> str:
        return {
            "integer": "int",
            "float": "float64",
            "string": "string",
            "boolean": "bool",
            "class": "interface{}",
            "object": "interface{}",
        }[type_name]

    def get_array_type(self) -> str:
        return "[]<item>"

    def get_map_type(self) -> str:
        return "map[<key>][]<value>"

    def get_attribute_line(self, attribute_name: str, attribute_type: str) -> str:
        return f'\t{ self.get_class_name(attribute_name) } {attribute_type} `json:"{attribute_name}"`'

    def create_private_static_final_map_attr(self, relation: Relation, class_name: str) -> str:
        e1t = self.get_primitive_type(relation.info.entity1.type)
        e2t = self.get_primitive_type(relation.info.entity2.type)

        text = f"var {class_name}_e1e2 = map[{e1t}]{e2t} {'{'}"
        text_reversed = f"var {class_name}_e2e1 = map[{e2t}]{e1t} {'{'}"
        for item in relation.attributes:
            e1l = self.create_literal(item.entity1, relation.info.entity1.type)
            e2l = self.create_literal(item.entity2, relation.info.entity2.type)

            if relation.info.entity1.type == "class":
                e1l = f"{e1l}{'{}'}"
            if relation.info.entity2.type == "class":
                e2l = f"{e2l}{'{}'}"

            text += f"{e1l}: {e2l}, "
            text_reversed += f"{e2l}: {e1l}, "
        text += "}\n"
        text_reversed += "}\n"

        return text + text_reversed

    def create_mapper_function(self, relation: Relation, class_name: str) -> str:
        e1n = self.get_class_name(relation.info.entity1.name)
        e2n = self.get_class_name(relation.info.entity2.name)
        e1c = self.get_primitive_type(relation.info.entity1.type)
        e2c = self.get_primitive_type(relation.info.entity2.type)

        class_name = self.get_class_name(class_name)

        text = f"""
type { class_name } struct{'{}'}

func (x {class_name}) {e1n}To{e2n}(value {e1c}) {e2c} {'{'}
    return {class_name}_e1e2[value]
{'}'}

func (x {class_name}) {e2n}To{e1n}(value {e2c}) {e1c} {'{'}
    return {class_name}_e2e1[value]
{'}'}
"""
        return text
