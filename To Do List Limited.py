filename="file.tri"

def reset():
    with open(filename,"w") as file:
        for x in range(0,64):
            file.write("0")     #Entries
        for x in range(64,256):
            file.write("-")     #Names
        for x in range(256,1535):
            file.write("+")     #Desc
    
def read(chktst):
    with open(filename,"r") as file:
        for x in range(len(chktst)):
            file.seek(0)
            if chktst[x] == "1":
                file.seek(64+3*x)
                print(f"{x+1}: {file.read(3)}", end=" ")
                file.seek(0)
                file.seek(256+20*x)
                print(f"{file.read(20)}")


def write():
    with open(filename,"r+b") as file:
        id_entry=int(input("ID (1-64): "))
        while True:
            name_entry=input("Name (3 bytes): ")
            if "-" in name_entry:
                print("\"-\" isn't supported")
            elif len(name_entry) > 3:
                print(f"Enter a maximum of 3 bytes. You entered {len(name_entry)} bytes.")
            else:
                break
        
        while True:
            data_entry=input("Data (20 bytes): ")
            if "+" in data_entry:
                print("\"+\" isn't supported")
            elif len(data_entry) > 20:
                print(f"Enter a maximum of 20 bytes. You entered {len(data_entry)} bytes.")
            else:
                break
        file.seek(id_entry)
        file.write("1")
        file.seek(0)
        file.seek(64+id_entry*3)
        #fill in how to do the f string thing later
        file.write()
        file.seek(0)
        file.seek(256+data_entry*20)
        file.write()



with open(filename,"r") as file:    #Make checksum
    chktst=file.read(64)
    print(chktst)
if not chktst.isdigit():
    reset()

for x in range(64):                    #check checksum
    if chktst[x] != "0" and chktst[x] != "1":
        reset()
        break

while True:
    i_o=input("Read or Write [r/w]: ").lower()
    if i_o == "r":
        read(chktst)
        break
    elif i_o == "w":
        write()
        break
    else:
        print("Please enter \"r\" or \"w\".")
        continue
