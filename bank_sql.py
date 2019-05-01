import mysql.connector

class Validation():
   def checking(self,bal):   
      credits=mysql.connector.connect(host="localhost",user="root",passwd="root",database="bank")
      mycursor=credits.cursor()
      mycursor.execute("select * from login")
      data=mycursor.fetchall()
      for row in data:
          username=input("enter username:")
          password=input("enter password:")
          if username == row[0][0] and password == row[0][1]:
                         b.moneyWithdraw(bal)
                         b.deposit(bal)
          else:
                         print("invalid credentials")    


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

