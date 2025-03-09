from products import *

print("Bem-vindo ao sistema de gerenciamento de produtos!")
b = 2

c = inventory()
d = product()

for a in range (0,b,1):
    print(f"------------------ Número de acessos: {a+1} ------------------")
    exec = int(input("Quais sao suas ordens? \n1)Adicionar itens \n2)Deletar itens\n3)mostrar itens\n4)modificar itens \n5)sair\n\n"))
    if exec == 1:
        c.addItems()
        b += 1
        
    elif exec == 2:
        c.deleteItems()
        b += 1

    elif exec == 3:
        c.showItems()
        b += 1
        
    elif exec == 4:
        c.modifyItems()
        b += 1
        
    elif exec == 5:
        break
    
    else:
        print("número não identificado")
        b += 1
    
d.csv()