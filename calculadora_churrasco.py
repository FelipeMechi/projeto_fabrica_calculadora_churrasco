# Crie um programa que calcule a quantidade de bebidas e de carne
# para a organização de um churrasco

# Etapas da resolução:
# 1) Solicitar o número de convidados
# 2) Criar uma função para calcular a quantidade total de bebidas
# 3) Criar uma função para calcular a quantidade total de carnes
# 4) Apresentar o resultado com valores de total de carne e bebidas
# a serem comprados

# 1)  Solicitar o número de convidados
convidados = int(input('Digite o número de convidados: '))

# 2) Criar uma função para calcular a quantidade total de bebidas
def calcular_bebidas(convidados, consumo_por_pessoa_ml =800, volume_garrafa_litro =2.25):
    total_ml = convidados * consumo_por_pessoa_ml
    total_litro = total_ml/1000

    garrafas = int(total_litro//volume_garrafa_litro)
    if total_litro % volume_garrafa_litro > 0:
        garrafas += 1
    return total_litro, garrafas

#resultado = calcular_bebidas(convidados)
#print(resultado)

def calcular_carne(convidados, consumo_por_pessoa_grama=400):
    total_gramas = convidados * consumo_por_pessoa_grama
    total_kg = total_gramas /1000
    return total_kg


litro, garrafas = calcular_bebidas(convidados)
carne_kg = calcular_carne(convidados)

print('\n___Quantidade total para Churrasco___')
print(f'Número de convidados: {convidados}')
print(f'Refrigerante necessários: {litro:.2f} litros.')
print(f'Garrafas de 2,5L: {garrafas} unidades.')
print(f'Carne Necessária: {carne_kg:.2f} Kg.')