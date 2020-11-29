#Converting an input string into an integer:
#c = int(input('What is the temperature today in celcius?'))
#f = ((9/5)*c + 32)

#print(f)

def tempconvert(celcius):
    '''temperature converter function'''
    f = ((9/5)*celcius + 32)
    return(f)

while True:
    temp = int(input('What is the temperature today in celcius?'))
    degrees = tempconvert(temp)

    if temp == 0:
        break

    print('The temperature in farenheight today is: ',degrees) 
    print('Type 0 to exit')

    
    