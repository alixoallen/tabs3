while True:
    a=int(input('quer ver a tabuada de qual valor ? : '))
    print('-'*30)
    if a<0:
        print('tabuada invalida')
        break
    for x in range (1,11):
         print(f'{a}x{x}={a*x}')