file = open("furdoadat.txt", "r")
raw_file = file.readlines()

data = []
for row in raw_file:
    data.append({
        "id": row.split(" ")[0],
        "p_id": row.split(" ")[1],
        "act": row.split(" ")[2],
        "h": int(row.split(" ")[3]),
        "m": int(row.split(" ")[4]),
        "s": int(row.split(" ")[5])
    })

print(f"""2.feladat\nAz első vendég {data[0]["h"]}:{data[0]["m"]}:{data[0]["s"]}-kor lépett ki az öltözőből.""")

for x in range(len(data)-1, 0, -1):
    if data[x]["act"] == "1" and data[x]["p_id"] == "0":
        print(f"Az utolsó vendég {data[x]['h']}:{data[x]['m']}:{data[x]['s']}-kor lépett ki az öltözőből.")
        break

all_regs = []
for x in data:
    id_reg_counter = 0
    for y in data:
        if x["id"] == y["id"]:
            id_reg_counter += 1
    all_regs.append({"id": x["id"], "acts": id_reg_counter})

sorted_all_regs = []
[sorted_all_regs.append(x) for x in all_regs if x not in sorted_all_regs]

once_counter = 0
for x in sorted_all_regs:
    if x["acts"] <= 4:
        once_counter += 1
print(f"3. feladat\nA fürdőben {once_counter} vendég járt csak egy részlegen")

id_time = []
for x in data:
    if x["act"] == "1" and x["p_id"] == "0":
        for y in range(data.index(x), len(data)):
            if x["id"] == data[y]["id"] and data[y]["act"] == "0" and data[y]["p_id"] == "0":
                id_time.append({"id": x["id"], "time": (data[y]["h"]*360+data[y]["m"]*60+data[y]["s"])-(x["h"]*360+x["m"]*60+x["s"])})

sorted_id_time = []
[sorted_id_time.append(x) for x in id_time if x not in sorted_id_time]
print(sorted_id_time)

highest = {"id": 0, "time": 0}
all_highest = []
for x in sorted_id_time:
    if abs(x["time"]) >= highest["time"]:
        highest = x
for x in sorted_id_time:
    if abs(x["time"]) == highest["time"]:
        all_highest.append(x)

print(all_highest)

time_window_69 = 1
time_window_916 = 0
time_window_1620 = 0
for x in range(len(data)):
    if x>0:
        if data[x]["id"] != data[x-1]["id"]:
            if 5 < data[x]["h"] < 9: 
                time_window_69 += 1
            elif 9 <= data[x]["h"] < 16:
                time_window_916 += 1
            elif 15 < data[x]["h"] < 20:
                time_window_1620 += 1
print(f"5.feladat\n6-9 óra {time_window_69}\n9-16 óra {time_window_916}\n16-20 óra {time_window_1620}")