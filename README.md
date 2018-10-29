# syncConfig
Pequena app que permite editar e enviar 2 arquivos 'config.ini' simultaneamente para um servidor via ftp.

Para funcionar, necessita que um arquivo `params.ini` seja criado no diretório raíz, com os seguintes parâmetros:

```
[conn]
user=user
passwd=passwd

[path_local]
v1_local=/local/path/to/config.ini
v2_local=/local/path/to/config.ini

[path_remoto]
v1_remoto=/remote/path/to/config.ini
v2_remoto=/remote/path/to/config.ini
```
