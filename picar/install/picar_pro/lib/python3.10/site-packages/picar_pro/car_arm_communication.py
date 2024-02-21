import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CarArmCommunication(Node):

    def __init__(self):
        super().__init__('car_arm_communication')
        self.subscription = self.create_subscription(String, 'car_msg_topic', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(String, '/comm_topic', 10)
        self.mess = None

    def listener_callback(self, msg):
        self.mess = msg
        self.get_logger().info('Received message: "%s"' % msg.data)
        self.forward_message()

    def forward_message(self):
        if self.mess is not None:
            self.publisher_.publish(self.mess)
            self.get_logger().info('Forwarded message: "%s"' % self.mess.data)


def main(args=None):
    rclpy.init(args=args)
    minimal_node = CarArmCommunication()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
