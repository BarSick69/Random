from random import randint as rand
def adunare():
    a=rand(0,100)
    b=rand(0,100)
    print("a si b:",a,b)
    return a+b

def scadere():
    a=rand(0,100)
    b=rand(0,100)
    print("a si b:",a,b)
    return a-b,b-a

def inmultire():
    a=rand(0,100)
    b=rand(0,100)
    print("a si b:",a,b)
    return b*a
print(adunare())
print(scadere())
print(inmultire())