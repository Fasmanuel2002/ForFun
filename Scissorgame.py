
contador = 0
contador2 = 0
while(True):
    p1 = input("P1: What do you want: rock/scissors/paper: ").capitalize()
    p2 = input("P2: What do you want: rock/scissors/paper: ").capitalize()
    
   
    if p1 != "Scissors" or p1 != "Rock" or p1 != "Paper":
            pass
    if p2 != "Scissors" or p2 != "Rock" or p2 != "Paper":
            pass
   
    if (p1 == "Scissors") and (p2 == "Paper" ):
        print("First player won! ")
        contador += 1 
        
        
    elif (p1 == "Paper") and (p2 == "Rock" ):
        print("First player won!")
        contador += 1
        
    elif (p1 == "Rock") and (p2 == "Scissors" ):
        print("First player won! ")
        contador += 1
        
    elif (p1 == "Scissors") and (p2 == "Paper" ):
        print("First player won! ")
        contador += 1
        
    elif (p2 == "Paper") and (p1 == "Rock" ):
        print("Second player won!")
        contador2 += 1
        
    elif (p2 == "Rock") and (p1 == "Scissors" ):
        print("Second player won! ")
        contador2 += 1
        
    elif (p2 == "Scissors") and (p1 == "Paper" ):
        print("Second player won! ")
        contador2 += 1
    
    if contador == 2 or contador2 == 2:
        break

print(f"The first player won: {contador}")
print(f"The second player won: {contador2}")
