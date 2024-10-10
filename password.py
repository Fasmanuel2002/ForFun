import random as rd

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","p","q","r","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","-","_"]
choose_password = [rd.choice(letters) for _ in range(rd.randint(7,10))]
print(" ".join(choose_password))