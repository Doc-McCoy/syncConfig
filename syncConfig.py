import configparser, os.path
from ftplib import FTP

class SyncConfig:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('params.ini')
        self.user = config['conn']['user']
        self.passwd = config['conn']['passwd']
        self.path_v1 = config['path_local']['v1_local']
        self.path_v2 = config['path_local']['v2_local']
        self.remote_v1 = config['path_remoto']['v1_remoto']
        self.remote_v2 = config['path_remoto']['v2_remoto']

    def connectFTP(self):
        self.ftp = FTP('svrdev001')
        self.ftp.login(user=self.user, passwd=self.passwd)

    def readFilesBinary(self):
        self.config_v1 = open(self.path_v1, 'rb')
        self.config_v2 = open(self.path_v2, 'rb')

    def saveFilesOnServer(self):
        self.ftp.storbinary('STOR {}'.format(self.remote_v1), self.config_v1)
        self.ftp.storbinary('STOR {}'.format(self.remote_v2), self.config_v2)

    def syncFiles(self):
        self.connectFTP()
        self.readFilesBinary()
        self.saveFilesOnServer()
        self.ftp.quit()
        self.config_v1.close()
        self.config_v2.close()

    def getFilesContent(self):
        if os.path.isfile(self.path_v1):
            v1 = open(self.path_v1, 'r', encoding='ISO-8859-1')
            conteudo_v1 = v1.read()
            v1.close()
        else:
            conteudo_v1 = 'Config v1 não encontrado.'
        if os.path.isfile(self.path_v2):
            v2 = open(self.path_v2, 'r', encoding='ISO-8859-1')
            conteudo_v2 = v2.read()
            v2.close()
        else:
            conteudo_v2 = "Config v2 não encontrado."
        return [conteudo_v1, conteudo_v2]

    def saveFilesContent(self, content1, content2):
        file1 = open(self.path_v1, 'w', encoding='ISO-8859-1')
        file2 = open(self.path_v2, 'w', encoding='ISO-8859-1')
        file1.write(content1)
        file2.write(content2)
        file1.close()
        file2.close()
