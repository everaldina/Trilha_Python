# Linux

Este tutorial é para sistemas operacionais Linux baseado no Ubuntu

## Anaconda

O metodo para criação de ambientes virtuais escolhido foi o Anaconda por ser simples e já ser automaticamente detectado pelo VS Code (editor de codigo utilizado).

Com o Anaconda instalado ele te permite escolher por alterar a configuração do terminal para sempre iniciar já com o terminal do anacoda (base) ativo.
Caso rejeite essa opção você pode simplesmente ativa-lo quando precisar com o comando:

```
eval "$(/home/john/anaconda3/bin/conda shell.YOUR_SHELL_NAME hook)" 
```


No terminal padrão do Linux você pode utilizar:
```
eval "$(/home/john/anaconda3/bin/conda shell.bash hook)" 
```

## Criação de ambiente virtual
Com o Anaconda instalado, a criação de um environment (ambiente virtual) é simples, apenas por o comando no terminal:

```
conda create -n nomeAmbiente
```

Opcionalmente você pode definir qual python você quer que aquele ambiente rode:
```
conda create -n nomeAmbiente python=3.11
```


Para ativar o ambiente virtual, use:

```
conda activate trilhaPython
```

Para desativar o ambiente virtual, use

```
conda deactivate
```

## Configuração do ambiente virtual

Com o ambiente virtual ativo, você pode instalar os pacotes que quiser usando o proprio conda com:

```
conda install pacote
```

Ou com o pip (mais recomendado):

```
pip install pacote
```

Caso não tenha o pip instalado no ambiente basta usar:
```
conda install pip
```

## Utilização do ambiente virtual no VS Code

O VS Code já detecta automaticamente todos os ambientes virtuais criados pelo Anaconda.

Mas também é possivel utilizar apenas com o terminal.
Abra um terminal, ative o ambiente virtual desejado e rode o projeto via comando.