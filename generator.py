from __future__ import print_function
from mailmerge import MailMerge
from os import path
from datetime import datetime


class Generator(object):
    temp_files_folder_name = "temp_files"
    template_folder_name = "templates"

    def __init__(self, template_name: str):
        self.template = self.template_folder_name + "/" + template_name
        self.document = MailMerge(self.template)

    def get_template_fields(self):
        return self.document.get_merge_fields()

    def merge_pages_to_file(self, data, filename):
        self.document.merge_pages(data)
        file_path = self.temp_files_folder_name + "/" + filename
        self.document.write(file_path)
        return file_path

    def get_docx_file(self, data):
        filename = str(datetime.now()) + '.docx'
        file_path = self.merge_pages_to_file(data, filename)
        return file_path