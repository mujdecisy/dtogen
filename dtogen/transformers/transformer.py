from dtogen.interfaces import Dto, Attribute, DtoGenArgs, ClassInfo

primitive_types = {"integer", "float", "string", "boolean"}


class _Transformer:
    args: dict

    def __init__(self, args: DtoGenArgs) -> None:
        self.args = args

    def get_class_header(self, class_name: str) -> str:
        raise NotImplementedError("get_class_header not implemented")

    def get_class_footer(self) -> str:
        raise NotImplementedError("get_class_footer not implemented")

    def get_class_name(self, class_name: str) -> str:
        raise NotImplementedError("get_class_name not implemented")

    def get_primitive_type(self, item: dict) -> str:
        raise NotImplementedError("get_primitive_attribute_line not implemented")

    def get_array_type(self) -> str:
        raise NotImplementedError("get_array_attribute_line not implemented")

    def get_map_type(self) -> str:
        raise NotImplementedError("get_map_attribute_line not implemented")

    def get_attribute_line(self, attribute_name: str, attribute_type: str) -> str:
        raise NotImplementedError("get_attribute_line not implemented")

    def transform_type(self, item: Attribute) -> str:
        type_ = None
        if item.type in primitive_types:
            type_ = self.get_primitive_type(item)
        elif item.type == "array":
            type_ = self.get_array_type()
            array_item_type = self.transform_type(item.items)
            type_ = type_.replace("<item>", array_item_type)
        elif item.type == "map":
            type_ = self.get_map_type()
            key_item_type = self.transform_type(item.keys)
            value_item_type = self.transform_type(item.values)
            type_ = type_.replace("<key>", key_item_type)
            type_ = type_.replace("<value>", value_item_type)
        else:
            type_ = self.get_class_name(item.type)
        return type_

    def transform(self, class_name: str, data: Dto) -> ClassInfo:
        class_text = self.get_class_header(class_name) + "\n"
        for attribute in data.attributes:
            attribute_name = attribute.name
            attribute_type = self.transform_type(attribute)
            class_text += self.get_attribute_line(attribute_name, attribute_type) + "\n"
        class_text += self.get_class_footer()

        class_info = ClassInfo()
        class_info.class_name = self.get_class_name(class_name)
        class_info.class_text = class_text

        return class_info
