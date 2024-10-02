import random
import string

file = open("asd.txt", "r", encoding="utf-8")
raw_data = file.readlines()

data = []
for row in raw_data:
    record = {
        "side": row.split(" ")[0].strip(),
        "width": row.split(" ")[1].strip(),
        "color": row.split(" ")[2].strip()
    }
    data.append(record)

print("Feladat 2: ", len(data))

if data[len(data)-1]["side"] == "0":
    tempCount = 0
    for row in data:
        if row["side"] == "0":
            tempCount += 2
    print("Feladat 3a: ",)
    print("Feladat 3b: ", tempCount )
else:
    print("Feladat 3a: páratlan")

odd_plots = []
for x in range(len(data)):
    if data[x]["side"] == "1":
        odd_plots.append(data[x])

even_plots = []
for x in range(len(data)):
    if data[x]["side"] == "0":
        even_plots.append(data[x])

for x in range(len(odd_plots)):
    if(odd_plots[x]["color"] != ":" and odd_plots[x]["color"] != "#"):
        if odd_plots[x]["color"] == odd_plots[x+1]["color"] or odd_plots[x]["color"] == odd_plots[x-1]["color"]:
            print("Feladat 4: ", (x*2)+1)
            break
    
def ColorMyFence(plot, data_set):
    chosen = False
    while chosen == False:
        choice = random.choice(string.ascii_letters).upper()
        if choice != data_set[data_set.index(plot)+1]["color"] and choice != data_set[data_set.index(plot)-1]["color"] and plot["color"] != choice:
            chosen = True
            return choice
    
house_number = int(input("Házszám > "))
print("Feladat 5a: ", data[house_number]["color"])

if house_number % 2 == 0:
    print("Feladat 5b: ",ColorMyFence(even_plots[int(house_number/2)-1], even_plots))
else:
    print("Feladat 5b: ",ColorMyFence(odd_plots[int((house_number-1)/2)], odd_plots))

utca_txt = open("utcakep.txt", "w")

first_row = ""
second_row = ""
for x in range(len(odd_plots)):
    first_row += int(odd_plots[x]["width"]) * odd_plots[x]["color"]
    house_number = x*2+1
    spaces = (int(odd_plots[x]["width"])-len(str(house_number))) * " "
    second_row += f"{house_number}{spaces}"
    
utca_txt.write(f"{first_row}\n{second_row}")