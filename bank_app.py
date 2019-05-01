#Importing pandas
import pandas as pd

class Validation():
    username=input("enter username:")
    password=input("enter password:")
    def checking(self, bal):
        

        df=pd.read_csv('Auth.csv')
        for i  in df:
             if df.iloc[0, 0] == self.username and df.iloc[0, 1] == self.password:
                 
                 print("Your account balance is", bal)

             else:
                 print("invalid credentials")    


class Banking(Validation):

   def moneyWithdraw(self,bal):
         a=int(input("enter amout to withdraw:"))
         if a < bal:
           print("Request successful!!!!!!!")
           bal=bal-a
           print("Balance amount is:",bal)
      
         else:
          print("Insufficient funds")

   def deposit(self, bal):
         b=int(input("enter amount to deposit")) 
         if b > 0:
            bal = bal + b
            print("deposited amount is:", b)   
            print("total amont is:", bal)  
         else:
             print("Amount should be greater than 0")   



b=Banking()
b.checking(1000)
   
choice=True
while True:
    print("""
           1.Check your balance
           2.Withdrawl amount
           3.Deposit amount
           4.Exit 
           """)
    choice=input("Enter your option:")
    if choice=="1":
         b.checking(1000)
         break
    elif choice=="2":
         b.moneyWithdraw(1000)
        #  print("Withdrawl success")  
         break 
    elif choice=="3":
         b.deposit(1000)
         print("deposited successfully")   
         break  
    elif choice=="4":
        print("Exit")   
        break 
    else:
        print("Invalid option") 
        break   


