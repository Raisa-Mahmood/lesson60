print("Lello! Wemcome to prime number finding game!\n")
print("Input a number to know all the prime numbers between the range of 2 to it!\\n")
print("Let's start!🚀\n")
n=int(input("→Enter your number here!\n"))
prime=[True]*(n+1)
prime[0]=prime[1]=False
for i in range(2, int(n**0.5)+1):
    if prime[i]:
        for j in range(i*i,n+1,i):
            prime[j]=False
print("\n Prime numbers up to ",n, "are: ")
for i in range (n+1):
    if prime [i]:
        print(i,end="")
print("\n Great job!")

