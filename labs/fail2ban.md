# Segurança: Fail2Ban

**1 - Instalar o pacote fail2ban:**

```bash
apt-get install fail2ban -y
```

**2 - Edite o arquivo /etc/asterisk/logger.conf para fazer o asterisk gerar logs, e recarregue para aplicar:**

```bash
[general]

[logfiles]
console = verbose,notice,warning,error,debug
messages = notice,warning,error
;full = verbose,notice,warning,error,debug
;security = security
```

```bash
rasterisk -x 'logger reload'
```
 
**3 - Crie a Jail `iptables-asterisk` criando o arquivo /etc/fail2ban/jail.d/asterisk.local:**

```bash
[iptables-asterisk]
enabled = true
findtime = 300
maxretry = 3
bantime = 86400
backend = polling
logpath = /var/log/asterisk/messages
filter  = asterisk
action  = iptables[name=ASTERISK, port=5060, protocol=udp]
          iptables-multiport[name=ASTERISK, port=10000:20000, protocol=udp]
```

**4 - Restarte o Fail2ban**:
```bash
systemctl restart fail2ban
```

**5 - Cheque as jails carregadas**:

```bash
fail2ban-client status 
fail2ban-client status asterisk-iptables
```

**6 - Observe as regras de firewall existentes**:

```bash
iptables-save
```
**7 - Realize tentativas de autenticação inválidas com o softphone, observar o log do Fail2Ban e as regras de firewall criadas automaticamente para o bloqueio**

```bash
tail -f /var/log/fail2ban.log 
2023-06-10 13:24:38,117 fail2ban.filter         [2162]: INFO    [iptables-asterisk] Found 192.168.100.127 - 2023-06-10 13:24:37
2023-06-10 13:24:38,119 fail2ban.filter         [2162]: INFO    [iptables-asterisk] Found 192.168.100.127 - 2023-06-10 13:24:37
2023-06-10 13:24:38,121 fail2ban.filter         [2162]: INFO    [iptables-asterisk] Found 192.168.100.127 - 2023-06-10 13:24:37
2023-06-10 13:24:38,123 fail2ban.filter         [2162]: INFO    [iptables-asterisk] Found 192.168.100.127 - 2023-06-10 13:24:37
2023-06-10 13:24:38,125 fail2ban.filter         [2162]: INFO    [iptables-asterisk] Found 192.168.100.127 - 2023-06-10 13:24:37
2023-06-10 13:24:38,127 fail2ban.filter         [2162]: INFO    [iptables-asterisk] Found 192.168.100.127 - 2023-06-10 13:24:37
2023-06-10 13:24:38,282 fail2ban.actions        [2162]: NOTICE  [iptables-asterisk] Ban 192.168.100.127
```

```bash
root@debian:~# iptables-save | grep f2b
:f2b-ASTERISK - [0:0]
-A INPUT -p udp -m multiport --dports 10000:20000 -j f2b-ASTERISK
-A INPUT -p udp -m udp --dport 5060 -j f2b-ASTERISK
-A f2b-ASTERISK -s 192.168.100.127/32 -j REJECT --reject-with icmp-port-unreachable
-A f2b-ASTERISK -s 192.168.100.127/32 -j REJECT --reject-with icmp-port-unreachable

```

**8 - Para retirar o banimento**:

```bash
fail2ban-client unban --all
```
**9 - Use o parâmetro "ignoreip" ara adicionar exceções para as suas redes internas**:

```bash
[iptables-asterisk]
enabled = true
ignoreip = 192.168.100.0/24
findtime = 300
maxretry = 3
bantime = 86400
backend = polling
logpath = /var/log/asterisk/messages
filter  = asterisk
action  = iptables[name=ASTERISK, port=5060, protocol=udp]
          iptables-multiport[name=ASTERISK, port=10000:20000, protocol=udp]
```

```bash
systemctl restart fail2ban 
```

```
tail -f /var/log/fail2ban.log 

2023-06-10 13:39:09,495 fail2ban.filter         [2342]: INFO    [iptables-asterisk] Ignore 192.168.100.127 by ip
2023-06-10 13:39:09,496 fail2ban.filter         [2342]: INFO    [iptables-asterisk] Ignore 192.168.100.127 by ip
2023-06-10 13:39:09,496 fail2ban.filter         [2342]: INFO    [iptables-asterisk] Ignore 192.168.100.127 by ip
2023-06-10 13:39:09,497 fail2ban.filter         [2342]: INFO    [iptables-asterisk] Ignore 192.168.100.127 by ip
2023-06-10 13:39:09,497 fail2ban.filter         [2342]: INFO    [iptables-asterisk] Ignore 192.168.100.127 by ip

