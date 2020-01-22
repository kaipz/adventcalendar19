import math

i = 0
f = 0
init_intcode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0]
current_intcode = init_intcode
check = 19690720


def add(noun, verb, address):
    # print("adding")
    address = noun + verb
    return address

def mult(noun, verb, address):
    # print("multing")
    address = noun * verb
    return address


def runner(intcode):
    for x in range(len(intcode)):
        a = x/4
        if a.is_integer():
            if intcode[x] is 1:
               out_add = add(intcode[intcode[x+1]], intcode[intcode[x+2]], intcode[intcode[x+3]])
               if out_add is check:
                   print("y")
            elif intcode[x] is 2:
                out_mult = mult(intcode[intcode[x+1]], intcode[intcode[x+2]], intcode[intcode[x+3]])
                
                # print(out_mult)
                if out_mult is check:
                   print("y")
            elif intcode[x] is 99:
                break
            else:
                continue

current_intcode[1] = 0
current_intcode[2] = 0

while i < 100: 

    while f < 100:
        runner(current_intcode)
        f = f + 1
        # print("i = "+str(i)+" and f = "+str(f))
        # current_intcode = init_intcode
        current_intcode[2] = f

    
    i = i + 1
    f = 0
    current_intcode[1] = i




