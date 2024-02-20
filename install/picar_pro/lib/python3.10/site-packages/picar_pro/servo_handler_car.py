import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ServoHandlerCar(Node):

    def __init__(self):
        super().__init__('servo_handler_car')
        self.subscription = self.create_subscription(String, 'obj_topic', self.listener_callback, 10)
        self.publisher_wheels = self.create_publisher(String, 'wheels_topic', 10)
        self.publisher_comm = self.create_publisher(String, 'car_msg_topic', 10)
        self.publisher_claw = self.create_publisher(String, 'claw_topic', 10)
        self.mess = None

    def listener_callback(self, msg):
        self.mess = msg
        self.get_logger().info('Received message: "%s"' % msg.data)
        self.forward_message()

    def forward_message(self):
        if self.mess is not None:
            self.publisher_wheels.publish(self.mess)
            self.publisher_comm.publish(self.mess)
            self.publisher_claw.publish(self.mess)
            self.get_logger().info('Forwarded message: "%s"' % self.mess.data)


def main(args=None):
    rclpy.init(args=args)
    minimal_node = ServoHandlerCar()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()