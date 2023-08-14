# diffdrive_slambot
The code is adapted from https://github.com/joshnewans/diffdrive_arduino

Demonstrates ros2_control using a hardware interface and gives commands to real robot as opposed to gazebo (without actually connecting to the real robot). Visualize in Rviz. 

To run:

ros2 launch diffdrive_slambot diffbot.launch.py 

ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=diffbot_base_controller/cmd_vel_unstamped





It is based on the diffbot example from [ros2_control demos](https://github.com/ros-controls/ros2_control_demos/tree/master/example_2).

For a tutorial on how to develop a hardware interface like this, check out the video below:

https://youtu.be/J02jEKawE5U



