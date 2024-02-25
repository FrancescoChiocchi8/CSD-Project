import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommHandler(Node):
    def __init__(self):
        super().__init__('comm_handler')
        self.picarComm_subscription = self.create_subscription(String, 'picarComm_topic', self.picarComm_callback, 10)
        self.comm_publisher = self.create_publisher(String, '/comm_topic', 10)

        self.commMsg = None
    
    def picarComm_callback(self, msg):
        self.commMsg = msg
        self.get_logger().info('Received picar_comm message: "%s"' % msg.data)

        self.comm_publisher.publish(self.commMsg)
        self.get_logger().info('Forwarded picar -> arm message: "%s"' % self.commMsg.data)

def main(args=None):
    rclpy.init(args=args)
    minimal_node = CommHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()