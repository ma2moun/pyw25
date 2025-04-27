for x in range(1,4):
    print(f"Multiplication table of {x}", end="\t")
print()
for i in range(1,4):
    for j in range(1,4):
        print(f"{j} X {i} = {j*i}", end="\t\t\t")
    print() 
