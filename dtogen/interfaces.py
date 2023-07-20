from typing import Dict, List


class Info:
    name: str
    version: str


class NestedAttribute:
    type: str
    items: "NestedAttribute"
    keys: "NestedAttribute"
    values: "NestedAttribute"


class Attribute(NestedAttribute):
    name: str


class Dto:
    attributes: List[Attribute]


class DtoGenYaml:
    info: Info
    dtos: Dict[str, Dto]


class ClassInfo:
    class_name: str
    class_text: str


class FileInfo:
    file_name: str
    file_text: str


class DtoGenArgs:
    input_file: str
    output_dir: str
    lang: str
    java_package: str
