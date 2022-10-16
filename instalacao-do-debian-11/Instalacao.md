# Instalação do Debian 11


## Pré-requisitos
 - [Virtualbox](https://www.virtualbox.org/wiki/Downloads) mais novo instalado no seu computador.
 - O sistema operacional da máquina host não é relevante (Windows/Linux/MacOS).

## Instalação

**1 - Baixar a ISO do site oficial:**


[https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-11.5.0-amd64-netinst.iso](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-11.5.0-amd64-netinst.iso)


**2 - Criar uma nova máquina virtual no Virtualbox:**

![virtualbox-botao-new.png](./virtualbox-botao-new.png)

![virtualbox-configuracao-vm.png](./virtualbox-configuracao-vm.png)


![virtualbox-memoria.png](./virtualbox-memoria.png)

![virtualbox-hard-disk.png](./virtualbox-hard-disk.png)

![virtualbox-hard-disk-type.png](./virtualbox-hard-disk-type.png)


![virtualbox-hard-disk-grow.png](./virtualbox-hard-disk-grow.png)

![virtualbox-hard-disk-size.png](./virtualbox-hard-disk-size.png)


![virtualbox-settings.png](./virtualbox-settings.png)

![virtualbox-settings-boot-order.png](./virtualbox-settings-boot-order.png)

![virtualbox-selecting-disk.png](./virtualbox-selecting-disk.png)

![virtualbox-selected-disk.png](./virtualbox-selected-disk.png)

**3 - Coloque a placa de rede da VM em modo Bridge conforme a imagem abaixo.**

![virtualbox-network.png](./virtualbox-network.png)

Obs: Caso esteja utilizando o sistema operacional Linux, utilize o comando "ip a s" para listar as placas de rede e verificar qual é a utilizada por você. No print abaixo estamos utilizando a interface "wlp0s20f3", então esta será a interface a ser configurada no campo "Nome".

![linux-network.png](./linux-network.png)


**4 - Inicialize a máquina virtual recém criada e comece a instalação do Debian 11:**

![virtualbox-start.png](./virtualbox-start.png)

**5 - Escolha o modo gráfico de instalação e deixe as configurações conforme os prints abaixo:**


![debian-1.png](./debian-1.png)

![debian-2.png](./debian-2.png)


![debian-3.png](./debian-3.png)

![debian-4.png](./debian-4.png)

![debian-5.png](./debian-5.png)

**6 - Digite o domínio de sua preferência. Neste exemplo, colocamos o domínio como "local.domain"**
 
![debian-6.png](./debian-6.png)

**7 - Digite a senha do usuário "root":**

![debian-7.png](./debian-7.png)

**8 - Digite um nome de usuário. Usaremos o usuário "suporte" como exemplo em nossas aulas:**

![debian-8.png](./debian-8.png)

![debian-9.png](./debian-9.png)

**9 - Digite a senha do usuário "suporte" criado anteriormente:**
 
![debian-10.png](./debian-10.png)

**10 - Escolha a região de acordo com a sua localidade:**
  
![debian-11.png](./debian-11.png)

**11 - Utilize o modo "assistido" para facilitar a instalação. Obs: as seguintes opções que foram selecionadas para efetuar o particionamento de disco não é a configuração adequada para instalações em ambiente de produção, mas sim apenas o suficiente para o que precisaremos no curso.**

![debian-12.png](./debian-12.png)

![debian-13.png](./debian-13.png)

![debian-14.png](./debian-14.png)

![debian-15.png](./debian-15.png)

![debian-16.png](./debian-16.png)

![debian-17.png](./debian-17.png)

![debian-18.png](./debian-18.png)

![debian-19.png](./debian-19.png)

**12 - Não é necessário digitar nada na próxima tela, apenas continue:**
  
![debian-20.png](./debian-20.png)

![debian-21.png](./debian-21.png)

 - **Atenção:**  Este é o passo mais importante durante a instalação! Deixe as opções marcadas conforme o print para que o ambiente gráfico não seja instalado e possamos também ter um servidor SSH para efetua acesso remoto durante as aulas.
 
![debian-22.png](./debian-22.png)


![debian-23.png](./debian-23.png)


![debian-24.png](./debian-24.png)


 - **Parabéns!** Agora você tem o Debian 11 instalado.
 
![debian-25.png](./debian-25.png)






























