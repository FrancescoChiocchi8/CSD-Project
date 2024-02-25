import rclpy
from rclpy.node import Node
from std_msgs.msg import String

'''
This node forwards the message received from the robot communication node to the servo_handler node.
'''
class ArmHandler(Node):

    def __init__(self):
        super().__init__('arm_handler')
        self.subscription = self.create_subscription(String, 'armComm_topic', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(String, 'servo_topic', 10)
        self.mess = None

    def listener_callback(self, msg):
        self.mess = msg
        self.get_logger().info('Received message: "%s"' % msg.data)
        self.read_mess(self.mess)

    '''
    This method examines the received content and forwards it to the "servo_topic", sending "left" if it has read "left"
    and "right" if it has read "right".
    '''
    def read_mess(self, mess):
         if mess is not None:
            msg_to_publish = String()
            if self.mess.data == 'left':
                msg_to_publish.data = 'left'
                self.publisher_.publish(msg_to_publish)
                self.get_logger().info('going left...')

            elif self.mess.data == 'right':
                msg_to_publish.data = 'right'
                self.publisher_.publish(msg_to_publish)
                self.get_logger().info('going right...')
            
            else: 
                self.get_logger().info('Invalid message')


def main(args=None):
    rclpy.init(args=args)
    minimal_node = ArmHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()