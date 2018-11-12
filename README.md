# syncConfig
Pequena app que permite editar e enviar 2 arquivos de texto simultaneamente, e ainda upá-los para um servidor via ftp se for necessário.

Para funcionar, necessita que um arquivo `params.ini` seja criado no diretório raíz, com os seguintes parâmetros:

```
[conn]
user=user
passwd=passwd
host=host

[local]
file1=/local/path/to/file1.txt
file2=/local/path/to/file2.txt

[remoto]
file1=/remote/path/to/file1.txt
file2=/remote/path/to/file2.txt
```
