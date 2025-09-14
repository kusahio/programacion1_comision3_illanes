import random

numeros = random.sample(range(1, 51), 25)
carton = [numeros[i:i+5] for i in range(0,25,5)]
tombola = ''


print('\nTu cartón inicial:\n')
for fila in carton:
    print(fila)

while tombola != 'n':
    index = None
    bingo = random.randint(1,50)
    ganador = []
    
    for  fila in carton:
        
        if bingo in fila:
            index = fila.index(bingo)
            fila[index] = 0
            print(f'\nSe sortea el número... {bingo} -> Lo tienes.')
            break
        
        elif carton.index(fila) == len(carton) - 1 and bingo not in fila:
            print(f'\nSe sortea el número... {bingo} -> No lo tienes.')
        
        elif sum(fila) == 0:
            print(f'\nHas completado la fila {carton.index(fila)+1}!')

        ganador.extend(fila)
    print('\nTu cartón actualizado:\n')
    
    for fila in carton:
        print(fila)
    
    print(f'\nganador {ganador}')
    # if sum(ganador) == 0:
    #     print('\nHas ganado')
    #     break

    tombola = input('\nSortear número?: S/N: ').lower()