import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from adafruit_servokit import ServoKit
import time

class ClawMotorCar(Node):

    def __init__(self):
        super().__init__('claw_motor_car')
        self.subscription = self.create_subscription(String, 'wheels_topic', self.listener_callback, 10)
        self.mess = None
        self.kit = ServoKit(channels=16, frequency=50)

    def listener_callback(self, msg):
        self.mess = msg
        self.get_logger().info('Received message: "%s"' % msg.data)
        self.execute_operations()

    def execute_operations(self):
        if self.mess is not None:
            if self.mess.data == 'destra':
                self.get_logger().info('Andando verso destra...')
                self.initial_position()
                self.moving_servos(2, 90)
                time.sleep(5)
                self.moving_servos(3, 45)
                self.moving_servos(4, 90)

            elif self.mess.data == 'sinistra':
                self.get_logger().info('Andando verso sinistra...')
                self.initial_position()
                time.sleep(5)
                self.moving_servos(2, 0)
                self.moving_servos(3, 0) 
                self.moving_servos(4, 0)

            else:
                self.get_logger().warning('Messaggio non valido: "%s"' % self.mess.data)


    def moving_servos(self, pin, angle):
        self.kit.servo[pin].angle = angle

    def initial_position(self):
        self.moving_servos(2, 0)
        self.moving_servos(3, 0) 
        self.moving_servos(4, 0)


   

def main(args=None):
    rclpy.init(args=args)
    minimal_node = ClawMotorCar()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()