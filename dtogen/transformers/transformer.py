
primitive_types = {'integer', 'float', 'string', 'boolean'}

class Transformer:
    def __init__(self) -> None:
        self.types: set = {'integer', 'float', 'string', 'boolean', 'array', 'map'}

    def get_class_header(self, class_name: str) -> str:
        raise NotImplementedError("get_class_header not implemented")

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

    def transform_type(self, item: dict) -> str:
        if item['type'] in primitive_types:
            return self.get_primitive_type(item)
        elif item['type'] == 'array':
            type = self.get_array_type()
            array_item_type = self.transform_type(item['items'])
            type = type.replace('<item>', array_item_type)
            return type
        elif item['type'] == 'map':
            type = self.get_map_type()
            key_item_type = self.transform_type(item['keys'])
            value_item_type = self.transform_type(item['values'])
            type = type.replace('<key>', key_item_type)
            type = type.replace('<value>', value_item_type)
            return type
        else:
            return self.get_class_name(item['type'])

    def transform(self, class_name: str, data: dict) -> str:
        class_text = self.get_class_header(class_name) + '\n'
        for attribute in data['attributes']:
            attribute_name = attribute['name']
            attribute_type = self.transform_type(attribute)
            class_text += self.get_attribute_line(attribute_name, attribute_type) + '\n'
        return class_text




