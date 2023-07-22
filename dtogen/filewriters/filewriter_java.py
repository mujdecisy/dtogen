from typing import List
from ..interfaces import FileInfo
from .filewriter import __FileWriter


class FileWriterJava(__FileWriter):
    def get_extension(self) -> str:
        return "java"

    def generate_comment(self, comment: str) -> str:
        return f"// {comment}"

    def generate_files(self) -> List[FileInfo]:
        files = []
        for a_class in self.classes:
            a_file = FileInfo()
            a_file.file_name = a_class.class_name
            a_file.file_text = a_class.class_text
            files.append(a_file)
        return files
