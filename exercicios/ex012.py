produto = float(input("Qual é o valor do produto?R$ "))
desconto = (produto / 100) * 5
print(f"Um produto que custava {produto}, com 5% de desconto passou a custar {produto - desconto:.2f}")
