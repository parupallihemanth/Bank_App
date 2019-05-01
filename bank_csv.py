import csv
import pandas
class Validation:
     def checking(self,bal):
         username=input("Enter username:")
         password=input("Enter password:")
         print("step1")
         df=pandas.read_csv('Auth.csv',)
         for i  in df:
             if df.iloc[0, 0] == username and df.iloc[0, 1] == password:
                 print("Your bank balance is:", bal)
                 b.moneyWithdraw(bal)
                 break
                 b.deposit(bal)

             else:
                   print('fail')






class Bank(Validation):

   def moneyWithdraw(self,bal):
         a=int(input("enter amout to withdraw"))
         if a < bal:
           print("Request successful!!!!!!!")
           bal=bal-a
           print("Balance amount is",bal)
      
         else:
          print("Insufficient funds")

   def deposit(self, bal):
         b=int(input("enter amount to deposit")) 
         if b > 0:
            bal = bal + b
            print("deposited amount is", b)   
            print("total amont is", bal)  
         else:
             print("Amount should be greater than 0")   

b = Bank()
b.checking(1000)
