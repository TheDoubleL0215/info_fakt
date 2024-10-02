file = open("ajto.txt", "r", encoding="utf-8")
raw_file = file.readlines()

data = []
for row in raw_file:
    data.append({
        "hour": row.split(" ")[0],
        "min": row.split(" ")[1],
        "id": row.split(" ")[2],
        "act": row.split(" ")[3].strip(),
    })


print(f"2. feladat \nAz első belépő: {data[0]['id']}") # mert biztosan tudjuk hogy üres volt az épület
for x in range(len(data)-1, 0, -1):
    if data[x]["act"] == "ki":
        print(f"Az utolsó kilépő: {data[x]['id']}")
        break

only_id = []
for x in data:
    only_id.append(int(x['id']))

act_sum_list = []

for x in range(len(only_id)):
    if{"id": only_id[x],"count": only_id.count(only_id[x])} not in act_sum_list:
        act_sum_list.append({
            "id": only_id[x],
            "count": only_id.count(only_id[x])
        })


athaladas_txt = open("athaladas.txt", "w")
athaladasok = []
for item in act_sum_list:
    athaladasok.append({
        'id': item['id'],
        'count': item['count']
    })
    athaladas_txt.write(f"{item['id']} {item['count']}\n")

stayed_id_peoples = ""
for item in athaladasok:
    if item['count'] % 2 != 0:
        stayed_id_peoples += f"{item['id']} "

print(f"4. feladat\nA végén a társalgóban voltak: {stayed_id_peoples}")

date_times = []
all_count = 0
for item in data:
    if item['act'] == "be":
        all_count += 1
    else:
        all_count -= 1
    date_times.append({'hour': item['hour'], 'min': item['min'], 'count': all_count})
most_people = {'hour': 0, 'min': 0, 'count': 0}
for item in date_times:
    if int(item['count']) > most_people['count']:
        most_people = item
print(f"Például {most_people['hour']}:{most_people['min']}-kor voltak a legtöbben a társalgóban")

get_id = input("Adja meg a személy azonosítóját! > ")
act_of_id = []
for item in data:
    if item['id'] == get_id:
        act_of_id.append(item)

for x in range(len(act_of_id)):
    print(act_of_id[x])
    if len(act_of_id) % 2 == 0:
        print(f"{act_of_id[x]['hour']}:{act_of_id[x]['min']}-{act_of_id[x+1]['hour']}:{act_of_id[x+1]['min']}")
        x+=1
    else:
        print(f"{act_of_id[x]['hour']}:{act_of_id[x]['min']}-{act_of_id[x+1]['hour'] if x+1 < len(act_of_id)else''}:{act_of_id[x+1]['min']if x+1 < len(act_of_id)else''}")
    x+=1


