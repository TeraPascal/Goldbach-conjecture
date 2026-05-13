import pandas as pd

while True:
    def txtreader(file):
        data = pd.read_csv(f"{file}.txt", header = None, sep = " ")
        data = data.values.tolist()[0]
        if not data[len(data)-1] > 1:
            del data[len(data)-1]
        return data
    primes = txtreader("primesuntil100000")

    num = int(input('even num :\n  >  '))
    if num%2 != 0 :
        print(f"  >  {num} is odd and doesn't meet Goldbach conjuction.\n")
    else:
        plis = []
        for p in primes:
            if p < num:
                plis.append(p)
            else:
                break
        for a in plis:
            for b in plis[0:int(len(plis)/2)+1]:
                if a + b == num:
                    print(f"  >  is the sum of two prime numbers {int(a)} and {int(b)}")
    print()   
