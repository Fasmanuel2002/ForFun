import random as rd
def main():
    contador = 0
    count_bad = 10
    lower = int(input("Put lower number: ")) 
    upper = int(input("Put upper number: "))
    all_numbers = rd.randint(lower, upper)
    while(True):
        user = int(input("What number do you think is: "))
        if (user == all_numbers):
            print("horray")
            contador += 1
        elif (user != all_numbers) and user > all_numbers:
            print("You are Bad")
            print("You are higher than the number")
            count_bad -= 1
            print(f"How many chances you have {count_bad}")
            
        elif (user != all_numbers) and user < all_numbers:
            print("You are Bad")
            print("You are lower than the number")
            count_bad -= 1
            print(f"How many chances you have {count_bad}")
            pass
        if contador == 1:
            print("You win")
            break
        if count_bad == 0:
            print("You loose!")
            print(f"The number was: {all_numbers}")
            break
main()