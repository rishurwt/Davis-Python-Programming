Entries = []
size = int(input("Total number of elements : "))
for i in range( size ):
    entry = int(input(f"Enter {i+1} element : "))
    Entries.append(entry)


for i in Entries:
    if(i > 50):
        print(i)