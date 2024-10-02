pages = ""
for x in range (1,129):
    pages += str(x)
print(pages)
num_input = int(input("Negyjegyu szam > "))
print(f"Van benne: {pages.find(str(num_input))+1}" if str(num_input) in pages else "A szám nem fordul elő!")  