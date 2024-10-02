file = open("fogado.txt", "r", encoding="utf-8")
raw_file = file.readlines()

data = []
for row in raw_file:
    data.append({
        "vezn": row.split(" ")[0].strip(),
        "kern": row.split(" ")[1].strip(),
        "date": {
            "h": row.split(" ")[2].split(":")[0].strip(),
            "m": row.split(" ")[2].split(":")[1].strip(),
        },
        "reg": {
            "Y": row.split(" ")[3].split(".")[0].strip(),
            "M": row.split(" ")[3].split(".")[1].strip(),
            "D": row.split(" ")[3].split(".")[2].split("-")[0].strip(),
            "h": row.split(" ")[3].split(".")[2].split("-")[1].split(":")[0].strip(),
            "m": row.split(" ")[3].split(".")[2].split("-")[1].split(":")[1].strip(),
        }
    })

print(f"2.feladat\nFoglalások száma: {len(data)}")

get_teacher = input("3.feladat\nAdjon meg egy nevet: ")
appt_counter = 0
for rec in data:
    if rec["vezn"] == get_teacher.split(" ")[0] and rec["kern"] == get_teacher.split(" ")[1]:
        appt_counter += 1

print(f"{get_teacher} néven {appt_counter} időpontfoglalás van" if appt_counter > 1 else "A megadott néven nincs időpontfoglalás")

get_time = input("4. feladat\nAdjon meg egy érvényes időpontot (pl. 17:10): ")

all_appt_that_time = []
for rec in data:
    if rec["date"]["h"] == get_time.split(":")[0] and rec["date"]["m"] == get_time.split(":")[1]:
        all_appt_that_time.append(f"{rec['vezn']} {rec['kern']}")

jelentes = open(f"{get_time.split(':')[0]}{get_time.split(':')[1]}", "w")
for item in sorted(all_appt_that_time):
    jelentes.write(f"{item}\n")
jelentes.close()

lowest_time = 9999
