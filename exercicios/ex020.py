numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'deiz', 'onze', 'doze',
           'trese', 'catorse', 'quinze', 'desesseis', 'desessete', 'desoito', 'desenove', 'vinte')

while True:
    n_p1 = int(input("Digite um valor de 0 a 20: "))
    if 0 <= n_p1 <= 20:
        print(f"O valor digitado foi {numeros[n_p1]}")
        break
    else:
        print("Valor incorreto, tente novamente.", end="")
