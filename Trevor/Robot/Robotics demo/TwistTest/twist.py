import wpilib

class MyRobot(wpilib.SampleRobot):
    def robotInit(self):
        self.stick = wpilib.Joystick(0)
        twist = self.stick.Joystick.getTwist(0)

    def operatorControl(self):
        '''Called when operation control mode is enabled'''

        while self.isOperatorControl() and self.isEnabled():

            self.robot_drive.arcadeDrive(self.stick)

        wpilib.Timer.delay(0.04)

if __name__ == '__main__':
    wpilib.run(MyRobot)
