from .transformer import __Transformer
from ..interfaces import NestedAttribute, Relation


class TransformerJava(__Transformer):
    def get_class_header(self, class_name: str) -> str:
        header = f"package {self.args.java_package};\n\n"
        header += f"public class {self.get_class_name(class_name)} {'{'}"
        return header

    def get_relation_class_header(self, class_name: str) -> str:
        return self.get_class_header(class_name)

    def get_class_footer(self) -> str:
        return "}\n"

    def get_primitive_type(self, type_name: str) -> str:
        return {
            "integer": "Integer",
            "float": "Float",
            "string": "String",
            "boolean": "Boolean",
            "class": "Class",
            "object": "Object"
        }[type_name]

    def get_array_type(self) -> str:
        return "List<<item>>"

    def get_map_type(self) -> str:
        return "Map<<key>, <value>>"

    def get_attribute_line(self, attribute_name: str, attribute_type: str) -> str:
        return f"    public {attribute_type} {attribute_name};"

    def __create_literal(self, value: str, type: str) -> str:
        keyval = value
        if type == "string":
            keyval = f'"{value}"'
        elif type == "class":
            keyval = self.get_class_name(value)
        return keyval

    def create_private_static_final_map_attr(self, relation: Relation) -> str:
        e1c = self.get_primitive_type(relation.info.entity1.type)
        e2c = self.get_primitive_type(relation.info.entity2.type)

        text = f"    private static final Map<{e1c}, {e2c}> e1_e2 = new HashMap<>() {'{{'}\n"
        text_reversed = f"    private static final Map<{e2c}, {e1c}> e2_e1 = new HashMap<>() {'{{'}\n"

        for item in relation.attributes:
            e1l = self.__create_literal(item.entity1, relation.info.entity1.type)
            e2l = self.__create_literal(item.entity2, relation.info.entity2.type)

            text += f"      put({e1l}, {e2l});\n"
            text_reversed += f"      put({e2l}, {e1l});\n"

        text += "   }};\n"
        text_reversed += "  }};\n"

        return text + text_reversed

    def create_mapper_function(self, relation: Relation, class_name: str) -> str:
        e1n = relation.info.entity1.name
        e2n = relation.info.entity2.name
        e1c = self.get_primitive_type(relation.info.entity1.type)
        e2c = self.get_primitive_type(relation.info.entity2.type)

        class_name = self.get_class_name(class_name)

        text = f"""
    public static {e2c} {e1n}_to_{e2n}({e1c} value) {'{'}
        return {class_name}.e1_e2.get(value);
    {'}'}

    public static {e1c} {e2n}_to_{e1n}({e2c} value) {'{'}
        return {class_name}.e2_e1.get(value);
    {'}'}
"""
        return text
