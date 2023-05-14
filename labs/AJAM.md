# [AJAM](https://wiki.asterisk.org/wiki/pages/viewpage.action?pageId=4817256)

**1 - Ativar o recurso web no manager.conf, e incluir a rede 192.168.100.0/24 no usuário 'admin'**

```
[general]
webenabled = yes
```
```
[admin]
permit=192.168.100.0/255.255.255.0
```


**2 - Configurar o http.conf**

```
[general]
enabled=yes
bindaddr=0.0.0.0
bindport=8088
```



**3 - Recarregar os módulos do manager e http no Asterisk**


```
rasterisk -x 'module reload manager'
```

```
rasterisk -x 'module reload http'
```

**4 - Acessar http://192.168.100.153:8088/amanager para executar os comandos:**

```
Action: QueueSummary
```


