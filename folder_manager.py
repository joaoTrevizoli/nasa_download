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
        self.text_files = ["{}/{}".format(self.base_dir, ) for i in os.listdir(self.base_dir) if i.endswith(".txt")]
        if len(self.text_files) == 0:
            raise UrlFileNotFound("None url file found in the {}, "
                                  "please add url files and retry!".format(folder))

if __name__ == '__main__':
    paths = Urls("urls")
    print(paths.text_files)