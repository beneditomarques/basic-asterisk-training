# Instalação do Asterisk 18 no Debian 11

**Obs:** Embora a instalação do sistema operacional não seja foco deste treinamento, disponibilizamos um material para auxiliar na instalação do Debian 11 [neste link](https://github.com/beneditomarques/basic-asterisk-training/blob/main/instalacao-do-debian-11/Instalacao.md).

**1 - Download do Asterisk**

```bash
wget https://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-18.14.0.tar.gz
```

**2 - Descompactar o arquivo baixado, atualizar a lista de pacotes do Debian e instalar as dependências**

```bash
tar xzfv asterisk-18-current.tar.gz 
apt update
bash asterisk-18.*/contrib/scripts/install_prereq install
```

**3 - Compilar o Asterisk**

```bash
cd asterisk-18.*/
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



