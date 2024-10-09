dobas_txt = open("dobasok.txt", "r")
osveny_txt = open("osvenyek.txt", "r")
dobas_raw = dobas_txt.readlines()
osveny_raw = osveny_txt.readlines()

dobas_data = []
osveny_data = []

for x in range(len(dobas_raw[0])):
    if dobas_raw[0][x] != " " and dobas_raw[0][x] != "\n":
        dobas_data.append(dobas_raw[0][x])

for record in osveny_raw:
    row = []
    for x in range(len(record)):
        if record[x] != '\n':
            row.append(record[x].strip())
    osveny_data.append(row)

print(f"2. feladat:\nA dobások száma: {len(dobas_data)}\nAz ösvények száma: {len(osveny_data)}")

longest_path = {"id": 0, "length": 0}
for x in range(len(osveny_data)):
    if len(osveny_data[x]) > longest_path["length"]:
        longest_path = {"id": x+1, "length": len(osveny_data[x])}

print(f"3. feladat\nAz egyik leghosszabb a(z): {longest_path['id']}. ösvény, hossza: {longest_path['length']}")

get_path = int(input("Adja meg egy ösvény sorszámát! > "))
get_players = int(input("Adja meg a játékosok számát! > "))

print(osveny_data[get_path-1])

zones = {"M": 0, "V": 0, "E": 0}
for x in osveny_data[get_path-1]:
    if x == "M":
        zones["M"] = zones["M"]+1
    elif x == "V":
        zones["V"] = zones["V"]+1
    elif x == "E":
        zones["E"] = zones["E"]+1

print("5. feladat")
for key, value in zones.items():
    print(f"{key}: {value} darab")

special_txt = open("kulonleges.txt", "w")
for x in range(len(osveny_data[get_path-1])):
    if osveny_data[get_path-1][x] != "M":
        special_txt.write(f"{x+1}\t{osveny_data[get_path-1][x]}\n")
special_txt.close()

log = {}
#initialize players
for x in range(1, get_players+1):
    log[x] = 0
print(log)

current_player = 1
round = 1
for x in dobas_data:
    if round <= len(osveny_data[get_path-1]):
        if current_player > get_players+1:
            current_player = 1
        log[current_player] += int(dobas_data[round])
        if log[current_player] >= len(osveny_data[get_path-1]):
            break
        current_player += 1
        round += 1

print(log)



