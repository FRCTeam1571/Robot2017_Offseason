
#!/usr/bin/env python3

import wpilib
import ctre
from networktables import networktables


class MyRobot(wpilib.SampleRobot):
    '''Main robot class'''

    def robotInit(self):
        '''Robot-wide initialization code should go here'''

        self.lstick = wpilib.Joystick(0)
        self.rstick = wpilib.Joystick(1)

        self.fr_motor = ctre.CANTalon(2)
        self.rr_motor = ctre.CANTalon(3)
        self.fl_motor = ctre.CANTalon(0)
        self.rl_motor = ctre.CANTalon(1)

        self.climber = ctre.CANTalon(5)
        self.intake = ctre.CANTalon(7)
        self.shooter = ctre.CANTalon(8)
        self.feeder = ctre.CANTalon(6)



        self.rr_motor.changeControlMode(self.rr_motor.ControlMode.Follower)
        self.rr_motor.set(self.fr_motor.getDeviceID())
        self.rl_motor.changeControlMode(self.rl_motor.ControlMode.Follower)
        self.rl_motor.set(self.fl_motor.getDeviceID())


        self.robot_drive = wpilib.RobotDrive(self.fl_motor, self.fr_motor)


        # Position gets automatically updated as robot moves
        self.gyro = wpilib.AnalogGyro(1)

        Networktables.initialize(server='roborio-1571-frc.local')

        sd = Networktables.getTable('SmartDashboard')


    def disabled(self):
        '''Called when the robot is disabled'''
        while self.isDisabled():
            wpilib.Timer.delay(0.01)

    def autonomous(self):
        '''Called when autonomous mode is enabled'''

        timer = wpilib.Timer()
        timer.start()

        while self.isAutonomous() and self.isEnabled():

            if timer.get() < 2.0:
                self.robot_drive.arcadeDrive(-1.0, -.3)
            elif timer.get() > 2.0 and timer.get() < 5.0:
                self.robot_drive.arcadeDrive(-1.0, -1.0)
            elif timer.get() > 5.0 and timer.get() < 10.0:
                self.robot_drive.arcadeDrive(-1.0, 1.0)
            else:
                self.robot_drive.arcadeDrive(0, 0)

            wpilib.Timer.delay(0.01)

    def operatorControl(self):
        '''Called when operation control mode is enabled'''

        while self.isOperatorControl() and self.isEnabled():

            self.robot_drive.arcadeDrive(self.lstick)

            self.climbButtonResult = self.lstick.getRawButton(5)
            if self.climbButtonResult:
                self.climber.set(-0.25)
            else:
                self.climber.set(0)


            self.intakecw = self.lstick.getRawButton(6)
            self.intakecc = self.lstick.getRawButton(4)
            if self.intakecw:
                self.intake.set(-0.25)
            elif self.intakecc:
                self.intake.set(0.25)
            else:
                self.intake.set(0)

            self.rapid = self.lstick.getRawButton(1)
            self.single = self.lstick.getRawButton(2)
            if self.rapid:
                self.shooter.set(0.5)
                sd.putNumber('shooterValue', self.shooter.get())
                self.feeder.set(0.5)
            else:
                self.shooter.set(0)
                self.feeder.set(0)


            wpilib.Timer.delay(0.04)


if __name__ == '__main__':
    wpilib.run(MyRobot,
               physics_enabled=True)
