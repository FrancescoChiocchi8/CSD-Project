import rclpy
from rclpy.node import Node
from std_msgs.msg import String

'''
This node forwards the message received from the robot communication node to the servo_handler node.
'''
class ArmHandler(Node):

    def __init__(self):
        super().__init__('arm_handler')
        self.comm_subscription = self.create_subscription(String, '/comm_topic', self.comm_callback, 10)
        self.servo_publisher = self.create_publisher(String, 'servo_topic', 10)
        self.comm_publisher = self.create_publisher(String, 'armComm_topic', 10)

        self.commMsg = String()
        self.servoMsg = String()

    '''
    This method examines the received content and forwards it to the "servo_topic", sending "left" if it has read "left"
    and "right" if it has read "right".
    '''
    def comm_callback(self, msg):
        self.commMsg = msg
        self.get_logger().info('Received comm message: "%s"' % msg.data)

        self.servo_publisher.publish(self.commMsg)
            
    def servo_callback(self, msg):
        self.servoMsg = msg
        self.get_logger().info('Received servo message: "%s"' % msg.data)

        self.comm_publisher.publish(self.servoMsg)

def main(args=None):
    rclpy.init(args=args)
    minimal_node = ArmHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()