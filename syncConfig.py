import configparser
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

    def openFiles(self):
        self.config_v1 = open(self.path_v1, 'rb')
        self.config_v2 = open(self.path_v2, 'rb')

    def saveFilesOnServer(self):
        self.ftp.storbinary('STOR {}'.format(ftp_path_v1), self.config_v1)
        self.ftp.storbinary('STOR {}'.format(ftp_path_v2), self.config_v2)

    def __destroy__(self):
        self.config_v1.close()
        self.config_v2.close()
        self.ftp.quit()
