import rclpy, time
from pathlib import Path
from rclpy.node import Node
from std_msgs.msg import String

class PicarHandler(Node):
    def __init__(self):
        super().__init__('picar_handler')
        self.subscription = self.create_subscription(String, 'obj_topic', self.listener_callback, 10)
        self.publisher_wheels = self.create_publisher(String, 'wheels_topic', 10)
        self.publisher_comm = self.create_publisher(String, 'picarComm_topic', 10)
        self.publisher_servo = self.create_publisher(String, 'servo_topic', 10)
        self.mess = None
        self.movement = String()
        self.currentPath = open(r'/home/csd/CSD-Project/src/picar_pro/picar_pro/paths/percorso.txt',"r").readlines()
        self.movementIndex = 0

    def listener_callback(self, msg):
        self.movement = msg
        self.get_logger().info('Received message: "%s"' % msg.data)
        if msg.data == "YES":
            self.forward_picarWheels_msg()
        else:
            if(self.movementIndex<len(self.currentPath)):
                self.movement.data = self.currentPath[self.movementIndex]
                self.movementIndex=self.movementIndex+1
                self.forward_picarWheels_msg()

    def forward_picarWheels_msg(self):
        if self.movement is not None:
            self.publisher_wheels.publish(self.movement)
            self.get_logger().info('Forwarded wheel message: "%s"' % self.movement.data)

    def forward_picarArm_msg(self):
        if self.mess is not None:
            self.publisher_servo.publish(self.mess)
            self.get_logger().info('Forwarded servo message: "%s"' % self.mess.data)

    def forward_picarComm_msg(self):
        if self.mess is not None:
            self.publisher_comm.publish(self.mess)
            self.get_logger().info('Forwarded communication message: "%s"' % self.mess.data)

def main(args=None):
    rclpy.init(args=args)
    minimal_node = PicarHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()