from faker import Faker
import numpy as np
import pandas as pd

def rand_cpf():
    numbers = np.random.randint(0, 10, size = 11)
    cpf = ''.join(map(str, numbers))
    cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    return cpf


def gerar_dataframe(n = 1000):
    faker = Faker('pt_BR') # criando objeto faker


    cpfs = [rand_cpf() for _ in range(n)]
    genders = [np.random.choice(['M', 'F']) for _ in range(n)]
    names = [faker.name() for _ in range(n)]
    addresses = [faker.address().replace("\n", " ") for _ in range(n)]
    ages = [np.random.randint(18, 28) for _ in range(n)]
    enem_grade = [np.random.randint(640, 801) for _ in range(n)]
    not_active = [np.random.choice([True, False]) for _ in range(n)]
    droupout = [np.random.randint(1, 9) if not_active[student] == True else np.nan for student in range(n)]
    cra_2 = [np.random.uniform(5, 10) if sem > 2 or np.isnan(sem) else np.nan for sem in droupout]
    cra_4 = [np.random.uniform(5, 10) if sem > 4 or np.isnan(sem) else np.nan for sem in droupout]
    cra_6 = [np.random.uniform(5, 10) if sem > 6 or np.isnan(sem)else np.nan for sem in droupout]

    # arredondando as notas
    cra_2 = np.round(cra_2, 2)
    cra_4 = np.round(cra_4, 2)
    cra_6 = np.round(cra_6, 2)

    data_frame = pd.DataFrame({'CPF': cpfs, 'Nome': names, 'Sexo': genders, 'Idade': ages, 
                            'Endereço': addresses, 'Nota do ENEM': enem_grade, 'Abandono': not_active,
                            'Semestre de desistência': droupout, 'CRA até 2º semestre': cra_2,
                            'CRA até 4º semestre': cra_4, 'CRA até 6º semestre': cra_6})

    return data_frame

def save_csv(data_frame, file_name):
    data_frame.to_csv(file_name, index = False)


