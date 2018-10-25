import configparser
from ftplib import FTP

config = configparser.ConfigParser()
config.read('params.ini')
user = config['conn']['user']
passwd = config['conn']['passwd']

path_v1 = config['path_local']['v1_local']
path_v2 = config['path_local']['v2_local']

ftp_path_v1 = config['path_remoto']['v1_remoto']
ftp_path_v2 = config['path_remoto']['v2_remoto']

ftp = FTP('svrdev001')
ftp.login(user=user, passwd=passwd)

config_v1 = open(path_v1, 'rb')
config_v2 = open(path_v2, 'rb')

ftp.storbinary('STOR {}'.format(ftp_path_v1), config_v1)
ftp.storbinary('STOR {}'.format(ftp_path_v2), config_v2)

config_v1.close()
config_v2.close()
ftp.quit()
