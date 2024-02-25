import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):

    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, '/comm_topic', 10)
        self.timer_ = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'blue'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.timer_.cancel()


def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = PublisherNode()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

