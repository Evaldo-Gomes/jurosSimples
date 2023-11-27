# Calculadora de Juros Simples
# Apresentação
print('\n\t\t\t  -- Calculadora de Juros Simples --')
# Entradas
c = float(input('Informe o capital (R$): '))
i = float(input('Informe a taxa (%): '))
n = int(input('Informe a quantidade de parcelas: '))
# Processamento
j = (c*i*n)/100
# Saída
print(f'Juros: R$ {j}')