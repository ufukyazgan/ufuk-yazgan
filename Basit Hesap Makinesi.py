

def Addittion(num1,num2):
  return num1+num2
  
def Substraktion(num1,num2):
 return num1-num2
 
def Multiplikation(num1,num2):
 return num1*num2
 
def Division (num1,num2):
  return num1/num2

while True:
    opChoice=input("Was ist ihre Auswahl?\n[1]Addittion\n[2]Subsraktion\n[3]Multiplikation\n[4]Division\nAuswahl:")
    match opChoice:
        case "1":
            num1=int(input("Erste Zahl?"))
            num2=int(input("Zweite Zahl?"))
            print(f"{num1}+{num2}={Addittion(num1,num2)}")
            break
        case "2":
            num1=int(input("Erste Zahl?"))
            num2=int(input("Zweite Zahl?"))
            print(f"{num1}-{num2}={Substraktion(num1,num2)}")
            break
        case "3":
            num1=int(input("Erste Zahl?"))
            num2=int(input("Zweite Zahl?"))
            print(f"{num1}*{num2}={Multiplikation(num1,num2)}")
            break
        case "4":
            num1=int(input("Erste Zahl?"))
            num2=int(input("Zweite Zahl?"))
            print(f"{num1}/{num2}={Division(num1,num2)}")
            break
 