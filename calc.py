import re

print('My calc')
print('Type Quit to exit\n')
previous = 0
run = True

def performMath():
    global run
    global previous
    equation = input('enter equation:')
    if equation == 'quit' :
        run = False
    else:
        equation = re.sub('[a-zA-z,.:()" "]','',equation)
        previous = eval(equation)
        print('you typed', previous)

while run:
        performMath()
