import os

sc = '-sc'
for fname in os.listdir('./txt'):
    if sc in fname:
        print(fname, "has the keyword")