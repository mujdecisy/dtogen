from dtogen.transformers.transformer_java import TransformerJava
import yaml


class DtoGenerator:
    def __init__(self, input_file: str, output_dir: str, lang: str, java_package: str = None):
        self.input_file = input_file
        self.output_dir = output_dir
        self.lang = lang
        self.java_package = java_package

    def generate(self):
        with open(self.input_file) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            print(data)
        if self.lang == "java":
            transformer = TransformerJava()
            for key, value in data['dtos'].items():
                resp = transformer.transform(key, value)
                print(resp)
