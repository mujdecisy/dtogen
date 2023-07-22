from typing import List
from ..interfaces import FileInfo
from .filewriter import __FileWriter


class FileWriterPython(__FileWriter):
    def get_extension(self) -> str:
        return "py"

    def generate_comment(self, comment: str) -> str:
        return f"# {comment}"

    def generate_files(self) -> List[FileInfo]:
        file_text = "from typing import List, Dict\n\n\n"
        for a_class in self.classes:
            file_text += a_class.class_text

        a_file = FileInfo()
        a_file.file_name = "dtos"
        a_file.file_text = file_text

        return [a_file]
