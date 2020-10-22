import math

def sigmoid(h):
    y = 1.0/1+math.exp(-h)
    return y

def activate(x,w):
    h=0
    for i,j in zip(x,w):
        h+=i*j
    return sigmoid(h)    

w = [1,2,3]
x = [0.1,0.2,0.3]
output = activate(w,x)
print(output)
