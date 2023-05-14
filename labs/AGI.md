# [AGI](https://wiki.asterisk.org/wiki/pages/viewpage.action?pageId=32375589)

**1 - Instalar o pip**

```
apt install python3-pip -y
```

**2 - Instalar a lib pyst2**

```
pip3 install pyst2
```

**3 - Criar o script: /var/lib/asterisk/agi-bin/check_user_email.agi e dar permissão de execução**

```
#!/usr/bin/python3
import requests
from asterisk import agi
import sys

agi = agi.AGI()
id = sys.argv[1]
url = f"https://reqres.in/api/users/{id}"
payload = ""
response = requests.request("GET", url, data=payload)

#print(response.json()['data']['email'])
agi.set_variable('EMAIL', response.json()['data']['email'])
```

```
chmod +x /var/lib/asterisk/agi-bin/check_user_email.agi 
```

**4 - Adicionar a subrotina no dialplan do Asterisk**

```
[check-email]
exten => s,1,Noop(Check email from ID ${ARG1})
 same =>   n,AGI(check_user_email.agi,${ARG1})
 same =>   n,Noop(RESULT: ${EMAIL})
 same =>   n,GotoIf($["${EMAIL}" = "janet.weaver@reqres.in"]?pass)
 same =>   n,Playback(invalid)
 same =>   n,Hangup()
 same =>   n(pass),Noop(EMAIL ${EMAIL} PASS)
 same =>   n,Return()
```

**5 - Adicionar a rota DDI no plano de discagem:**

 - rotas-saida.conf
 
```
;DDI
[ddi]
exten => _18002446227,1,Verbose(DDI)
 same =>              n,Gosub(record,s,1(${CALLERID(num)},${EXTEN}))
 same =>              n,Gosub(check-email,s,1(${CALLERID(num):-1}))
 same =>              n,Dial(IAX2/SIMULADOR-OPERADORA2/${EXTEN},${TIMERING})
 same =>              n,Hangup()
```

 - extensions.conf

```
[interno]
include => ddi
```

**5 - Recarregar o plano de discagem:**
```
rasterisk -x 'dialplan reload'
```


 
 
