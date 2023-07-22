from .interfaces import DtoGenYaml, DtoGenArgs
from .transformers import (
    Transformer,
    TransformerJava,
    TransformerPython,
    TransformerTypescript,
)

from .filewriters import (
    FileWriter,
    FileWriterJava,
    FileWriterPython,
    FileWriterTypescript,
)

import yaml
from mapperr import to_obj
from typing import Dict


class __LangClass:
    transformer: Transformer.__class__
    filewriter: FileWriter.__class__

    def __init__(
        self, transformer: Transformer.__class__, filewriter: FileWriter.__class__
    ):
        self.transformer = transformer
        self.filewriter = filewriter


_LANGUAGE_CLASSES: Dict[str, __LangClass] = {
    "java": __LangClass(TransformerJava, FileWriterJava),
    "python": __LangClass(TransformerPython, FileWriterPython),
    "typescript": __LangClass(TransformerTypescript, FileWriterTypescript),
}


class DtoGenerator:
    def __init__(self, args: DtoGenArgs):
        self.args = args

    def generate(self):
        with open(self.args.input_file) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            data: DtoGenYaml = to_obj(data, DtoGenYaml)

        transformer: Transformer = _LANGUAGE_CLASSES[self.args.lang].transformer(
            self.args
        )

        class_info_list = []
        for class_name, dto in data.dtos.items():
            class_info = transformer.transform(class_name, dto)
            class_info_list.append(class_info)

        file_writer: FileWriter = _LANGUAGE_CLASSES[self.args.lang].filewriter(
            self.args, class_info_list, data.info
        )
        file_writer.write()
