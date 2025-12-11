# Declaração de Faturamento da minha Empresa

faturamento = 1200
custo = 700 
lucro = faturamento - custo
vendas = 5000
taxa = 0.1


    
print('O lucro foi de', lucro)

margem_lucro = custo / faturamento

print("a margem de lucro é de", margem_lucro)

if(vendas >= 5000):
    margem_lucro -= taxa
    print('Como sua venda passou da isenção então seu lucro foi apenas de: ', margem_lucro)