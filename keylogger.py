import keyboard
import time
import msvcrt as m

wordlist = ""
def main(): 
    global wordlist
    str1 = m.getch().decode("utf-8")
  
    if str1 == "c":
        print("nice")
    else:
        if str1 == "\\r":
            wordlist += "\n" 
        else:
            wordlist = wordlist + (str(str1))
        f = open("keys.txt", "w+") 
        f.write(wordlist)
        f.close()
        print(str1)
        main()

main()
