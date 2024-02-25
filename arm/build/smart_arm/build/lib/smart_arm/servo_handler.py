import rclpy
from rclpy.node import Node
from std_msgs.msg import String
#from ServoController import main as moveServo
from smart_arm.ServoController import main

class ServoHandler(Node):

    def __init__(self):
        super().__init__('servo_handler')
        self.subscription = self.create_subscription(String, 'servo_topic', self.listener_callback, 10)
        self.mess = None

    def listener_callback(self, msg):
        self.mess = msg
        self.get_logger().info('Received message: "%s"' % msg.data)
        self.execute_operations()

    '''
    motorA: 0 (right) - 160 (left)
    motorB: 100 (min) - 180 (max)
    motorC: 0 (min) - 180 (max)
    motorD: 0 (min) - 120 (max)
    '''
    def execute_operations(self):
        if self.mess is not None:
            if self.mess.data == 'left':
                self.get_logger().info('going left...')
                main(12, 160)


            elif self.mess.data == 'right':
                self.get_logger().info('going right...')
                main(12, 0)

            else:
                self.get_logger().warning('Invalid message')


    def initial_position(self):
        main(12, 60)
        main(13, 60)
        main(14, 50)
        main(15, 0)

def main(args=None):
    rclpy.init(args=args)
    minimal_node = ServoHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()