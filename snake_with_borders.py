from os import system
import keyboard
from random import randrange
from time import sleep


###functions 

def output_2(lista,cialo,punkt_1,punkt_2):
    
    for x in range(len(lista)):
        for j in range(len(lista[x])):
            coor=str(x)+str(j)
            if coor in cialo:
                print("O",end=" ")
            elif coor not in cialo:
                print("-",end=" ")
        print("")
def output(lista,cialo,punkt_1,punkt_2):
    punkty=[]
    coor_2=str(punkt_1)+str(punkt_2)
    punkty.append(coor_2)
    for x in range(len(lista)):
        for j in range(len(lista[x])):
            coor=str(x)+str(j)
            if coor in punkty:
                print("X",end=" ")
            elif coor in cialo:
                print("O",end=" ")
            elif coor not in cialo:
                print("-",end=" ")
            
        print("")

        
def left(lista):
    global dlugosc
    global dane_1,dane_2
    global pomoc
    global cialo
    lista[dane_1][dane_2]=" "
    if dane_2-1<0:
        pomoc=2
        
    try:
            if lista[dane_1][dane_2-1]=="X":
                
                dane_1=dane_1
                dane_2=dane_2-1
                dlugosc+=1
                coor=str(dane_1)+str(dane_2)
                cialo.append(coor)
                
                
                pomoc=1
                
                
                
            elif lista[dane_1][dane_2-1]=="O":
                pomoc=2
            else:
                
                dane_1=dane_1
                dane_2=dane_2-1
                coor=str(dane_1)+str(dane_2)
                cialo.append(coor)
                del cialo[0]
                sleep(0.1)
            
    except IndexError:
            pomoc=2

def right(lista):
    global dlugosc, dane_1,dane_2,pomoc,cialo
   
    lista[dane_1][dane_2]=" "
    if dane_2+1>len(lista):
        pomoc=2
    
        

    try:
            if lista[dane_1][dane_2+1]=="X":  
                  
                dane_1=dane_1
                dane_2=dane_2+1
                dlugosc+=1
                coor=str(dane_1)+str(dane_2)
                cialo.append(coor)
                
                
                pomoc=1
                
                
                
                
            elif lista[dane_1][dane_2+1]=="O":
                pomoc=2
            else:
                dane_1=dane_1
                dane_2=dane_2+1
                coor=str(dane_1)+str(dane_2)
                cialo.append(coor)
                del cialo[0]
                sleep(0.1)
    except IndexError:
        pomoc=2
def up(lista):
    global pomoc,dlugosc,dane_1,dane_2,cialo
    
    lista[dane_1][dane_2]=" "
    if dane_1-1<0:
        pomoc=2
        

    try:
            if lista[dane_1-1][dane_2]=="X":    
                
                dane_1=dane_1-1
                dane_2=dane_2
                dlugosc+=1
                coor=str(dane_1)+str(dane_2)
                cialo.append(coor)
               
                
                pomoc=1
                
                
                
                
            elif lista[dane_1-1][dane_2]=="O":
                pomoc=2
            else:
                lista[dane_1-1][dane_2]="O"
                dane_1=dane_1-1
                dane_2=dane_2
                coor=str(dane_1)+str(dane_2)
                cialo.append(coor)
                del cialo[0]
                sleep(0.1)

    except IndexError:
        pomoc=2
def down(lista):
    global pomoc,dlugosc,dane_1,dane_2,cialo
    lista[dane_1][dane_2]=" "
    if dane_1+1>len(lista):
            pomoc=2
        
    try:
            if lista[dane_1+1][dane_2]=="X":
                
                dane_1=dane_1+1
                dane_2=dane_2
                dlugosc+=1
                coor=str(dane_1)+str(dane_2)
                cialo.append(coor)

                pomoc=1
                
                
                
                
                
            elif lista[dane_1+1][dane_2]=="O":
                pomoc=2
            else:
                lista[dane_1+1][dane_2]="O"
                dane_1=dane_1+1
                dane_2=dane_2
                coor=str(dane_1)+str(dane_2)
                cialo.append(coor)
                del cialo[0]
                sleep(0.1)

    except IndexError:
        pomoc=2
        
def move(lista):
    global dlugosc
    global dane_1,dane_2
    global pomoc
    global direction
    
    

    if keyboard.is_pressed("w"):
        direction="up"
    elif keyboard.is_pressed("a"):
        direction="left"
    elif keyboard.is_pressed("d"):
        direction="right"
    elif keyboard.is_pressed("s"):
        direction="down"

    sleep(0.2)
    system("cls")
    

    if direction=="left":
        left(lista)
        if pomoc==2:
            print(f"You lost, your score: {dlugosc-1}")
            sleep(4)
            
            

    if direction=="right":
        right(lista)
        if pomoc==2:
            print(f"You lost, your score: {dlugosc-1}")
            sleep(4)
            

    if  direction=="up":
        up(lista)
        if pomoc==2:
            print(f"You lost, your score: {dlugosc-1}")
            sleep(4)
           
            
    
    if  direction=="down":
        down(lista)
        if pomoc==2:
            print(f"You lost, your score: {dlugosc-1}")
            sleep(4)
      
    if keyboard.is_pressed("w"):
        direction="up"
    elif keyboard.is_pressed("a"):
        direction="left"
    elif keyboard.is_pressed("d"):
        direction="right"
    elif keyboard.is_pressed("s"):
        direction="down"
    
    
    

    
    

def punkt():
    global punkt_1,punkt_2,lista
    punkt_1=int()
    punkt_2=int()

    punkt_1=randrange(0,len(lista))
    punkt_2=randrange(0,len(lista[punkt_1]))
    coor= str(punkt_1)+str(punkt_2)
    while coor in cialo:
        punkt_1=randrange(0,len(lista))
        punkt_2=randrange(0,len(lista[punkt_1]))
    lista[punkt_1][punkt_2]="X"
    

system("cls")
lista=[]
dlugosc=1
szerokosc=input("Width: ")
wysokosc=input("Height: ")
szerokosc=int(szerokosc)
wysokosc=int(wysokosc)

while (szerokosc%2==0 or wysokosc%2==0):
    system("cls")
    print("Give me the numbers that arent even numbers, numbers which type is int,numbers which are " " ")
    szerokosc=(input("Width: "))
    wysokosc=(input("Height: "))

szerokosc=int(szerokosc)
wysokosc=int(wysokosc)

punkt_1=0
punkt_2=0



while True:
    cialo=[]
    coor=str(wysokosc)+str(szerokosc)
    cialo.append(coor)
    dlugosc=1
    lista.clear()
    for x in range (0,wysokosc):
        lista.append([])
        for j in range(0,szerokosc):
            lista [x].append(" ")

    pomoc=0
    lista[punkt_1][punkt_2]=" "
    dane_1=szerokosc//2
    dane_2=wysokosc//2
    direction="left"
    

    while True:
        
        system("cls")
        if pomoc==2:
            break
        
        lista[punkt_1][punkt_2]=" "
        pomoc=0
        
        while True:
            if pomoc==2:
                break
            
            punkt()

            while True:
                pomoc=0
                move(lista)
                if pomoc==1:
                    output_2(lista,cialo,punkt_1,punkt_2)
                else:
                    output(lista,cialo,punkt_1,punkt_2)
                print("")
                print(f"Score: {dlugosc-1}",end="")
                sleep(0.4)
                if pomoc==1:
                    break
                elif pomoc==2:
                    break
                else:
                    continue









