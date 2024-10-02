import random

file = open("pakli.txt", "r", encoding="utf-8-sig")
raw_data = file.readlines()

data = []


for row in raw_data:
    data.append({
            "type": row[:2].strip(),
            "value": row[2:].strip()
        }) 
    
for x in range(1001):
    first = random.randint(0, len(data)-1)
    second = random.randint(0, len(data)-1)
    if first != second:
       data[first], data[second] = data[second], data[first]
    else:
        x -= 1 


output = ""
for x in data:
    output += f"{x['type']}{x['value']} " 

print(output)

sum_value = 0
counter = 0
sum_cards = []
for x in range(len(data)):
    real_value = 0
    if data[x]["value"] == "J" or data[x]["value"] == "Q" or data[x]["value"] == "K" :
        real_value = 10
    elif data[x]["value"] == "Á":
        real_value = 11
    else: 
        real_value = int(data[x]["value"]) 

    if real_value+sum_value <= 21:
        sum_value += real_value        
        sum_cards.append(data[x])
    elif data[x]["value"] == "Á" and 1+sum_value <= 21:
        sum_value += 1       
        sum_cards.append(data[x])

print("Black Jack: ",sum_cards)