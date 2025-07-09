filename="file.tri"
chktst="0"

def reset():
    with open(filename,"w") as file:
        for x in range(0,64):
            file.write("0")     #Entries
        for x in range(64,256):
            file.write("-")     #Names
        for x in range(256,1535):
            file.write("+")     #Desc

def resetsoft():
    with open(filename,"r+") as file:
        for x in range(64):
            file.write("0")
    
def read2(chktst):
    with open(filename,"r") as file:
        for x in range(len(chktst)):
            file.seek(0)
            if chktst[x] == "1":
                file.seek(64+3*x)
                print(f"{x+1:2}: {file.read(3)}", end=" - ")
                file.seek(0)
                file.seek(256+20*x)
                print(f"{file.read(20)}")


def write2():
    with open(filename,"r+") as file:
        bleb=1
        while bleb==1:
            try:
                id_entry_tmp=int(input("ID (1-64): "))
                if id_entry_tmp > 65 or id_entry_tmp < 1:
                    print("pick a ID from 1-64 please.") 
                else:
                    id_entry=id_entry_tmp-1
                    bleb=0                  
            except ValueError:
                print("Please Enter a valid ID number.")
        
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
        file.write(" "*3)
        file.seek(64+id_entry*3)
        file.write(name_entry)
        
        file.seek(0)
        file.seek(256+id_entry*20)
        file.write(" "*20)
        file.seek(0)
        file.seek(256+id_entry*20)
        file.write(data_entry)

def delete2():
    while True:
        try:
            del_entry=int(input("Which entry to delete: "))
            break
        except ValueError:
            print("Please Enter an ID number")
    with open(filename,"r+") as file:
        file.seek(del_entry-1)
        file.write("0")

try:
    with open(filename,"r") as file:    #Make checksum
        
        chktst=file.read(64)
        #print(chktst)
except FileNotFoundError:
    reset()
    
if not chktst.isdigit():
    reset()

for x in range(64):                    #check checksum
    if chktst[x] != "0" and chktst[x] != "1":
        reset()
        break

while True:
    i_o=input("Read or Write or Delete or Delete All [r/w/d/x]: ").lower()
    if i_o == "r":
        read2(chktst)
        break
    elif i_o == "w":
        write2()
        break
    elif i_o == "d":
        delete2()
        break
    elif i_o == "x":
        deleteall=input("Are you sure (Enter \"YES\" in all caps)")
        if deleteall == "YES":
            resetsoft()
            break

    else:
        print("Please enter \"r\" or \"w\" or \"d\" or \"x\".")
        continue
