from __future__ import print_function
from mailmerge import MailMerge


class Generator(object):
    temp_files_folder_name = "temp_files"
    template_folder_name = "templates"

    def __init__(self, template_name: str):
        self.template = self.template_folder_name + "/" + template_name
        self.document = MailMerge(self.template)

    def get_template_fields(self):
        return self.document.get_merge_fields()

    def marge_pages_to_file(self, data, output_file_name):
        self.document.merge_pages(data)
        path = self.temp_files_folder_name + "/" + output_file_name
        self.document.write(path)



