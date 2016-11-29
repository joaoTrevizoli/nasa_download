from url_manager import Urls
import urllib.request

url_test = "http://download.thinkbroadband.com/10MB.zip"


class DownloadFile(object):
    def __init__(self, url):
        self.url = url
        self.opener = urllib.request.build_opener()
        self.opener.addheaders = ([('User-agent', 'Mozilla/5.0')])
        try:
            self.u = self.opener.open(self.url)
            self.size = int(self.u.info()._headers[3][1])
        except Exception as e:
            print(e)

    def teste(self):
        print(self.size)

if __name__ == '__main__':
    teste = DownloadFile(url_test)
    teste.teste()