from random import randint




def toss(faces=6):
    return randint(1,faces)

def system_iaros(counter, value_plus):
    values_toss=[]
    for i in range(counter):
        val = toss()
        if(val + value_plus >6):
            values_toss.append(val)
    return len(values_toss)