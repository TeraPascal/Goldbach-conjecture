import pandas as pd

while True:
    def txtreader(file):
        data = pd.read_csv(f"{file}.txt", header = None, sep = " ")
        data = data.values.tolist()[0]
        if not data[len(data)-1] > 1:
            del data[len(data)-1]
        return data
    primes = txtreader("primesuntil100000")

    def goldbach(num):
        solved = 0
        plis = []
        for p in primes:
            if p < num:
                plis.append(p)
            else:
                break
        for a in plis:
            for b in plis[0:int(len(plis)/2)+1]:
                if a + b == num:
                    print(f"  >  {num} is the sum of two prime numbers {int(a)} and {int(b)}")
                    solved = 1
                    break
            if solved == 1:
                break

    
    limit = int(input('maximum number of the fact check range for Goldbach conjecture :\n  >  '))
    print()

    for n in range(limit):
        num = n+1
        if num%2 == 0:
            goldbach(num)
        
    print()   
