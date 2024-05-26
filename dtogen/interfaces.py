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


class RelAttribute:
    entity1: str
    entity2: str

class RelationInfoAttr:
    name: str
    type: str

class RelationInfo:
    entity1: RelationInfoAttr
    entity2: RelationInfoAttr

class Relation:
    info: RelationInfo
    attributes: List[RelAttribute]


class DtoGenYaml:
    info: Info
    dtos: Dict[str, Dto]
    relations: Dict[str, Relation]


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
