def read():
    num = []
    with open ("./files/numbers.txt","r",encoding="utf-8") as f:
        for line in f:
            num.append(int(line))
    print (num)

def write():
    nombres = ["mario","leslie","doris","juan"]
    with open("./files/names.txt","w",encoding="utf-8") as o:
        for name in nombres:
            o.write(name)
            o.write("\n")
            


def run():
    read()
    write()

if __name__ =='__main__':run()