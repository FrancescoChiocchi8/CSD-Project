import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommHandler(Node):

    def __init__(self):
        super().__init__('comm_handler')
        self.subscription = self.create_subscription(String, 'comm_topic', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(String, 'armComm_topic', 10)
        self.mess = None

    def listener_callback(self, msg):
        self.mess = msg
        self.get_logger().info('Received message: "%s"' % msg.data)
        #self.forward_message()
        self.read_mess()

    def read_mess(self):
         if self.mess.data is not None:
            if self.mess.data == 'red':
                self.publisher_.publish('left')
                self.get_logger().info('going left...')

            elif self.mess.data == 'blue':
                self.publisher_.publish('right')
                self.get_logger().info('going right...')
            
            else: 
                self.get_logger().info('Invalid message')
                

def main(args=None):
    rclpy.init(args=args)
    minimal_node = CommHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()