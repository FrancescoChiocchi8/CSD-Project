import rclpy, time
from rclpy.node import Node
from std_msgs.msg import String
from adafruit_servokit import ServoKit
from WheelController import main as move

class WheelsHandler(Node):
    def __init__(self):
        super().__init__('wheels_handler')
        self.subscription = self.create_subscription(String, 'wheels_topic', self.listener_callback, 10)
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
                time.sleep(5)
                self.moving_servos(0, 0)
                self.moving_servos(1, 0)

            elif self.mess.data == 'sinistra':
                self.get_logger().info('Andando verso sinistra...')
                self.initial_position()
                time.sleep(5)
                self.moving_servos(0, 180)
                self.moving_servos(1, 180) 

            else:
                self.get_logger().warning('Messaggio non valido: "%s"' % self.mess.data)

def parseMovement():
    #parse con separatore del messaggio inviato da servo handler
    move(speed, direction, turn, duration)

def main(args=None):
    rclpy.init(args=args)
    minimal_node = WheelsHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()