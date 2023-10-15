p = float(input("Preço do produto: R$"))
desconto = (p / 100) * 5
print(f"O produto que valia R${p}, com 5% de desconto vai valer R${p - desconto:.2f}")
