import os #imports os module

os.system("cls")
os.system("color F9")
#Unnecessary ASCII Art
print(r"   _____          _      _____ ____  _____         _______ ______      ")
print(r"  / ____|   /\   | |    |_   _|  _ \|  __ \     /\|__   __|  ____|     ")
print(r" | |       /  \  | |      | | | |_) | |__) |   /  \  | |  | |__        ")
print(r" | |      / /\ \ | |      | | |  _ <|  _  /   / /\ \ | |  |  __|       ")
print(r" | |____ / ____ \| |____ _| |_| |_) | | \ \  / ____ \| |  | |____      ")
print(r"  \_____/_/    \_\______|_____|____/|_|__\_\/_/____\_\_|_ |______|____ ")
print(r"                 |  __ \ / __ \|  _ \ / __ \__   __|_   _/ ____|/ ____|")
print(r"                 | |__) | |  | | |_) | |  | | | |    | || |    | (___  ")
print(r"                 |  _  /| |  | |  _ <| |  | | | |    | || |     \___ \ ")
print(r"                 | | \ \| |__| | |_) | |__| | | |   _| || |____ ____) |")
print(r"                 |_|  \_\\____/|____/ \____/  |_|  |_____\_____|_____/ ")
print("Welcome to the CALibrate Robotics Robot UI")
print("Best if run in Command Prompt")
print("------------------------------------------------------------------")


fp = input("File Path: ")
fn = input("File Name: ")

ext = ".py" #Checks to see if file has a .py extention
if fn == '':
    fn = 'robot.py'
elif ext not in fn:
    fn = fn+ext

def ri():
    print("Run In:")
    print("A. Simulator")
    print("B. Deploy")
    rq = input("Type Letter: ")
    if rq == "A" or rq == "a":
       rn = "sim"
    elif rq == "B" or rq == "b":
        rn = "deploy"
    else:
        ri()
    return rn

rn = ri()
#Deploy menu
def deploy():

    def head(up):
        os.system("cls")
        print("CALibrate Robotics Robot UI "+fp+"\\"+fn)
        print("Deploy Menu Settings")
        print(up)
        print("------------------------------------------------------------------")
        print("")

    def test():
        stq = input("Skip tests? Default: Off [Y/N]") #Skip Test Question
        if stq.lower() == "y":
            st = "--skip-tests"
        else:
            st = ""
        head("Updated Skip Test Setting")
        return

    def netcode():
        ncq = input("Use Netcode (feedback)? Default: On [Y/N]") #Netcode Question
        if ncq.lower() == "y":
            nc = "--nc"
        else:
            nc = ""
        head("Updated Netcode Setting")
        return

    def delete():
        depq = input("Delete Config? [Y/N]") #Config Question
        if depq.lower() == "y":
            print("Are you sure you want to delete previous settings?")
            print("If so type 'delete', If not press Enter")
            delprompt = input("")
            if delprompt == "delete":
                delyn = input("Are you REALLY sure? (Case Sensitive) [Yes/No]")
                if delyn == "Yes":
                    os.remove(fp+"\.deploy_cfg")
                    head("Deleted .deploy_cfg")
                else:
                    head("Cancelled Delete")
            else:
                head("Cancelled Delete")
        else:
            head("Cancelled Delete")
        return

    def go():
        print("A. Netcode setup")
        print("B. Skip Test setup")
        print("C. Delete Config File")
        print("D. Exit Settings")
        goto = input("Type Letter: ")
        if goto.lower() == 'a':
            netcode()
            go()

        elif goto.lower() == 'b':
            test()
            go()

        elif goto.lower() == 'c':
            delete()
            go()
        elif goto.lower() == 'd':
            deploy()
        else:
            head("")
            go()

    head("No Updates")
    print("A. Start")
    print("B. Settings")
    opt = input("Type Letter: ")
    if opt.lower() == 'a':
        return
    elif opt.lower() == 'b':
        os.system("cls")
        head("No Updates")
        go()
    else:
        deploy()
    return


nc = ""
st = ""
if rn == "deploy":
    deploy()

os.chdir(fp) #Changes to directory

while True:
    os.system("cls")
    print("CALibrate Robotics Robot UI "+fp+"\\"+fn)
    print("Setup Complete\n")
    print("------------------------------------------------------------------\n")

    ans = input("Start the Robot? [Y/N]")
    if ans.lower() == 'y' or ans == '':
        print("Starting...")
        '''Types this in cmd line'''
        os.system("py -3 "+fn+" "+rn+" "+nc+" "+st)
        input("Press Enter to Resume")
    else:
        qu = input("Do you want to quit? [Y/N]")
        if qu.lower() == "y":
            exit() #exits the program
#Made by Trevor- Team 1571
