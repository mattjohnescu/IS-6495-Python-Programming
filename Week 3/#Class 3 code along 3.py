#Class 3 code along 3
apples = "apples"
for c in apples:
    print(c)
    
total = 0 
for i in range(10000):
    total += i

print("sum of all numbers from 0 to 10000:", total)


characters = ["Batman","Lex Luther","Wonder Women","Robin","Loki","Aquaman","Flash"]
#loops for each variable in list, the for is count based nad definitive on the size of the list
for item in characters:
    print(item)

#combo of range and length function
for item in range(len(characters)):
    print(item)

for item in range(len(characters)):
    print(characters[item])
    characters.append("Black Adam")


for item in characters:
    print(item.upper)

characters = ["Batman", "Superman", "Aquaman", "Green Lantern", "Wonder Woman"]
