import datetime
while True:
    f=[]
    print("\n\n.\n..\n...\n..\n.\n")

    def prime(num):
        l = divisors(num)
        if len(l) == 2:
            return(1)
        else:
            return(0)
        
    def divisors(num):
        l=[]
        for i in range(num):
            i = i+1
            r = num%i
            if r == 0 :
                l.append(i)
        return(l)
            
    limit = int(input('maximum number to solve :\n  >  '))
    print("\n")

    for n in range(limit):
        n = n+1
        print(datetime.datetime.now(),f" - solving for {n} ..")
        if prime(n) == 1:
            f.append(n)        

    with open(f"primesuntil{limit}.txt","w+") as txt:
        for i in range(len(f)):
            txt.write(f"{f[i]} ")
        
    print(f"\nprime numbers found until number {limit} prime numbers in this range are:\n {f}")    
    print("done.")
