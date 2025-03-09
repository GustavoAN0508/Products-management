class product:
    #variáveis globais da classe produto
    global prod
    prod = list()
    
    def csv() -> None:
        for b in range(0, len(prod), 1): 
            with open("test.csv", "w") as test:
                test.write(f"{prod[b][0]},{prod[b][1]},{prod[b][2]}\n")
            
    
class inventory(product):
    #variáveis globais da classe inventário
    global price 
    global iden 
    global quantity 
    
    price = []
    iden = []
    quantity = []
        
    #adicionar itens ao inventário
    def addItems() -> None:
        a = 2
        for b in range(0, a, 1):
            
            price.append(float(input("Coloque um preço aqui: ")))
            iden.append(str(input("Coloque um nome no produto: ")))
            quantity.append(int(input("Coloque a qtd. de itens: ")))
            prod.append([price[b], iden[b], quantity[b]])
            
            next = input("Deseja continuar a adicionar?\nS/N\n").upper()
            if next == "SIM" or next == "S":
                print(f"---------------------vezes que voce ja adicionou itens: {b+1}--------------------")
                a += 1
                
            else:
                print(f"--------------------vezes que voce ja adicionou itens: {b+1}--------------------")
                break
            
    #deletar itens do inventário     
    def deleteItems() -> None:
        a = 1
        for b in range(0, a, 1):
            choose = int(input(f"Selecione o Item que você quer deletar: (1-{len(prod)})")) - 1 #até porquê ninguém é obrigado a saber que uma lista começa do 0
            for c in range (0, len(prod), 1):
                if choose == 0:
                    print("Erro!")
                    break
                elif c == choose and c != 0:
                    prod.remove(choose)      
            choose2 = input("Deseja continuar deletando?\nS/N")
            if choose2 == "S" or choose2 == "SIM":
                print(f"---------------------vezes que voce ja deletou itens: {b+1}--------------------")
                a += 1
                continue
            
            else:
                break                      
                
    #mostrar elementos específico dos itens      
    def showItems() -> None:
        a = 1
        for b in range(0, a, 1):
            print(f"------------------vezes que voce ja pesquisou {b}------------------")
            
            choose = int(input("Escolha o que você quer pesquisar?\n1)preço \n2)identificação \n3)quantidade \n4)mostrar todas as categorias de um item \n5)mostrar tudo"))
            if choose == 1:
                numero = int(input("Coloque o numero da coluna: ")) - 1
                print(prod[numero][0])
                break
                    
            elif choose == 2:
                numero = int(input("Coloque o numero da coluna: ")) - 1
                print(prod[numero][1])
                break
            
            elif choose == 3:
                numero = int(input("Coloque o numero da coluna: ")) - 1
                print(prod[numero][2])
                break
            
            elif choose == 4:
                numero = int(input("Coloque o numero da coluna: ")) - 1
                print(f"{prod[numero][0]}|{prod[numero][1]}|{prod[numero][2]}")
                break
            
            elif choose == 5:
                for c in range (0, len(prod),1):
                    print(f"{prod[c][0]}|{prod[c][1]}|{prod[c][2]}")
                break
            
            
            else:
                print("Número inválido")
                a += 1
                continue
            
    #modifica itens do elemento escolhido
    def modifyItems():
        a = 1
        for b in range(0, a, 1):
            print(f"------------------vezes que voce ja modificou {b}------------------")
            
            choose = int(input("Escolha o que você quer modificar?\n1)preço \n2)identificação \n3)quantidade"))
            if choose == 1:
                numero = int(input("Coloque o numero da coluna: ")) - 1
                prod[numero][0] = float(input("Modifique o preço para o valor desejado: "))
                print(f"Preço alterado para: {prod[numero][0]}")
                break
                    
            elif choose == 2:
                numero = int(input("Coloque o numero da coluna: ")) - 1
                prod[numero][1] = str(input("Modifique o valor da identificação para o valor desejado: "))
                print(f"identificação alterada para: {prod[numero][1]}")
                break
            
            elif choose == 3:
                numero = int(input("Coloque o numero da coluna: ")) - 1
                prod[numero][2] = int(input("Modifique a quantidade do produto desejado: "))
                print(f"Quantidade de produtos alterada para: {prod[numero][2]}")
                break
            
            else:
                a += 1
                continue
