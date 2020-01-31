import socket
def main():
    print('''
  _   _    _  _ _  ___
 / \ | |  | || | || __|
| o || |_ | || V || _|
|_n_||___||_| \_/ |___| by @humblelad

FAST TOOL TO FIND IF THE HOST IS UP!!!
''')
    f=open("read.txt","r")
    count=0

    f1=f.readlines()
    for sd in f1:
        aas=sd.strip()
        print("CHECKING  "+ aas+" --> ",end='')

        try:
            w=socket.gethostbyname(aas)

            print("Up!",sep='')
            count=count+1

        except socket.error:
            print("\033[31m" + "Down!"+"\033[0m",sep='')

        print("\n")

    print("\n Total hosts FOUND to be UP ARE :  "+str(count))


if __name__=="__main__" :
    main()


