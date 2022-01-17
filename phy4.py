import os

os.system("tput setaf 1")
print("t\t\thay welcome to TUI thats make life simple")
os.system("tput setaf 7")

print("\t\t\t---------------------------------------")

print("where you would like to perform your job (local/remote) :" , end='')
location = input()
print(location)

if location == "remote":
     remoteIP = input("Enter ur IP : ")

while true:
        print("""
        press 1: to see date
        press2: to check cal
        press3: conf web server
        press4: to create user
        press5: create file
         """)

        print("Enter your choice : " , end="")
        ch=input()
        print(ch)

        if location == "local":
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
            elif int(ch) == 6:
                os.system("date")
            elif int(ch) == 7:
                exit()
            else:
                print("option not supported")
            input("Enter to continue....")
                os.system("clear")

       
       elif location == "local":
            if int(ch) == 1:
                os.system("ssh {0} date".fotmate(remoteIP))
            elif int(ch) == 2:
                os.system("ssh {0} cal".fotmate(remoteIP))
            elif int(ch) == 3:
                os.system("yum install httpd")
            elif int(ch) == 4:
                print("can u plz user name: " , end='')
                create user = input()
                os.system("useradd {}".format (create_user))
            elif int(ch) == 5:
                os.system("date")
            elif int(ch) == 6:
                os.system("date"
                        )
            else:
                print("option not supported")

