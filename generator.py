from __future__ import print_function
from mailmerge import MailMerge


class Generator(object):
    def __init__(self, template_url: str):
        self.template = template_url
        self.document = MailMerge(self.template)

    def get_template_fields(self):
        return self.document.get_merge_fields()

    def marge_pages_to_file(self, data, output_file):
        self.document.merge_pages(data)
        self.document.write(output_file)



