Tutorial para o ambiente virtual no windows

Para utilizar o ambiente virtual no Windows é necessário primeiramente abrir o 
prompt do Anaconda. Em seguida deve-se digitar o comando "conda create --name <nome_ambiente> python=<versao>"

Após criado o ambiente virtual é necessário ativá-lo. Para isso deve-se digitar o seguinte comando
"conda activate <nome_ambiente>".
Para instalar o 'numpy' dentro do ambiente virtual basta digitar o seguinte comando:
'pip install numpy'.
Para sair do ambiente virtual basta digitar o seguinte comando:
'conda deactivate'

========

VS Code

Para utilizar o ambiente virtual no VS Code é necessário seguir os seguintes passos:

Criar uma pasta para o projeto
Digitar no terminal "pip instal virtualenv", caso não tenha o virtualenv instalado
Para criar o ambiente virtual é necessário digitar no terminal: "python -m venv <nome_ambiente>"
Para ativar o ambiente virtual é necessário digitar no terminal: "<nome_ambiente>\Scripts\activate.bat
Digitar no terminal: "pip install <biblioteca>", para instalar as bibliotecas desejadas.


=====
Jupyter Notebook

Digitar no terminal: "<nome_ambiente>\Scripts\activate"
Instalar o Jupyter Notebook: "pip install jupyter"
Abrir o Jupyter Notebook: "jupyter notebook"
