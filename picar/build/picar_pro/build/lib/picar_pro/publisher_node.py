import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PublisherNode(Node):

    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, '/obj_topic', 10)
        self.published = False

    def timer_callback(self):
        if not self.published:
            msg = String()
            msg.data = 'Questa è una pallina'
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
            self.published = True 


def main(args=None):
    rclpy.init(args=args)
    publisher_node = PublisherNode()
    publisher_node.timer_callback()
    publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()