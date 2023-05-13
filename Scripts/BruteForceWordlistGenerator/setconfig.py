import json

# listes
all = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','\\','|',':',';',"'",
 '"','<',',','>','.','?','/','`','~','1','2','3','4','5','6','7','8','9','0','q','w','e','r','t',
 'y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E',
 'R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'," "]
SChar = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','\\','|',':',';',"'",
 '"','<',',','>','.','?','/','`','~'," "]
num = ['1','2','3','4','5','6','7','8','9','0']
allAlps = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x',
        'c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H',
        'J','K','L','Z','X','C','V','B','N','M']
SAlps = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x',
        'c','v','b','n','m']
CAlps = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H',
        'J','K','L','Z','X','C','V','B','N','M']
custo = ["A","B","Z","Y","X"]


config = "brute.json"
logpath = "brutelog.log"
def giveli(progresschar,li:list):
    return li[li.index(progresschar):]

def setlog():
    jsonconfig = json.load(open(config,"r"))
    dic = dict()
    log = open(logpath,"r").read()
    log = log.split(" ")[-1]
    for i in range(1,len(log)+1):
        dic.update({f"li{i}":giveli(log[i-1],jsonconfig[f"li{i}"])})
    json.dump(dic,open(config,"w"),indent=4)

def resetconfig(digs:int,CList:list):
    dic = dict()
    for i in range(1,digs+1):
        dic.update({f"li{i}":CList})
    json.dump(dic,open(config,"w"),indent=4)

if __name__ == "__main__":
    pass