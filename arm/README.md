This package is designed for managing the RaspArm robot, which you can find at this [link](https://www.adeept.com/rasp-arm-s_p0250.html).
The task of this robot is to move a load from its designated base station upon receiving a message from the PicarPro robot indicating that the load is ready to be picked up and placed in a box.

Depending on the color of the load recognized by the PicarPro robot (either red or blue), it picks up the load from the station. If the load is red, it places it in a box to the left of the robot; if it's blue, it places the load in a box to the right of the robot.