
from random import randint
from math import pow

def tesadufi ():
    listim=[]
    for _ in range(5):
        listim.append(randint(20,50))
    return listim

def cut_ve_kvadrat(siyahi):
    cut=[]
    for i in siyahi:
        if i %2 == 0:
            cut.append(int(pow(i,2)))
    return cut
listler=tesadufi()
print(f"20 ilə 50 ədədi arasındakı təsadufi ədədlər bunlardır: {listler}")
cutler=cut_ve_kvadrat(listler)
print(f"20 ilə 50 ədədi arasındakı cüt ədədlərin kvadratları bunlardır: {cutler}")
