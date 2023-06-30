from dtogen.transformers.transformer import Transformer

class TransformerJava(Transformer):
    def __init__(self) -> None:
        super().__init__()
        self.types = {'integer', 'float', 'string', 'boolean', 'array', 'map'}

    def get_class_header(self, class_name: str) -> str:
        return f'public class {class_name} {{'

    def get_class_name(self, class_name: str) -> str:
        # split class name with non-alphanumeric characters
        class_name_alphanum = class_name.replace('[^\w^\d]+', '-')
        return ''.join([word[0].upper() + word[1:] for word in class_name_alphanum.split('-')])

    def get_primitive_type(self, item) -> str:
        return {
            'integer': 'Integer',
            'float': 'Float',
            'string': 'String',
            'boolean': 'Boolean'
        }[item['type']]

    def get_array_type(self) -> str:
        return 'List<<item>>'

    def get_map_type(self) -> str:
        return 'Map<<key>, <value>>'

    def get_attribute_line(self, attribute_name: str, attribute_type: str) -> str:
        return f'public {attribute_type} {attribute_name};'