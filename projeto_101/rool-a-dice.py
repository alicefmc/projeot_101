import random
yes = "y"
no = "n"
response = input("Quer jogar o dado? ")
if response == "n":
    while response == "n":
        print("Fim")
        break

      
if response == "y":
    print(random.randint(1,6))
    response1 = input("Quer jogar o dado de novo? ")
    while response1 == "y":
        print(random.randint(1,6))
        response1 = input("Quer jogar o dado de novo? ")  
        while response1 == "n":
            print("fim")
            break