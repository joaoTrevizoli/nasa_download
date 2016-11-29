import os
from nasa_download_exception import UrlFileNotFound


class Urls(object):
    def __init__(self, folder="/urls"):
        base_dir = os.path.abspath(os.path.dirname(__file__))

        if folder[0] != "/":
            folder = "/" + folder
        self.base_dir = "".join([base_dir, folder])

        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)
        self.text_files = os.listdir(self.base_dir)
        if len(self.text_files) == 0:
            raise UrlFileNotFound("None url file found in the {}, "
                                  "please add url files and retry!".format(folder))

    def url_files(self):
        return ["{}/{}".format(self.base_dir, i) for i in os.listdir(self.base_dir) if i.endswith(".txt")]

    def urls(self):
        for i in self.url_files():
            with open(i, mode="r") as url_file:
                return [line.replace("\n", '') for line in url_file.readlines()]