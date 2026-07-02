#Dados Cadastrais aluno
a = str(input('Nome completo: '))
data_nascimento = input('Data nascimento (dd/mm/aaaa): ')
p = float(input('Peso: '))
al = float(input('Altura (em m): '))
patologia = input('Possui alguma patologia?').strip().upper()
if patologia == 'SIM':
    qual_patologia = input('Qual patologia possui? ')
else:
    qual_patologia = 'Nenhuma'
obj = str(input('Qual o seu objetivo? '))
imc = p / al ** 2



print('===Ficha Do Aluno===')
print('Nome: {}.'.format(a))
print('Data de nascimento:', data_nascimento)
print('Peso: {} Kg.'.format(p))
print('Altura: {}cm.'.format(al))
print('Patologia: {}.'.format(qual_patologia))
print('Objetivo: {}'.format(obj))
print('IMC: {:.2f}'.format(imc))




