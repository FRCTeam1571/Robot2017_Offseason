import os #imports os module

os.system("cls")
os.system("color F0")
#Unnecessary ASCII Art
print("   _____          _      _____ ____  _____         _______ ______      ")
print("  / ____|   /\   | |    |_   _|  _ \|  __ \     /\|__   __|  ____|     ")
print(" | |       /  \  | |      | | | |_) | |__) |   /  \  | |  | |__        ")
print(" | |      / /\ \ | |      | | |  _ <|  _  /   / /\ \ | |  |  __|       ")
print(" | |____ / ____ \| |____ _| |_| |_) | | \ \  / ____ \| |  | |____      ")
print("  \_____/_/    \_\______|_____|____/|_|__\_\/_/____\_\_|_ |______|____ ")
print("                 |  __ \ / __ \|  _ \ / __ \__   __|_   _/ ____|/ ____|")
print("                 | |__) | |  | | |_) | |  | | | |    | || |    | (___  ")
print("                 |  _  /| |  | |  _ <| |  | | | |    | || |     \___ \ ")
print("                 | | \ \| |__| | |_) | |__| | | |   _| || |____ ____) |")
print("                 |_|  \_\\\____/|____/ \____/  |_|  |_____\_____|_____/ ")
print("Welcome to the CALibrate Robotics Robot UI")
print("Setup")
print("------------------------------------------------------------------")


fp = input("File Path: ")
fn = input("File Name: ")

ext = ".py" #Checks to see if file has a .py extention
if ext not in fn:
    ta = input("Is this file a Python file (.py)? [Y/N]")
    if ta == "Y" or ta == "y":
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
        if stq == "Y" or stq == "y":
            st = "--skip-tests"
        else:
            st = ""
        head("Updated Skip Test Setting")
        return

    def netcode():
        ncq = input("Use Netcode (feedback)? Default: On [Y/N]") #Netcode Question
        if ncq == "Y" or ncq == "y":
            nc = "--nc"
        else:
            nc = ""
        head("Updated Netcode Setting")
        return

    def delete():
        depq = input("Delete Config? [Y/N]") #Config Question
        if depq == "Y" or depq == "y":
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
        if goto == "A" or goto == "a":
            netcode()
            go()

        elif goto == "B" or goto == "b":
            test()
            go()

        elif goto == "C" or goto == "c":
            delete()
            go()
        elif goto == "D" or goto == "d":
            deploy()
        else:
            head("")
            go()

    head("No Updates")
    print("A. Start")
    print("B. Settings")
    opt = input("Type Letter: ")
    if opt == "A" or opt == "a":
        return
    elif opt == "B" or opt == "b":
        os.system("cls")
        head("No Updates")
        go()
    else:
        deploy()
    return


nc = ""
st = ""
if rn == "deploy":
    nc = "--nc"
    deploy()

pyq = input("Do you have pyfrc and pygame installed? [Y/N]")
if pyq == "N" or pyq == "n":
    print("Downloading pyfrc and pygame...")
    os.system("py -3 -m pip install pyfrc") #downloads pyfrc
    os.system("py -3 -m pip install pygame") #downloads pygame

os.chdir(fp) #Changes to directory

while True:
    os.system("cls")
    print("CALibrate Robotics Robot UI "+fp+"\\"+fn)
    print("Setup Complete")
    print("")
    print("------------------------------------------------------------------")
    print("")

    ans = input("Start the Robot? [Y/N]")
    if ans == "Y" or ans == "y":
        print("Starting...")
        '''Types this in cmd line'''
        os.system("py -3 "+fn+" "+rn+" "+nc+" "+st)
        input("Press Enter to Resume")
    elif ans == "N" or ans =="n":
        qu = input("Do you want to quit? [Y/N]")
        if qu == "Y" or qu == "y":
            exit() #exits the program
#Wow you made it to the end.
#Todo: Make a menu for the simulator
#Made by Trevor- Team 1571
