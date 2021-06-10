from controller import Robot
from controller import Motor
from controller import DistanceSensor


TIME_STEP=32


robot = Robot()


# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())




# Main loop:
while robot.step(timestep) != -1:
   
  
            
    pass
