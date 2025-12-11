# Declaração de Faturamento da minha Empresa

faturamento = 1200
custo = 700 
lucro = faturamento - custo
vendas = 5000
taxa = 0.1


    
print('O lucro foi de R$', lucro)

margem_lucro = custo / faturamento

print("A margem de lucro é de R$", margem_lucro)

if vendas >= 5000:
    margem_lucro -= taxa
    print('Como sua venda passou da isenção então seu lucro foi apenas de: ', margem_lucro)

print('O lucro foi de R$',lucro)

margem_lucro = custo / faturamento

print(f"A margem de lucro é de R${margem_lucro:.2f}")

novas_vendas = 5000
taxa = 0.05

valortotal = novas_vendas - (novas_vendas * taxa)
print('Surgiram novas vendas com uma taxa de 5%')
print('Total de:', valortotal)
print('Total de R$', valortotal)

nome = "AdryEly rosaRio de olIveIra"
nome_upper = nome.upper()
print(nome_upper)
print('Total de R$', valortotal)

#alteração matias - lista de impostos
impostos = [5,10,15,20]
for i in range(len(impostos)):
    print(f"Imposto de {i+1}: {impostos[i]}%")



nome_lower = nome.lower()
print(nome_lower)

for i in range(5):
    print(i)