
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

# Exception
class DigitsErr(Exception):
    def __init__(self, msg="Given digits of word is not obeying digits of wordlist."):
        self.msg = msg
        super().__init__(msg)

def letternext(liste,letter):
    try :
        return liste[liste.index(letter)+1]
    except:
        return liste[0]

def checkforlast(listelast,word):
    islast = True
    for i in word:
        if i != listelast:
            islast = False
    return islast

def next(liste:list,word):
    if checkforlast(liste[-1],word):
        return
    word.reverse()
    indexcou = 0
    finish = 0
    for i in word:
        if i == liste[-1]:# one of many digs have to be changed.
            word[word.index(i)] = letternext(liste,i)
            if i == word[0]: # its the first digs of the word.
                word.reverse()
                return word
            finish = 1
            indexcou+=1
        elif finish == 1:# i is not last but a word to be changed lastly
            word[indexcou] = letternext(liste,i)
            word.reverse()
            return word
        else:
            word[word.index(i)] = letternext(liste,i)
            word.reverse()
            return word

def bruteforce(liste,digs,countinues:list=None):
    if countinues == None: word = [liste[0] for i in range(digs)]
    else:
        word = countinues
        if len(countinues) != digs:
            countinues = "".join(countinues)
            raise DigitsErr(f"Continue: {countinues} doesn't have {digs} number of digits")
    for i in range(digs**len(liste)):
        yield word
        word = next(liste,word)
        if word == None:
            yield None
            break
