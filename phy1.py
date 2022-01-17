import os

os.system("tput setaf 1")
print("t\t\thay welcome to TUI thats make life simple")
os.system("tput setaf 7")

print("\t\t\t--------------------------------------- )


print("""press 1: to see date
press2: to check cal
press3: conf web server
press4: to create user
press5: create file
""")

       print("Enter your choice : " , end="")
ch=input()

print(ch)

if int(ch) == 1:
        os.system("date")
elif int(ch) == 2:
        os.system("cal")
elif int(ch) == 3:
        os.system("yum install httpd")
elif int(ch) == 4:
        print("can u plz user name: " , end='')
        create user = input()
        os.system("useradd {}".format (create_user))
elif int(ch) == 5:
        os.system("date")
elif int(ch) == 1:
        os.system("date")
elif int(ch) == 1:
        os.system("date")
elif int(ch) == 1:
        os.system("date")



