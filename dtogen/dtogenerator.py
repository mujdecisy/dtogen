from dtogen.transformers.transformer_java import TransformerJava
from dtogen.filewriters.filewriter_java import FileWriterJava
import yaml
from mapperr import to_obj
from dtogen.interfaces import DtoGenYaml, DtoGenArgs, ClassInfo


class DtoGenerator:
    def __init__(
        self, args: DtoGenArgs
    ):
        self.args = args

    def generate(self):
        with open(self.args.input_file) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            data: DtoGenYaml = to_obj(data, DtoGenYaml)

        if self.args.lang == "java":
            transformer = TransformerJava(self.args)

        class_info_list = []
        for class_name, dto in data.dtos.items():
            class_info = transformer.transform(class_name, dto)
            class_info_list.append(class_info)

        if self.args.lang == "java":
            file_writer = FileWriterJava(self.args, class_info_list, data.info)
            file_writer.write()
