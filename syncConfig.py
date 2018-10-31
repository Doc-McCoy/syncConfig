import configparser, os.path
from ftplib import FTP

class SyncConfig:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('params.ini')
        self.user = config['conn']['user']
        self.passwd = config['conn']['passwd']
        self.paths_locais = config.options('path_local')
        self.paths_remotos = config.options('path_remoto')
        # path_v1
        # path_v2

    def connectFTP(self):
        self.ftp = FTP('svrdev001')
        self.ftp.login(user=self.user, passwd=self.passwd)

    def readFilesBinary(self): # MUDAR ESSE
        self.files = []
        for path in self.paths_locais:
            self.files.append(open(self.config[path]))

    def saveFilesOnServer(self):
        self.ftp.storbinary('STOR {}'.format(self.remote_v1), self.config_v1)
        self.ftp.storbinary('STOR {}'.format(self.remote_v2), self.config_v2)

    def syncFiles(self):
        self.connectFTP()y
        self.readFilesBinary()
        self.saveFilesOnServer()
        self.ftp.quit()
        self.config_v1.close()
        self.config_v2.close()

    def getFilesContent(self): # MUDAR ESSE
        self.files_content = []
        for path in self.paths_locais:
            if os.path.isfile(self.config[path]):
                file = open(self.config[path], 'r', encoding='ISO-8859-1')
                content = file.read()
                self.files_content.append(content)
                file.close()
            else:
                self.files_content.append("Arquivo definido em {} não encontrado".format(path))

        return self.files_content

    def saveFilesContent(self, contents): # MUDAR ESSE
        for path in self.paths_locais:
            file = open(self.config[path], 'w', encoding='ISO-8859-1')
            file.write(contents[0]) # ARRUMAR ISSO
            file.close()
