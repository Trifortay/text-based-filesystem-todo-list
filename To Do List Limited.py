def reset():
    with open("file.tri","w") as file:
        for x in range(0,64):
            file.write("0")     #Entries
        for x in range(64,256):
            file.write("-")     #Names
        for x in range(256,1535):
            file.write("+")     #Desc
    
def read(chktst):
    with open("file.tri","r") as file:
        for x in range(len(chktst)):
            file.seek(0)
            if chktst[x] == "1":
                file.seek(64+3*x)
                print(f"{x+1}: {file.read(3)}", end=" ")
                file.seek(0)
                file.seek(256+20*x)
                print(f"{file.read(20)}")
           # indexes=
           
        pass

def write():
    print(2)
    pass

with open("file.tri","r") as file:    #Make checksum
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
