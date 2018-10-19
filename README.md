# Projeto-Metodos
Projeto da cadeira Métodos Numéricos Computacionais (if816ec) do Centro de Informática (CIN) da Universidade Federal de Pernambuco

##Instalando o projeto
Para rodar o projeto, recomendo criar um virtualenv, para que as bibliotecas instaladas não entrem em conflito com as que a sua máquina já venha a possuir.

Para tal, é preciso primeiro saber se você já possui virtualenv instalada.
```shell
virtualenv --version
````  
Caso ocorra algum erro pelo fato de o pacote não estar instalado :

```shell
pip install virtualenv
````  
Para isto, é preciso ter o pip do python, e caso você não tenha, basta usar o comando

```shell
sudo apt install python3-pip
````  
caso você també não tenha o python 3
```shell
sudo apt install python3
````  

##Rodando o projeto
Agora que temos tudo instalado, vamos criar o ambiente virtual para separar as biblioteca, como foi dito em cima. Para isto é preciso estar denntro do diretório do projeto, o mesmo que tem o arquivo 'metodos.py"
```shell
virtualenv -p python3 venv
````  
Agora é preciso entrar no ambiente
```shell
source venv/bin/activate
````  
Agora que estamos no ambiente vitual, vamos instalar as bibliotecas utilizadas no projeto
```shell
pip install -r requirements.txt
```` 
Agora que tudo está instalado, basta rodar o projeto
```shell
python metodos.py
```` 
Lembando que a entrada é feita pelo arquivo entrada.txt e a saída será feita no arquivo saida.txt, as outras saídas serão as imagens do gráficos plotados, que serão geradas na mesma pasta, na forma "n° da empressão.png"

