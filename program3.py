from random import randint as rand
def xxxDiv_Cu_6_si_8():
    numar = rand(100,999)
    while(numar%6!=0 or numar%8!=0):
        numar = rand(100,999)
    return numar
print(xxxDiv_Cu_6_si_8())