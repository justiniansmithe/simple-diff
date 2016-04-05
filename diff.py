import re

def differeniate(equation):
    d = re.split("([+-/*])", equation)

    #show items
    for item in d:
        if len(d) > 1:
            print(item)
    
    print('   ')    
    #power rule
    for item in d:
        base = re.findall(r'^\d', item)
        power = re.findall(r'\^(.[0-9]*)', item)       

        if len(base) > 0:
            print('The base is '+ str(base))
        if len(power) > 0:
            print('The power is '+ str(power))
            power = ''.join(power)
        elif len(power) == 0:
            power = 0

        
        base = ''.join(base)

        if power == 0:
            diff = str(base)
        else:
            try:
                d_base = int(power) * int(base)
                d_x = 'x'
                d_power = int(power) -1
                diff = str(d_base) + str(d_x) + '^' + str(d_power)
            except Exception as e:
                diff = "Working on this part! ;)"

        print(diff)
        
    return diff

#TESTS

x1 = differeniate('2x^7+x^3-x+8')
x1 = differeniate('2x^5')
#x2 = differeniate('2x^555')
#x2 = differeniate('2x^71')
#x2 = differeniate('9x^17')
x2 = differeniate('4x')



