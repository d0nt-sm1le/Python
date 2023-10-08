s1 = float(input("Primeiro segmento: "))
s2 = float(input("Segundo segmento: "))
s3 = float(input("Terceiro segmento: "))

if s1 == s2 == s3:
    print("Os segmentos acima PODEM um triângulo EQUILATERO!")

elif s1 == s2 != s3:
    if s1 + s2 > s3:
        print("Os segmentos acima PODEM um triângulo ISÓCELES!")
    else:
        print("Os segmentos acima NÃO PODEM formar um triângulo ISÓCELES!")

else:
    if s1 + s2 > s3:
        print("Os segmentos acima PODEM um triângulo ESCALENO!")
    else:
        print("Os segmentos acima NÃO PODEM formar um triângulo ESCALENO!")
