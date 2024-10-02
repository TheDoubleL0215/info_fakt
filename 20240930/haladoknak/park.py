file = open("felajanlas.txt", "r")
raw_file = file.readlines()

data = []
for x in range(len(raw_file)):
    if x == 0:
        data.append({"length": int(raw_file[x].strip())})
    else:
        data.append({
            "start": raw_file[x].split(" ")[0],
            "end": raw_file[x].split(" ")[1],
            "col": raw_file[x].split(" ")[2].strip(),
            "id": x
        })

print("2. feladat\nA felajánlások száma:", len(data)-1)

left_right_counter = ""
for x in range(len(data)):
    if x > 0:
        if data[x]["start"] == data[0]["length"]-1 or data[x]["start"] == 1 or int(data[x]["start"]) > int(data[x]["end"]):
            left_right_counter += f"{x} "

print("3. feladat\nA bejárat mindkét oldalán ültetők:",left_right_counter)

#get_place = int(input("4. feladat\nAdja meg az ágyás sorszámát! "))
get_place = 100

givers_counter = 0
first_planter = []
for x in range(len(data)):
    if x > 0:
        if get_place in range(int(data[x]["start"]), int(data[x]["end"])):
            first_planter.append(data[x])
            givers_counter += 1

print("A felajánlók száma:", givers_counter)
if not first_planter:
    print("Ezt az ágyást nem ültetik be.")
else:
    print("A virágágyás színe, ha csak az első ültet:", first_planter[0]["col"])
    all_colors = ""
    for x in first_planter:
        if x["col"] not in all_colors:
            all_colors += f"{x['col']} "
    print(all_colors)

all_taken = True
all_pos = []
for x in range(1, data[0]["length"]):
    for y in range(len(data)):
        if y > 0:
            if int(data[y]["start"]) > int(data[y]["end"]):
                for z in range(int(data[0]["length"]), int(data[y]["start"])+1, -1):
                    all_pos.append(z)
                for alpha in range(1, int(data[y]["end"])+1):
                    all_pos.append(z)
            else:
                for x in range(int(data[y]["start"]), int(data[y]["end"])+1):
                    all_pos.append(x)
for x in range(1, data[0]["length"]):
    if x not in all_pos:
        all_taken = False
        break

print("Minden ágyás beültetésére van jelentkező" if all_taken else "")
print("A beültetés nem megoldható" if len(all_pos) < len(data) else "Átszervezéssel megoldahtó")


def Putting(id, element):
    positions.insert(id, {"col": element["col"], "id": element["id"]})

positions = [{"col": "#", "id": 0}] * data[0]["length"]
print(len(positions))

for x in range(len(data)):
    if x > 0:
        if data[x]["start"] > data[x]["end"]:
            for z in range(int(data[0]["length"]), int(data[x]["start"])+1, -1):
                positions.insert(z, {"col": data[x]["col"], "id": data[x]["id"]})
            for y in range(1, int(data[x]["end"])+1):
                positions.insert(y, {"col": data[x]["col"], "id": data[x]["id"]})
        else:
            for a in range(int(data[x]["start"]), int(data[x]["end"])+1):
                positions.insert(a, {"col": data[x]["col"], "id": data[x]["id"]})

print(len(positions))

