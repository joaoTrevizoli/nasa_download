import requests
import os
import sys
import time

from url_manager import Urls


class DownloadFile(object):
    __base_dir = os.path.abspath(os.path.dirname(__file__)) + "/data/"
    __headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                               'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def __init__(self, url):
        self.url = url
        self.r = requests.get(url, stream=True, headers=self.__headers)
        self.file_name = self.url.split("/")[-1]
        self.size = int(self.r.headers.get('content-length'))
        if not os.path.exists(self.__base_dir):
            os.mkdir(self.__base_dir)

    def download(self, current_file=1, last_file=1):
        file_path = self.__base_dir + self.file_name
        if os.path.exists(file_path):
            if os.path.getsize(file_path) < self.size:
                os.remove(file_path)
            else:
                print("{} already downloaded".format(self.file_name))
                return

        if self.size is None:
            print("No downloadable content found!")
            return
        start = time.clock()
        with open(file_path, "wb") as f:
            print("Downloading file {} of {}, name: {}".format(current_file,
                                                               last_file,
                                                               self.file_name))
            dl = 0
            for chunck in self.r.iter_content(1024):
                dl += len(chunck)
                f.write(chunck)
                done = int(50 * dl / self.size)
                sys.stdout.write("\r[%s%s] %s kps" % ('=' * done, ' ' * (50 - done), (dl*0.001 // (time.clock() - start))))
            print('')
        return time.clock() - start


def download_all():
    url_list = Urls().urls()
    n_urls = len(url_list)
    count = 1
    for i in url_list:
        downloader = DownloadFile(i)
        downloader.download(current_file=count, last_file=n_urls)
        count += 1
