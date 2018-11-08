import configparser, os.path
from ftplib import FTP

class SyncConfig:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('params.ini')
        self.user = self.config['conn']['user']
        self.passwd = self.config['conn']['passwd']
        self.host = self.config['conn']['host']
        self.paths_locais = self.config.options('local')
        self.paths_remotos = self.config.options('remoto')

    def connectFTP(self):
        self.ftp = FTP(self.host)
        self.ftp.login(user=self.user, passwd=self.passwd)

    def readFilesBinary(self):
        self.files = []
        for path in self.paths_locais:
            self.files.append(open(self.config['local'][path]))

    def saveBinaryFilesOnServer(self):
        index = 0
        for path in self.paths_remotos:
            self.ftp.storbinary("STOR {}".format(self.config['remoto'][path]), self.files[index])
            index += 1

    def closeBinaryFiles(self):
        for file in self.files:
            file.close()

    def syncFiles(self):
        self.connectFTP()
        self.readFilesBinary()
        self.saveBinaryFilesOnServer()
        self.closeBinaryFiles()
        self.ftp.quit()

    def getFilesContent(self):
        self.files_content = []
        for path in self.paths_locais:
            if os.path.isfile(self.config['local'][path]):
                file = open(self.config['local'][path], 'r', encoding='ISO-8859-1')
                content = file.read()
                self.files_content.append(content)
                file.close()
            else:
                self.files_content.append("Arquivo definido em {} não encontrado".format(path))

        return self.files_content

    def saveFilesContent(self, contents):
        index = 0
        for path in self.paths_locais:
            file = open(self.config['local'][path], 'w', encoding='ISO-8859-1')
            file.write(contents[index])
            file.close()
            index += 1
