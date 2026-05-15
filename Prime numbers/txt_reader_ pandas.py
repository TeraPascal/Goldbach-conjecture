import pandas as pd

def txtreader(file):
    data = pd.read_csv("primesuntil1000.txt", header = None, sep = " ")
    data = data.values.tolist()[0]
    if not data[len(data)-1] > 1:
        del data[len(data)-1]
    return data

data = txtreader("primesuntil1000")
