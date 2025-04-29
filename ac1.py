print("Welcome to the number chechicking game!")
print("Let's check if your input number is prime or not!\n")
number=int(input("→Enter your number!\n"))
if number>1:
    for i in range(2,number):
        if number%i==0:
            print(f"Oh no! number {number} is not a prime number.")
            break
    else:
        print(f"Yes! number {number} is a prime number!")
else:
    print("Numbers less than 2 are not prime numbers!")
print("Thanks for playing the game. 😊")
        