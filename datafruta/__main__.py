from datafruta import ListaIdades
from datafruta import ListaNomes
from datafruta import ListaSalarios
from datafruta import ListaDatas
from datafruta import Data

def menu():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()
    
    listaListas = [nomes, datas, salarios, idades]

    # Teste geral de classes
    for lista in listaListas:
        lista.entradaDeDados()
        input("Pressione enter para continuar...\n")
        lista.listarEmOrdem()
        print("___________________")
        print("Mediana: " + lista.mostraMediana())
        print("Menor elemento: " + lista.mostraMenor())
        print("Maior elemento: "+lista.mostraMaior())
        print("___________________")
        print("\n")

    while True:
        print("1. Incluir um nome na lista de nomes.")
        print("2. Incluir um salário na lista de salários.")
        print("3. Incluir uma data na lista de datas.")
        print("4. Incluir uma idade na lista de idades.")
        print("5. Percorrer as listas de nomes e salários.")
        print("6. Calcular o valor da folha com um reajuste de 10%")
        print("7. Modificar o dia das datas anteriores a 2019.")
        print("8. Sair.")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            print()
            try:
                nome = input("Digite o nome: ")
                nomes.add(nome)
            except Exception as e:
                print(str(e))
        elif opcao == 2:
            print()
            try:
                salario = float(input("Digite o salario: "))
                salarios.add(salario)
            except Exception as e:
                print(str(e))
        elif opcao == 3:
            print()
            try:
                data = input("Digite a data no formato dd/mm/aaaa: ")
                dia, mes, ano = data.split("/")
                data = Data(int(dia), int(mes), int(ano))
                datas.add(data)
            except Exception as e:
                print(str(e))
        elif opcao == 4:
            print()
            try:
                idade = int(input("Digite a idade: "))
                idades.add(idade)
            except Exception as e:
                print(str(e))
        elif opcao == 5:
            print()
            percorrerNomesSalarios(nomes.lista, salarios.lista)
        elif opcao == 6:
            print()
            reajusteSalarios(salarios.lista)
        elif opcao == 7:
            print()
            filtrarDatas(datas)
        elif opcao == 0:
            break

        print()


def percorrerNomesSalarios(nomes: ListaNomes, salarios: ListaSalarios):
    '''
    Este método percorre duas listas simultaneamente
    sem a necessidade de um contador.
    '''
    for nome, salario in zip(nomes, salarios):
        print(f"{nome} recebe R${salario:.2f}")
    print()

def reajusteSalarios(salarios: ListaSalarios):
    '''
    Este método aplica um reajuste de 10% em todos os
    itens da lista de salários.
    '''
    print("Salarios originais:")
    for salario in salarios:
        print(f"R${salario:.2f}")
    print()

    salarioAjustado = map(lambda x: x * 1.1, salarios)
    print("Salarios ajustados em 10%:")
    for salario in salarioAjustado:
        print(f"R${salario:.2f}")
    print()

def filtrarDatas(datas: ListaDatas):
    '''
    Este método recebe uma lista de datas e modifica as datas que são menores que 2019
    para o dia ser dia 1.
    '''
    print("Datas Originais:")
    datas.listarEmOrdem()
    print()

    datasFiltradas = filter(lambda x: x.ano < 2019, datas.lista)
    for data in datasFiltradas:
        data.dia = 1
    print("Datas depois de modificacao: ")

    datas.listarEmOrdem()
    print()


menu()