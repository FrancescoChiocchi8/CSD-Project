import rclpy, time
from rclpy.node import Node
from std_msgs.msg import String
from ServoController import main as moveServo

class ServoHandler(Node):
    def __init__(self):
        super().__init__('servo_handler')
        self.subscription = self.create_subscription(String, 'servo_topic', self.listener_callback, 10)
        self.mess = None

    def listener_callback(self, msg):
        self.mess = msg
        self.get_logger().info('Received message: "%s"' % msg.data)
        self.execute_operations()

    def execute_operations(self):
        if self.mess is not None:
            if self.mess.data == 'destra':
                self.get_logger().info('Andando verso destra...')
                self.initial_position()
                moveServo(2, 90)
                time.sleep(5)
                moveServo(3, 45)
                moveServo(4, 90)

            elif self.mess.data == 'sinistra':
                self.get_logger().info('Andando verso sinistra...')
                self.initial_position()
                time.sleep(5)
                moveServo(2, 0)
                moveServo(3, 0) 
                moveServo(4, 0)

            else:
                self.get_logger().warning('Messaggio non valido: "%s"' % self.mess.data)

    def initial_position(self):
        moveServo(1, 0)
        moveServo(2, 0)
        moveServo(3, 0) 
        moveServo(4, 0)

def main(args=None):
    rclpy.init(args=args)
    minimal_node = ServoHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()