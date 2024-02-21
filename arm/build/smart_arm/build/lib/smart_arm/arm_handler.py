import rclpy
from rclpy.node import Node
from std_msgs.msg import String

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

    def read_mess(self, mess):
         if mess is not None:
            if self.mess.data == 'left':
                self.publisher_.publish('left')
                self.get_logger().info('going left...')

            elif self.mess.data == 'right':
                self.publisher_.publish('right')
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