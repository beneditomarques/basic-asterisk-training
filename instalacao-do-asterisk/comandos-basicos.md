# Comandos básicos do Asterisk e dicas

**Dicas**

 - Entrar na CLI (Command Line Interface - Interface de Linha de Comando) do Asterisk

```bash
asterisk -r
```


 - Entrar na CLI do Asterisk com outro nível de debug:

```bash
asterisk -rvvv
```

 - Completamento de linha de comando

```bash
core show <tab><tab>
```

**Tabela de comandos**

Comando                                       | Descrição
---------------------------------------------- | ------------
pjsip show settings | Exibe as configurações atuais do módulo chan_pjsip.so|
pjsip show endpoints | Exibe a lista de endpoints|
pjsip show endpoint [endpoint] | Exibe a configuração individual de um endpoint |
pjsip show auths | Exibe a lista de objetos de autenticação |
pjsip show auth [auth] | Exibe a configuração individual de um objeto de autenticação  |
pjsip show aors | Exibe a lista de objetos AOR (Address Of Record - Endereço de registro) |
pjsip show aor [aors] | Exibe a configuração individual de um AOR|
dialplan show	 | Exibe todo o plano de discagem carregado atualmente na memória |
dialplan show [dialplan context]	 | Exibe um contexto específico do plano de discagem carregado atualmente na memória |
dialplan reload	 | Recarrega o plano de discagem |
module load [module name] | Carrega um módulo no Asterisk |
module unload [module name]	 | Descarrega um módulo do Asterisk |
module reload [module name]	 | Recarrega um módulo do Asterisk |
![shell command] | Executa um comando do shell do linux dentro da CLI do Asterisk |
core show channels	 | Exibe informações sobre os canais que estão em ligação no momento |
core show settings	 | Exibe as configurações do core do Asterisk|
core show translation	 | Exibe a matriz de tradução de codecs |
core show uptime	 | Exibe informações sobre o tempo de atividade do Asterisk |
core show applications	 | Exibe as aplicações disponíveis no Asterisk (apenas dos módulos que estão carregados) |
core show application [nome da aplicação]	 | Exibe as informações sobre uma aplicação específica disponível no Asterisk (apenas se o módulo correspondente estiver carregado) |
core show functions	 | Exibe as funções disponíveis no Asterisk (apenas dos módulos que estão carregados) |
core show function [nome da função]	 | Exibe as informações sobre uma função específica disponível no Asterisk (apenas se o módulo correspondente estiver carregado) |
core set verbose [verbosity level]	 | Configura o nível de detalhamento (verbosidade) na CLI do Asterisk|
core restart now	 | Restarta o Asterisk |
core stop now	 | Para o Asterisk |
core restart when convenient	 | Restarta o Asterisk apenas quando não houver mais ligações, e não permite novas chamadas |
core stop when convenient	 |  Para o Asterisk apenas quando não houver mais ligações, e não permite novas chamadas  |
core restart gracefully | Restarta o Asterisk apenas quando não houver mais ligações, mas permite novas chamadas |
core stop gracefully | Para o Asterisk apenas quando não houver mais ligações, mas permite novas chamadas |
reload	 | Reload global no Asterisk |
core show help  | Exibe toda a lista de comandos do Asterisk e a descrição | 
core show help [Asterisk command]	 | Exibe a documentação ajuda de um comando específico |