# Declaração de Faturamento da minha Empresa

faturamento = 1200
custo = 700 
lucro = faturamento - custo



print('O lucro foi de R$',lucro)

margem_lucro = custo / faturamento

print(f"A margem de lucro é de R${margem_lucro:.2f}")

novas_vendas = 5000
taxa = 0.05

valortotal = novas_vendas - (novas_vendas * taxa)
print('Surgiram novas vendas com uma taxa de 5%')
print('Total de R$', valortotal)

# add uma nova lista de valores (no exemplo é a receita diaria) e fiz a soma total dos valores  
lista_vendas_diarias = [1500,850,960,750]
print(f" A receita diária é {sum(lista_vendas_diarias):.2f}")
