i=2520
inloop=True
while inloop:
    if  (i%11==0)\
    and (i%12==0)\
    and (i%13==0)\
    and (i%14==0)\
    and (i%15==0)\
    and (i%16==0)\
    and (i%17==0)\
    and (i%18==0)\
    and (i%19==0):
        inloop=False
    else:
        i+=20
print(i)
