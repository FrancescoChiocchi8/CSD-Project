import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommHandler(Node):
    def __init__(self):
        super().__init__('comm_handler')
        self.subscription = self.create_subscription(String, 'picarComm_topic', self.listener_callback, 10)
        self.publisher = self.create_publisher(String, '/comm_topic', 10)
        self.mess = None

    def listener_callback(self, msg):
        self.mess = msg
        self.get_logger().info('Received message: "%s"' % msg.data)
        self.forward_message()

    def forward_message(self):
        if self.mess is not None:
            self.publisher.publish(self.mess)
            self.get_logger().info('Forwarded comm message: "%s"' % self.mess.data)

def main(args=None):
    rclpy.init(args=args)
    minimal_node = CommHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()