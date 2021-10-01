import csv
dat=open("school_data.csv","a",newline='')
writer=csv.writer(dat)
writer.writerow(['Name','Age','Number','Email'])
students_list=[]
num=int(input("Enter Number of the student whose Data you want to enter:"))
for i in range(1,num+1):
    name=input("Enter the Name of the Student {}: ".format(i))
    age=int(input("Enter the age of the student {}: ".format(name)))
    number=int(input("Enter the Phone number of the student {}: ".format(name)))
    email=input("Enter the Valid Email ID of the student {}: ".format(name))
    list1=[name,age,number,email]
    print("Data You Enterd is:\n Name {}\n Age {}\n Phone {}\n Email {}\n".format(list1[0],list1[1],list1[2],list1[3]))
    choice=input("Is the entered data is correct:(yes/no)")
    if choice=="yes":
        writer.writerow(list1)
        print("Data entered succesfullly!!!")
    else:
        sit=True
        while sit==True:
            choice2=input("What is wrong 1.Name, 2.Age, 3.Phone, 4.Email???")
            if choice2=="Name":
                new_name=input("Enter the correct new name:")
                list1[0]=new_name
                sit=False
            elif choice2=="Age":
                list1[1]=input("Enter the correct  Age:")
                sit=False
            elif choice2=="Phone":
                list1[2]=int(input("Enter the correct Phone Number:"))
                sit=False
            elif choice2=="Email":
                list1[3]=input("Enter the correct Email:")
                sit=False
            else:
                print("Try giving ccommand whats written in the question asked up there!!")
                sit=True
        writer.writerow(list1)
        print("Data entered succesfullly!!!")
dat.close()
