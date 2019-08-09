import random
import os
import datetime
orderdata ={}
def deloder():
	more='Y'
	itemdata={
		"1":0,
		"2":0,
		"3":0,
		"4":0,
		"5":0,
		"6":0,
		"7":0,
	}
	add=""
	f=open("MENU.TXT","r")
	f2=open("order.txt","w+")
	f2.write("ORDER TYPE:Delivery"+"\n")
	while(more=='Y' or more=='y'):
		print(f.read())
		try:
			item=input("Enter Choice Number: ")
			quantity=int(input("Enter Quantity in Numbers: ")) 
		except ValueError:
			print("Please Enter Numbers Only")
			more="Y"
		else:
			itemdata[item]=quantity
			more=input("To Order More Press 'Y', to exit press any other key:") 
	input("Press Enter to Generate Bill")
	print("--------------------------------------"+"\n")
	total=0
	for x,y in itemdata.items():
		if(y!=0):
			if(x=="1"):
				#f2.write("COLD COFFEE PLAIN\t\t"+str(y)+"\t$"+str(y*2.00)+"\n")
				print("COLD COFFEE PLAIN {0:10} ${1:10} \n".format(y,y*2.00),file=f2)
				total=total+y*2.00
			elif(x=="2"):
				f2.write("COLD COFFEE WITH ICE CREAM\t\t"+str(y)+"\t$"+str(y*2.50)+"\n")
				total=total+y*2.50
			elif(x=="3"):
				f2.write("LATTE\t\t"+str(y)+"\t$"+str(y*2.95)+"\n")
				total=total+y*2.95
			elif(x=="4"):
				f2.write("HAZELNUT\t\t"+str(y)+"\t$"+str(y*4.00)+"\n")
				total=total+y*4.00
			elif(x=="5"):
				f2.write("INTENCE CAFE\t\t"+str(y)+"\t$"+str(y*2.75)+"\n")
				total=total+y*2.75
			elif(x=="6"):
				f2.write("PASTA MAYO\t\t"+str(y)+"\t$"+str(y*3.40)+"\n")
				total=total+y*3.40
			elif(x=="7"):
				f2.write("PASTA\t\t"+str(y)+"\t$"+str(y*3.75)+"\n")
				total=total+y*3.75
	f2.write("--------------------------------------"+"\n")
	f2.write("SUBTOTAL: \t $"+str(total)+"\n")
	f2.write("TAX: \t $"+str(0.06*total)+"\n")
	f2.write("TOTAL: \t $"+str(total*1.06)+"\n")
	f2.seek(0,0)
	print(f2.read())
	input("PRESS ENTER TO PROCEED ")
	add=input("Enter your Address, Press enter to Submit: ")
	phone=input("Enter Phone Number:")
	print("ORDER CONFIRMED")
	orderId=random.randrange(1,999999,1)
	print("YOUR ORDER ID is: ",orderId)
	print("Please take a note of Order ID")
	f2.close()
	f2=open("order.TXT","a")
	f2.write("Address: "+add+"\n")
	f2.write("Phone: "+phone+"\n")
	f2.write("ORDER ID:"+str(orderId)+"\n")
	f2.write("Order Placed: "+str(datetime.datetime.now()))
	f.close()
	f2.close()
	newname=str(orderId)+".txt"
	os.rename("order.txt",newname)
def orderdet():
	id=input("Enter OrderId: ")
	id=id+str(".txt")
	if(os.path.exists(id)):
		f=open(id,"r")
		print(f.read())
	else:
		print("Wrong Order ID")
def takoder():
	more='Y'
	itemdata={
		"1":0,
		"2":0,
		"3":0,
		"4":0,
		"5":0,
		"6":0,
		"7":0,
	}
	add=""
	f=open("MENU.TXT","r")
	f2=open("order.txt","w+")
	f2.write("ORDER TYPE:Takeaway"+"\n")
	while(more=='Y'):
		print(f.read())
		item=input("Enter Choice Number: ")
		quantity=int(input("Enter Quantity in Numbers: "))
		itemdata[item]=quantity 
		more=input("Wanna order more? (Y/N): ")
	input("Press Enter to Generate Bill")
	print("--------------------------------------"+"\n")
	total=0
	for x,y in itemdata.items():
		if(y!=0):
			if(x=="1"):
				f2.write("COLD COFFEE PLAIN\t\t"+str(y)+"\t$"+str(y*2.00)+"\n")
				total=total+y*2.00
			elif(x=="2"):
				f2.write("COLD COFFEE WITH ICE CREAM\t\t"+str(y)+"\t$"+str(y*2.50)+"\n")
				total=total+y*2.50
			elif(x=="3"):
				f2.write("LATTE\t\t"+str(y)+"\t$"+str(y*2.95)+"\n")
				total=total+y*2.95
			elif(x=="4"):
				f2.write("HAZELNUT\t\t"+str(y)+"\t$"+str(y*4.00)+"\n")
				total=total+y*4.00
			elif(x=="5"):
				f2.write("INTENCE CAFE\t\t"+str(y)+"\t$"+str(y*2.75)+"\n")
				total=total+y*2.75
			elif(x=="6"):
				f2.write("PASTA MAYO\t\t"+str(y)+"\t$"+str(y*3.40)+"\n")
				total=total+y*3.40
			elif(x=="7"):
				f2.write("PASTA\t\t"+str(y)+"\t$"+str(y*3.75)+"\n")
				total=total+y*3.75
	f2.write("--------------------------------------"+"\n")
	f2.write("SUBTOTAL: \t $"+str(total)+"\n")
	f2.write("TAX: \t $"+str(0.06*total)+"\n")
	f2.write("TOTAL: \t $"+str(total*1.06)+"\n")
	f2.seek(0,0)
	print(f2.read())
	input("PRESS ENTER TO PROCEED ")
	phone=input("Enter Phone Number:")
	print("ORDER CONFIRMED")
	orderId=random.randrange(1,999999,1)
	print("YOUR ORDER ID is: ",orderId)
	print("Please take a note of Order ID and be at the Store in about half an hour")
	f2.close()
	f2=open("order.TXT","a")
	f2.write("Address: "+add+"\n")
	f2.write("Phone: "+phone+"\n")
	f2.write("ORDER ID:"+str(orderId)+"\n")
	f2.write("Order Placed: "+str(datetime.datetime.now()))
	f.close()
	f2.close()
	newname=str(orderId)+".txt"
	os.rename("order.txt",newname)
def menu():
	f=open("MENU.TXT","r")
	print(f.read())
def main():
	assume="8"
	while(assume=="8"):
		print("WELCOME TO KONDITOREI COFFEE \t \t \t VERSION- BETA 2")
		print("1. Order for Delivery ")
		print("2. Order for Take Away")
		print("3. Look at our Menu ")
		print("4. Check Order Details")
		try:
			i=int(input("Enter Choice: "))
			if(i==1):
				deloder()
			elif(i==2):
				takoder()
			elif(i==3):
				menu()
			elif(i==4):
				orderdet()
			else:
				raise Exception
		except ValueError:
			print("Please Enter Numbers only")
		except Exception:
			print("Invalid Input!! ")
		finally:
			assume=input("Press 8 to go to main menu any other key to exit : ")
main()
