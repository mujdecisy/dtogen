from .transformer import __Transformer
from ..interfaces import NestedAttribute, Relation


class TransformerTypescript(__Transformer):
    def get_class_header(self, class_name: str) -> str:
        return f"export class {self.get_class_name(class_name)} {'{'}"

    def get_relation_class_header(self, class_name: str) -> str:
        return f"export class {self.get_class_name(class_name)} {'{'}"

    def get_class_footer(self) -> str:
        return "}\n\n"

    def get_relation_class_footer(self) -> str:
        return self.get_class_footer()

    def get_primitive_type(self, type_name: str) -> str:
        return {
            "integer": "number",
            "float": "number",
            "string": "string",
            "boolean": "boolean",
            "class": "any",
            "object": "any",
        }[type_name]

    def get_array_type(self) -> str:
        return "<item>[]"

    def get_map_type(self) -> str:
        return "Record<<key>, <value>>"

    def get_attribute_line(self, attribute_name: str, attribute_type: str) -> str:
        return f"    {attribute_name}: {attribute_type}"

    def create_private_static_final_map_attr(self, relation: Relation) -> str:
        e1c = self.get_primitive_type(relation.info.entity1.type)
        e2c = self.get_primitive_type(relation.info.entity2.type)

        is_e1_class = relation.info.entity1.type == "class"
        is_e2_class = relation.info.entity2.type == "class"

        e1ckey = "string" if is_e1_class else e1c
        e2ckey = "string" if is_e2_class else e2c

        text = f"    private static readonly e1_e2: {'{'}[key: {e1ckey}]: {e2c}{'}'} = {'{'}"
        text_reversed = f"    private static readonly e2_e1: {'{'}[key: {e2ckey}]: {e1c}{'}'} = {'{'}"

        for item in relation.attributes:
            e1l = self.create_literal(item.entity1, relation.info.entity1.type)
            e2l = self.create_literal(item.entity2, relation.info.entity2.type)

            text += f"{ self.create_literal(e1l, 'string')  if is_e1_class else e1l}: {e2l}, "
            text_reversed += f"{ self.create_literal(e2l, 'string')  if is_e2_class else e2l}: {e1l}, "

        text += "   };\n"
        text_reversed += "  };\n"

        return text + text_reversed

    def create_mapper_function(self, relation: Relation, class_name: str) -> str:
        e1n = relation.info.entity1.name
        e2n = relation.info.entity2.name
        e1c = self.get_primitive_type(relation.info.entity1.type)
        e2c = self.get_primitive_type(relation.info.entity2.type)

        is_e1_class = relation.info.entity1.type == "class"
        is_e2_class = relation.info.entity2.type == "class"

        class_name = self.get_class_name(class_name)

        text = f"""
    public static {e1n}_to_{e2n}(value: {e1c}) : {e2c} {'{'}
        return {class_name}.e1_e2[{'value.name as string' if is_e1_class else 'value'}];
    {'}'}

    public static {e2n}_to_{e1n}(value: {e2c}): {e1c} {'{'}
        return {class_name}.e2_e1[{'value.name as string' if is_e2_class else 'value'}];
    {'}'}
"""
        return text
