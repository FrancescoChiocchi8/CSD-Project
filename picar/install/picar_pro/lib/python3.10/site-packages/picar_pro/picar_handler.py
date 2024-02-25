import rclpy
from time import sleep
from pathlib import Path
from rclpy.node import Node
from std_msgs.msg import String

class PicarHandler(Node):
    def __init__(self):
        super().__init__('picar_handler')
        self.obj_subscription = self.create_subscription(String, 'obj_topic', self.obj_callback, 10)
        self.comm_subscription = self.create_subscription(String, '/comm_topic', self.comm_callback, 10)
        self.wheels_publisher = self.create_publisher(String, 'wheels_topic', 10)
        self.comm_publisher = self.create_publisher(String, 'picarComm_topic', 10)
        self.servo_publisher = self.create_publisher(String, 'servo_topic', 10)

        self.currentPath = open(r'/home/csd/CSD-Project/src/picar_pro/picar_pro/paths/percorso.txt',"r").readlines()
        self.actionIndex = 0

        self.commMsg = String()
        self.wheelsMsg = String()
        self.servoMsg = String()

    def obj_callback(self, msg):
        self.wheelsMsg = msg
        
        if(msg.data!="NO"):
            self.get_logger().info('Received obj -> picar_handler message: "%s"' % msg.data)
        
        if(self.actionIndex==0):
            self.servoMsg.data = "GRAB"
            self.commMsg.data = "INCOMING"
            self.forward_servo_msg()
            sleep(20)
            self.forward_comm_msg()
            
            self.servoMsg.data = ""
            self.commMsg.data = ""

        if (self.actionIndex>0 and msg.data == "YES" and self.actionIndex<len(self.currentPath)):
            self.forward_wheels_msg()
        else:
            if(self.actionIndex<len(self.currentPath)):
                self.wheelsMsg.data = self.currentPath[self.actionIndex]
                self.servoMsg.data = "LOWER"
                self.actionIndex=self.actionIndex+1
                self.forward_wheels_msg()
                self.forward_servo_msg()

        if(self.actionIndex==(len(self.currentPath) - 1)):
            self.commMsg.data = "GRAB"
            self.forward_comm_msg()
            self.actionIndex=self.actionIndex+1

    def comm_callback(self, msg):
        self.commMsg = msg

        if(msg.data == "GRABBED"):
            self.servoMsg.data = "RELEASE"
            self.wheelsMsg.data = "REVERSE"
            self.commMsg.data = "RELEASE"

            self.forward_servo_msg()
            self.forward_wheels_msg()
            self.forward_comm_msg()

    def forward_wheels_msg(self):
        if self.wheelsMsg is not None:
            self.wheels_publisher.publish(self.wheelsMsg)
            self.get_logger().info('Forwarded wheels message: "%s"' % self.wheelsMsg.data)

    def forward_servo_msg(self):
        if self.servoMsg is not None:
            self.servo_publisher.publish(self.servoMsg)
            self.get_logger().info('Forwarded servo message: "%s"' % self.servoMsg.data)

    def forward_comm_msg(self):
        if self.commMsg is not None:
            self.comm_publisher.publish(self.commMsg)
            self.get_logger().info('Forwarded comm message: "%s"' % self.commMsg.data)

def main(args=None):
    rclpy.init(args=args)
    minimal_node = PicarHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()