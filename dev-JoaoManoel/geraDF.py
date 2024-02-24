from faker import Faker
import pandas as pd
import numpy as np

fake = Faker('pt-BR')
dataframe = pd.DataFrame(columns=['cpf', 'nome', 'idade', 'sexo', 'email', 'notaEnem', 'craP2', 'craP4', 'craP6', 'abandono', 'semestreAbandono'])

dataframe['cpf'] = [fake.cpf() for _ in range(1000)]
dataframe['sexo'] = [fake.random_element(elements=('M', 'F')) for _ in range(1000)]
dataframe['nome'] = [fake.name_male() if sexo == 'M' else fake.name_female() for sexo in dataframe['sexo']]
dataframe['idade'] = np.random.randint(18, 28, size=1000)
dataframe['email'] = [fake.email() for _ in range(1000)]
dataframe['notaEnem'] = np.random.randint(640, 800, size=1000)
dataframe['abandono'] = [fake.boolean() for _ in range(1000)]
dataframe['semestreAbandono'] = [fake.random_int(min=1, max=8) if abandono else None for abandono in dataframe['abandono']]
dataframe['craP2'] = [fake.random_int(min=5, max=10) if not semestreAbandono else fake.random_int(min=5, max=10) if semestreAbandono > 2 else None for semestreAbandono in dataframe['semestreAbandono']]
dataframe['craP4'] = [fake.random_int(min=5, max=10) if not semestreAbandono else fake.random_int(min=5, max=10) if semestreAbandono > 4 else None for semestreAbandono in dataframe['semestreAbandono']]
dataframe['craP6'] = [fake.random_int(min=5, max=10) if not semestreAbandono else fake.random_int(min=5, max=10) if semestreAbandono > 6 else None for semestreAbandono in dataframe['semestreAbandono']]

dataframe.to_csv('alunos.csv', index=False)