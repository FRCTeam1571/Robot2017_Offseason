#!/usr/bin/env python3


import wpilib

class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
        self.stick = wpilib.Joystick(1)

        self.motor = wpilib.Jaguar(4)
        self.motor.set(1)

        l_motor = wpilib.Talon(0)
        r_motor = wpilib.Talon(1)
        self.robot_drive = wpilib.RobotDrive(l_motor, r_motor)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Check if we've completed 100 loops (approximately 2 seconds)
        if self.auto_loop_counter < 100:
            self.robot_drive.drive(-0.5, 0) # Drive forwards at half speed
            self.auto_loop_counter += 1
        else:
            self.robot_drive.drive(0, 0)    #Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.robot_drive.arcadeDrive(self.stick)

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()

if __name__ == "__main__":
    wpilib.run(MyRobot)




