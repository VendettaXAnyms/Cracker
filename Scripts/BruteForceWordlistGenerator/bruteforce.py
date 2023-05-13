import time
import sys
import hashlib
import json

# Initials

logaddr = "brutelog.log"
with open(logaddr,"a") as f:
     f.write("")


# Vars
file = open("bruteresu.txt","a")
liste = json.load(open("brute.json","r"))

# Functions

def per(digs,listw,word_no):
  e = listw**digs
  return (round(word_no/e,10))*100
def log(word):
     with open(logaddr,"w") as i:
          i.write(f"last word {word}")
def cal_est(tot,count,speed):
  if speed!=0:
    return int((tot-count)/speed)
  else:
    return "Not known"
def ishash(word,findinghash):
   nowhash = hashlib.md5(bytes(word,encoding="utf-8")).hexdigest()
   Homehash = findinghash
   if Homehash == nowhash:
        print(f"Key is {word}")
        i = open("Keytex.txt","a")
        i.write(f"[Word : {word} :: hash : {nowhash} :: Homehash : {findinghash}]")
        i.close()
        return True
   else:
        return False
def bruteforce(liste,digs):
    if digs>0:
       li1 = liste["li1"]
    if digs>1:
      li2 = liste["li2"]
    if digs>2:
      li3 = liste["li3"]
    if digs>3:
      li4 = liste["li4"]
    if digs>4:
      li5 = liste["li5"]
    if digs>5:
      li6 = liste["li6"]
    if digs>6:
      li7 = liste["li7"]
    if digs>7:
      li8 = liste["li8"]
    if digs>8:
      li9 = liste["li9"]
    
    coun = 1
    prevc = coun
    stri = ""
    sp = 0
    timer = time.time()
    timer1 = time.time()
    tott = len(liste)**digs
    for i1 in li1:
     if digs > 1:
      for i2 in li2:
       if digs > 2:
        for i3 in li3:
         if digs > 3:
          for i4 in li4:
           if digs > 4:
            for i5 in li5:
             if digs > 5:
              for i6 in li6:
               if digs > 6:
                for i7 in li7:
                 if digs > 7:
                  for i8 in li8:
                   if digs > 8:
                     for i9 in li9:
                      if time.time()-timer >= 1:
                         sp = (coun - prevc)
                         prevc = coun
                         timer = time.time()
                      else:
                         pass
                      word = f"{i1}{i2}{i3}{i4}{i5}{i6}{i7}{i8}{i9}"
                      log(word)
                      file.write(word.__add__("\n"))
                      pri_str = f"word:{word} ".__add__(f"coun:{coun} per:{round(per(digs,len(liste),word_no=coun),5)}% time:{round(time.time()-timer1,1)} size:{sys.getsizeof(stri)} spd: {sp} WPS est: {cal_est(tot=tott,count=coun,speed=sp)}secs")
                      stri = stri.__add__(f"{word}\n")
                      coun += 1
                      print(pri_str)
                      stri = ""
                   else:
                     if time.time()-timer >= 1:
                       sp = (coun - prevc)
                       prevc = coun
                       timer = time.time()
                     else:
                       pass
                     word = f"{i1}{i2}{i3}{i4}{i5}{i6}{i7}{i8}"
                     log(word)
                     file.write(word.__add__("\n"))
                     pri_str = f"word:{word} ".__add__(f"coun:{coun} | per:{round(per(digs,len(liste),word_no=coun),5)}% | time:{round(time.time()-timer1,1)} | size:{sys.getsizeof(stri)} | spd: {sp} WPS | est: {cal_est(tot=tott,count=coun,speed=sp)} secs")
                     stri = stri.__add__(f"{word}\n")
                     coun += 1
                     print(pri_str)
              
                     stri = ""
                 else:
                  if time.time()-timer >= 1:
                    sp = (coun - prevc)
                    prevc = coun
                    timer = time.time()
                  else:
                    pass
                  word = f"{i1}{i2}{i3}{i4}{i5}{i6}{i7}"
                  log(word)
                  file.write(word.__add__("\n"))
                  pri_str = f"word:{word} ".__add__(f"coun:{coun} | per:{round(per(digs,len(liste),word_no=coun),5)}% | time:{round(time.time()-timer1,1)} | size:{sys.getsizeof(stri)} | spd: {sp} WPS | est: {cal_est(tot=tott,count=coun,speed=sp)} secs")
                  stri = stri.__add__(f"{word}\n")
                  coun += 1
                  print(pri_str)
                  stri = ""
               else:
                if time.time() - timer >= 1:
                       sp = (coun - prevc)
                       prevc = coun
                       timer = time.time()
                else:
                       pass
                word = f"{i1}{i2}{i3}{i4}{i5}{i6}"
                log(word)
                file.write(word.__add__("\n"))
                pri_str = f"word:{word} ".__add__(f"coun:{coun} | per:{round(per(digs,len(liste),word_no=coun),5)}% | time:{round(time.time()-timer1,1)} | size:{sys.getsizeof(stri)} | spd: {sp} WPS | est: {cal_est(tot=tott,count=coun,speed=sp)} secs")
                stri = stri.__add__(f"{word}\n")
                coun += 1
                print(pri_str)
        
                stri = ""
             else:
              if time.time()-timer >= 1:
                sp = (coun - prevc)
                prevc = coun
                timer = time.time()
              else:
                pass
              word = f"{i1}{i2}{i3}{i4}{i5}"
              log(word)
              file.write(word.__add__("\n"))
              pri_str = f"word:{word} ".__add__(f"coun:{coun} | per:{round(per(digs,len(liste),word_no=coun),5)}% | time:{round(time.time()-timer1,1)} | size:{sys.getsizeof(stri)} | spd: {sp} WPS | est: {cal_est(tot=tott,count=coun,speed=sp)} secs")
              stri = stri.__add__(f"{word}\n")
              coun += 1
              print(pri_str)
      
              stri = ""
           else:
            if time.time()-timer >= 1:
                sp = (coun - prevc)
                prevc = coun
                timer = time.time()
            else:
                pass
            word = f"{i1}{i2}{i3}{i4}"
            log(word)
            file.write(word.__add__("\n"))
            pri_str = f"word:{word} ".__add__(f"coun:{coun} | per:{round(per(digs,len(liste),word_no=coun),5)}% | time:{round(time.time()-timer1,1)} | size:{sys.getsizeof(stri)} | spd: {sp} WPS | est: {cal_est(tot=tott,count=coun,speed=sp)} secs")
            stri = stri.__add__(f"{word}\n")
            coun += 1
            print(pri_str)
    
            stri = ""
         else:
          if time.time()-timer >= 1:
                sp = (coun - prevc)
                prevc = coun
                timer = time.time()
          else:
                pass
          word = f"{i1}{i2}{i3}"
          log(word)
          file.write(word.__add__("\n"))
          pri_str = f"word:{word} ".__add__(f"coun:{coun} | per:{round(per(digs,len(liste),word_no=coun),5)}% | time:{round(time.time()-timer1,1)} | size:{sys.getsizeof(stri)} | spd: {sp} WPS | est: {cal_est(tot=tott,count=coun,speed=sp)} secs")
          stri = stri.__add__(f"{word}\n")
          coun += 1
          print(pri_str)
          stri = ""
       else:
        if time.time()-timer >= 1:
                sp = (coun - prevc)
                prevc = coun
                timer = time.time()
        else:
                pass
        word = f"{i1}{i2}"
        log(word)
        file.write(word.__add__("\n"))
        pri_str = f"word:{word} ".__add__(f"coun:{coun} | per:{round(per(digs,len(liste),word_no=coun),5)}% | time:{round(time.time()-timer1,1)} | size:{sys.getsizeof(stri)} | spd: {sp} WPS | est: {cal_est(tot=tott,count=coun,speed=sp)} secs")
        stri = stri.__add__(f"{word}\n")
        coun += 1
        print(pri_str)
        stri = ""
     else:
      if time.time()-timer >= 1:
                sp = (coun - prevc)
                prevc = coun
                timer = time.time()
      else:
                pass
      word = f"{i1}"
      log(word)
      file.write(word.__add__("\n"))
      pri_str = f"word:{word} ".__add__(f"coun:{coun} | per:{round(per(digs,len(liste),word_no=coun),5)}% | time:{round(time.time()-timer1,1)} | size:{sys.getsizeof(stri)} | spd: {sp} WPS | est: {cal_est(tot=tott,count=coun,speed=sp)} secs")
      stri = stri.__add__(f"{word}\n")
      coun += 1
      print(pri_str)
      stri = ""

# Main

bruteforce(liste,8)