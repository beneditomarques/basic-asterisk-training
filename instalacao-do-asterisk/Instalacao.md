# Instalação do Asterisk 18 no [Debian 11](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-11.5.0-amd64-netinst.iso)

Obs: A instalação do sistema operacional em sí está fora do escopo do curso. Caberá ao aluno realizar a instalação da distribuição Linux de sua preferência. 

1 - Download do Asterisk

```bash
root@debian:~# wget https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz
```

2 - Descompactar o arquivo baixado, atualizar a lista de pacotes do Debian e instalar as dependências:

```bash
root@debian:~# tar xzfv asterisk-18-current.tar.gz 
root@debian:~# apt update
root@debian:~# bash asterisk-18.14.0/contrib/scripts/install_prereq install
```

3 - Compilar o Asterisk:

```bash
root@debian:~# cd asterisk-18.14.0/
root@debian:~/asterisk-18.14.0# ./configure 
root@debian:~/asterisk-18.14.0# make
root@debian:~/asterisk-18.14.0# make install
root@debian:~/asterisk-18.14.0# make samples
root@debian:~/asterisk-18.14.0# make config
root@debian:~/asterisk-18.14.0# make basic-pbx
```

4 - Validar a instalação

```bash
root@debian:~/asterisk-18.14.0# /etc/init.d/asterisk status
root@debian:~/asterisk-18.14.0# /etc/init.d/asterisk start
root@debian:~/asterisk-18.14.0# rasterisk 
```



