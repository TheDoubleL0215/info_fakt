import time
start_time = time.time()

def translator():
    grep = input("Sentence > ")
    vowels = ["A", "Á", "E", "É", "I", "Í", "O", "Ó", "Ö", "Ő", "U", "Ú", "Ü", "Ű"]
    retrun_string = ""
    for x in range(len(grep)):
        retrun_string += grep[x]
        if grep[x] in vowels:
            retrun_string += f"V{grep[x]}"
    print(retrun_string)

def diving():
    test_data = "7.23, 7.25, 7.32, 7.36, 7.41, 7.71, 7.81"
    print("A hét adatai:", test_data)
    for x in range(0,6):
        if float(test_data.split(",")[x]) < float(test_data.split(",")[x-1]) and x!=0:
            print("A gyöngyhalásznak nem volt jó hete!")
            break
    print("A gyöngyhalásznak jó hete volt!")
    


diving()
print("--- %s seconds ---" % (time.time() - start_time))

