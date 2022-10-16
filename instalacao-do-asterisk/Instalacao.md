# Instalação do Asterisk 18 no [Debian 11](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-11.5.0-amd64-netinst.iso)

Obs: A instalação do sistema operacional em sí está fora do escopo do curso. Caberá ao aluno realizar a instalação da distribuição Linux de sua preferência. 

**1 - Download do Asterisk**

```bash
wget https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz
```

**2 - Descompactar o arquivo baixado, atualizar a lista de pacotes do Debian e instalar as dependências**

```bash
tar xzfv asterisk-18-current.tar.gz 
apt update
bash asterisk-18.14.0/contrib/scripts/install_prereq install
```

**3 - Compilar o Asterisk**

```bash
cd asterisk-18.14.0/
./configure 
make
make install
make samples
make config
make basic-pbx
```

**4 - Validar a instalação**

```bash
/etc/init.d/asterisk status
/etc/init.d/asterisk start
rasterisk 
```



