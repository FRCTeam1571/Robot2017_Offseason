public class DriveSpeed extends Command {
	
	double speed, steering;
	boolean isFinished;

    public DriveSpeed(double speed, double steering) {
        requires(Robot.driveSystem);
        this.speed = speed;
        this.steering = steering;
    }

    protected void initialize() {
    	if(speed == 0) {
    		isFinished = true;
    	} else {
    		isFinished = false;
    	}
    }

    protected void execute() {
    	Robot.driveSystem.tankDrive(speed, steering);
    }

    protected boolean isFinished() {
        return false;
    }

    protected void end() {
    	Robot.driveSystem.tankDrive(0, 0);
    }

    protected void interrupted() {
    }
def tank_drive(
def drive(speed):
    
