# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:20:35 2020

@author: Oluwatomiwa
"""


import datetime
now = datetime.datetime.now()
#print ("current date and time: ")
print (now.strftime("Date: " + "%d-%m-%y"))
print (now.strftime("Time: " + "%H-%M-%S"))
print("  ")


print("welcome to Mr Adamu super market...")
moredetails={}
localdict = {}
mydetails = {}


#login section 
print("1. purchase goods, 2.Login as Admin, 3.cutomer service")
login=int(input("Choose what to do..."))
if login ==1:
    print ("Welcome")

#Display items we have in the stored    
print("Our Menu: Items, Price ")

my_items= ["Sugar, 50", "Bread (sliced)", 200, "Bread (unsliced)", 150, "Egg", 50, "Three crown(tin)" ,150, "Peak milk", 120, "peak milk (sachet)", 50 , "Bournvita(scahet) ",  50, "Milo (tin)", 500, "peak milk (large sachet) ", 700, "Milo (large sachet)", 700, "Bournvita (large sachet)", 100, "Custard(small sachet )",200, "corn flakes (small sachet)", 150, "Golden morn (small sachet )",100, "Detergent (small Wawu", 120, "Detergent (small Aerial)",200, "Detergent (big Aerial)", 250, "Detergent (big Wawu)",200, "Corn flakes (big sachet)", 750, "Golden morn (Large sachet)",650, "Sprite (small)", 80,"Pepsi (small)",80, "Fanta (small)",80, "Lacasera (small)",80,
    "Sprite (Big)",150, "Pepsi(big)",150, "Fanta (big)",150, "Lacasera (big)",150, "Coke (big)",150]
print (my_items, "  ")

#sugar="sugar", Bread1="Bread (sliced)", Bread2 ="Bread (unsliced)",Egg="Egg", tin_crown ="Three crown(tin)",peak_tin= "Peak milk", peak_sachet= "peak milk (sachet)", Bour_sachet="Bournvita(scahet) ", Milo_tin= "Milo (tin)", peak_large="peak milk (large sachet) ", 700, "Milo (large sachet)", 700, "Bournvita (large sachet)", 100, "Custard(small sachet )",200, "corn flakes (small sachet)", 150, "Golden morn (small sachet )",100, "Detergent (small Wawu)", 120, "Detergent (small Aerial)",200, "Detergent (big Aerial)", 250, "Detergent (big Wawu)",200, "Corn flakes (big sachet)", 750, "Golden morn (Large sachet)",650, "Sprite (small)", 80, pepsi(small)="Pepsi (small)",80, fanta(small)"Fanta (small)",80, lacasera="Lacasera (small)",
#    "Sprite (Big)",150, "Pepsi(big)",150, "Fanta (big)",150, "Lacasera (big)",150, coke (big)="Coke (big)"

list={"Sugar":50, "Bread (sliced)": 200, "Bread (unsliced)": 150, "Egg": 50, "Three crown(tin)":150, "Peak milk": 120, "peak milk (sachet)": 50 , "Bournvita(scahet) ": 50, "Milo (tin)": 500, "peak milk (large sachet) ": 700, "Milo (large sachet)": 700, "Bournvita (large sachet)": 100, "Custard(small sachet )":200, "corn flakes (small sachet)":150, "Golden morn (small sachet )":100, "Detergent (small Wawu": 120, "Detergent (small Aerial)":200, "Detergent (big Aerial)":250, "Detergent (big Wawu)":200, "Corn flakes (big sachet)": 750, "Golden morn (Large sachet)":650, "Sprite (small)": 80,"Pepsi (small)":80, "Fanta (small)":80, "Lacasera (small)":80,
    "Sprite (Big)":150, "Pepsi(big)":150, "Fanta (big)":150, "Lacasera (big)":150, "Coke (big)":150}


#Ask Items Costumer want to buy 
def askitem():
    select=str(input ("Enter the item(s) you want to buy : "))
    #for select in list :
     #if select == my_items:
    return select

#Ask items quantity
def askquantity():
    quantity=int(input("Enter the quantity you want : "))
    return quantity

#Get the Items from the staff
def getdetails ():
    #localdict = {}
    localdict['select'] = askitem()
    localdict['quantity'] = askquantity()
    return localdict



# get the limit of the buyers
def  limits ():
         
     return 

#Get more items from Customer
def getmoredetails():
    #again=int (input("Did you really want to buy more? "))
    #again=1
    #while again==4:
          for i in range (1):
              currentdetails=getdetails()
              moredetails[currentdetails['select']]=currentdetails
          return moredetails
    
    

def fetch(select,total_price, quantity):
    #receipt={}
    #mydetails = {}
    for i,j in zip(moredetails.keys(), moredetails.values()):
        if i == select:
            price=50
            print("detials found")
            print(moredetails[select])
            total=(askquantity ()*price)
            ("Total of what you purchased is ", "#",total)
            print("         ")
            print (now.strftime("Date: " + "%d-%m-%y"))
            print (now.strftime("Time: " + "%H-%M-%S"))
            print ("Thanks for your patronage: ")
            print ("Items purchased: ",  mydetails[select])
            print ("item(s) purchased = ", price)
            print("Total Blanace of what you purchased is ", "#",total, "  No Vat added")
            print ("This receipt does not require signature ")
        break
    else:
            #print("Details not found")
            pass
    return
          
#logiun 2 for the Admin to alter the database
if login==2:
       password="Admin"
       user = str(input("Enter password..."))
       if user == password:
        print ("welcome...")
        #opera = int (input("what operation you want to perform "))
        #if opera == 1:
           # add_items=str(input("Enter the goods"))
            #new_stock=list.append(add_items)
            #print ("new stock added successfully", new_stock)
else:
        print("Incorrect password ")
        
#login for the costomer to make comment(s)
if login==3:
      print ("welcome...")
      print("Please enter your Enquiry, we get back to you shortly...")
      print ("Many thanks")
     
else:
       pass
 
    
#Output 
mydetails = {}
mydetails = getmoredetails()
#receipt={}
#receipt = receiptgo ()
#print(mydetails.keys())
#print(mydetails.values())

fetch('sugar','total_price','askquantity')

