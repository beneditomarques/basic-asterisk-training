
 - Instalar o MariaDB e compilar o conector ODBC para o MariaDB

```bash
apt update && apt install mariadb-server -y 
apt-get install unixodbc-dev unixodbc odbc-mariadb cmake -y
cd /opt/
git clone https://github.com/MariaDB/mariadb-connector-odbc.git
mkdir build && cd build
cmake ../mariadb-connector-odbc/ -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCONC_WITH_UNIT_TESTS=Off -DCMAKE_INSTALL_PREFIX=/usr/local -DWITH_SSL=OPENSSL
cmake --build . --config RelWithDebInfo
make install
```

 - Inicializar o serviço

```bash
systemctl enable --now mariadb
```

 - Colocar senha no usuário root

```sql
GRANT ALL ON *.* TO 'root'@'%' IDENTIFIED BY '9ZLH56F3v7rg' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```
 - Criar usuário admin

```sql
CREATE USER 'admin'@'localhost' IDENTIFIED BY '9ZLH56F3v7rg';
GRANT ALL PRIVILEGES ON * . * TO 'admin'@'localhost';
FLUSH PRIVILEGES;
```

 - Instalar o PhpMyAdmin

```bash
docker run -d --restart=always --network=host -e APACHE_PORT=9090 -e PMA_HOST=127.0.0.1 -e PMA_USER=admin -e PMA_PASSWORD=9ZLH56F3v7rg --name phpmyadmin phpmyadmin/phpmyadmin
```

 - Acessar o phpmyadmin
[http://192.168.100.153:9090/](http://192.168.100.153:9090)

 - Criar o banco de dados

```sql
CREATE DATABASE asteriskcdrdb;
```

 - Criar tabelas cdr e cel:

```sql 
CREATE TABLE IF NOT EXISTS `cdr` (
    accountcode VARCHAR(20), 
    src VARCHAR(80), 
    dst VARCHAR(80), 
    dcontext VARCHAR(80), 
    clid VARCHAR(80), 
    channel VARCHAR(80), 
    dstchannel VARCHAR(80), 
    lastapp VARCHAR(80), 
    lastdata VARCHAR(80), 
    start DATETIME, 
    answer DATETIME, 
    end DATETIME, 
    duration INTEGER, 
    billsec INTEGER, 
    disposition VARCHAR(45), 
    amaflags VARCHAR(45), 
    userfield VARCHAR(256), 
    uniqueid VARCHAR(150), 
    linkedid VARCHAR(150), 
    peeraccount VARCHAR(20), 
    sequence INTEGER
);

CREATE TABLE IF NOT EXISTS `cel` (
	`id` int(11) NOT NULL auto_increment,
	`eventtype` varchar(30) NULL,
	`eventtime` datetime NULL,
	`cid_name` varchar(80) NULL,
	`cid_num` varchar(80) NULL,
	`cid_ani` varchar(80) NULL,
	`cid_rdnis` varchar(80) NULL,
	`cid_dnid` varchar(80) NULL,
	`exten` varchar(80) NULL,
	`context` varchar(80) NULL,
	`channame` varchar(80) NULL,
	`src` varchar(80) NULL,
	`dst` varchar(80) NULL,
	`channel` varchar(80) NULL,
	`dstchannel` varchar(80) NULL,
	`appname` varchar(80) NULL,
	`appdata` varchar(80) NULL,
	`amaflags` int(11) NULL,
	`accountcode` varchar(20) NULL,
	`uniqueid` varchar(32) NULL,
	`linkedid` varchar(32) NULL,
	`peer` varchar(80) NULL,
	`userdeftype` varchar(255) NULL,
	`eventextra` varchar(255) NULL,
	`userfield` varchar(255) NULL,
	PRIMARY KEY (`id`),
	KEY `uniqueid_index` (`uniqueid`),
	KEY `linkedid_index` (`linkedid`)
);
```

 - Configurar o arquivo /etc/odbc.ini

```
[MariaDB-client]
Description=MariaDB-client
Driver=MariaDB
SERVER=localhost
USER=admin
PASSWORD=9ZLH56F3v7rg
DATABASE=asteriskcdrdb
PORT=3306
```

 - Configurar o arquivo /etc/odbcinst.ini
 
```
[MariaDB]
Driver=/usr/local/lib/mariadb/libmaodbc.so
Description=MariaDB
```

```bash
rasterisk -x 'module reload res_odbc.so'
```

 - Testar conexão com isql 
 
```bash 
isql MariaDB-client -v
``'

 - Configurar o arquivo /etc/asterisk/cdr_adaptive_odbc.conf
 
``` 
[first]
connection=asterisk
table=cdr
```

 - Configurar o arquivo /etc/asterisk/cel_odbc.conf

```
[general]
[first]
connection=asterisk
table=cel
```

 - Configurar o arquivo /etc/asterisk/cel.conf
 
```
[general]
enable=yes
apps=dial,park
events=ALL

[manager]
[radius]
```

 - Recarregar os módulos
 
```bash 
module reload cdr_adaptive_odbc.so 
module reload cel
module reload cel_odbc.so 
```
