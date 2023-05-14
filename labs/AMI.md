# [AMI](https://wiki.asterisk.org/wiki/display/AST/Asterisk+18+AMI+Actions)

**1 - Configurar o manager.conf**

```
[general]
enabled = yes
;webenabled = yes
port = 5038
bindaddr = 0.0.0.0

[admin]
secret = 1WHK5j93
deny=0.0.0.0/0.0.0.0
permit=127.0.0.1/255.255.255.0
read = agent
write = originate
```

**2 - Recarregar o módulo no Asterisk**

```
rasterisk -x 'module reload manager'
```


**3 - Logar no manager utilizando o telnet**

```
telnet localhost 5038
```

```
Action: login
Username: admin
Secret: 1WHK5j93
Events: Off
```

**4 - Realizar uma ligação:**

```
Action: Originate
Channel: PJSIP/1000
Context: interno
Exten: 8830348888
Priority: 1
Callerid: 8830348888
Timeout: 30000
```

**5 - Listar filas:**

```
Action: QueueSummary
```



