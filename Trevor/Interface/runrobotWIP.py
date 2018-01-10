#!/usr/bin/env python3
# coding=utf-8

import os
import platform  # this is to detect the operating system for cross-platform compatibility

os.system('color f9')
class RAGE:
    """ this is to be ran when an error occurs due to an incomplete feature, a known bug, or just some random *insert
    loud bleep noise that hurts all of our ears and we all know what they say but its still
    here for some annoying reason. i mean, just let the man cuss dude*
    returns nothing. ABSOLUTELY NOTHING!
    """

    @staticmethod
    def rageQuit():
        """ this is to express rage when the program breaks. stops it in a RAGE """
        print("¬_¬   ┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻   ლ(ಠ益ಠლ)")
        quit()


class Statics:
    """ this is just a class full of static methods """

    @staticmethod
    def brk():
        """
        this is used to add the line break. its just to save writing code
        """
        print('')
        print('')
        print('')
        print('')


def target_file():
    """
    this attempts to find the file specified by the user.

    :returns: file path of robot file
    :rtype: str
    """
    print("please input file name [should be 'robot.py'. you may click enter for the default")
    file = input(":  ")

    if file is "":
        file = "robot.py"

    ext = ".py" #Checks for .py file extension
    if  ext not in file:
        file = fn+ext

    print("let program search for file path? [y/n]")
    fpq = input(": ")
    if fpq == "N" or fpq == "n":
        fpath = input("enter file path: ")
    else:
        fpath = os.path.join(os.path.dirname(__file__), file)

    print(fpath)
    Statics.brk()
    return fpath


def platCheck():
    """ allows for cross-platform support though the assignment of variables """
    global clear
    platname = platform.system()
    if platname == 'Linux':
        clear = 'clear'
        # Linux

    elif platname == 'Darwin':
        clear = 'clear'
        #This is experimental. None of us know how to use OSX or have it.
        # MAC OS X

    elif platname == 'Windows':
        clear = 'cls'
        # Windows

    else:
        print("What is your OS?")
        print("A. Linux")
        print("B. Mac OS/ OSX")
        print("C. Windows")
        osq = input(": ")
        if osq == "A" or osq == "a":
            clear = 'clear'
        if osq == "B" or osq == "b":
            clear = 'clear'
        if osq == "C" or osq == "c":
            clear = 'cls'
    return clear
clear = 'cls'
platCheck() #Called for testing
os.system(clear)

print("\n \n \n \n Welcome to the CALibrate Robotics Robot UI\n")
Statics.brk()

target_file()


""" THE LAND OF STUFF TO DO """
# TODO search for file name in super, child, and current dir [use current as primary]
# TODO set to save a config file. More options setting for program reset, self test, and others.
# TODO make separate menus for specific things in the UI
# TODO make it actually run the robot based off of the OS. have to figure out os.system() variable issue first.
# TODO make a way to find if the user has RobotPy and PyGame installed

"""
Made by:
    Trevor W. - Team 1571
    Ethan A. - Team 5183
"""
