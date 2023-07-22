from ..interfaces import Dto, Attribute, DtoGenArgs, ClassInfo

PRIMITIVE_TYPES = {"integer", "float", "string", "boolean"}


class Transformer:
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
        raise NotImplementedError("transform_type not implemented")

    def transform(self, class_name: str, data: Dto) -> ClassInfo:
        raise NotImplementedError("transform not implemented")


class __Transformer(Transformer):
    def __init__(self, args: DtoGenArgs) -> None:
        self.args = args

    def get_class_header(self, class_name: str) -> str:
        raise NotImplementedError("get_class_header not implemented")

    def get_class_footer(self) -> str:
        raise NotImplementedError("get_class_footer not implemented")

    def get_primitive_type(self, item: dict) -> str:
        raise NotImplementedError("get_primitive_attribute_line not implemented")

    def get_array_type(self) -> str:
        raise NotImplementedError("get_array_attribute_line not implemented")

    def get_map_type(self) -> str:
        raise NotImplementedError("get_map_attribute_line not implemented")

    def get_attribute_line(self, attribute_name: str, attribute_type: str) -> str:
        raise NotImplementedError("get_attribute_line not implemented")

    def get_class_name(self, class_name: str) -> str:
        if len(class_name) < 3:
            raise ValueError("Class name must be at least 5 characters long")

        i = 1
        while i < len(class_name):
            if (class_name[i].isupper() and not class_name[i - 1].isupper()) or (
                class_name[i].islower() and not class_name[i - 1].islower()
            ):
                if not class_name[i - 1].isalpha():
                    class_name = class_name[: i - 1] + "-" + class_name[i:]
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

    def transform_type(self, item: Attribute) -> str:
        type_ = None
        if item.type in PRIMITIVE_TYPES:
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
