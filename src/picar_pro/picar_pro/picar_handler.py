import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PicarHandler(Node):
    def __init__(self):
        super().__init__('picar_handler')
        self.subscription = self.create_subscription(String, 'obj_topic', self.listener_callback, 10)
        self.publisher_wheels = self.create_publisher(String, 'wheels_topic', 10)
        self.publisher_comm = self.create_publisher(String, 'comm_topic', 10)
        self.publisher_servo = self.create_publisher(String, 'servo_topic', 10)
        self.mess = None
        self.movement = None

    def listener_callback(self, msg):
        self.mess = msg
        self.get_logger().info('Received message: "%s"' % msg.data)

    def forward_picarWheels_msg(self):
        if self.mess is not None:
            self.publisher_wheels.publish(self.mess)
            self.get_logger().info('Forwarded wheel message: "%s"' % self.mess.data)

    def forward_picarArm_msg(self):
        if self.mess is not None:
            self.publisher_servo.publish(self.mess)
            self.get_logger().info('Forwarded servo message: "%s"' % self.mess.data)

    def forward_picarComm_msg(self):
        if self.mess is not None:
            self.publisher_comm.publish(self.mess)
            self.get_logger().info('Forwarded communication message: "%s"' % self.mess.data)

def pathInterpreter(self):
    currentPathFile = open("paths/percorso.txt","r")
    currentPath = currentPathFile.readLines()

    while(currentPath.hasNext()):
        self.movement = next(currentPath)

def main(args=None):
    rclpy.init(args=args)
    minimal_node = PicarHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()