import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import smart_arm.ServoController as SC

'''
This is an actuator node. It listens on the "servo_topic" and is responsible for picking up the load from the base station
and placing it to the left (if the load is red) or to the right (if the load is blue).
'''
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
    This method is responsible for executing operations. If the received message is 'left', it executes operations for
    depositing cargo to the left; if the message is 'right', it executes operations for moving to the right.
    
    Possible params for servos:
    motorA: 0 (right) - 160 (left)
    motorB: 100 (min) - 180 (max)
    motorC: 0 (min) - 180 (max)
    motorD: 0 (min) - 120 (max)
    '''
    def execute_operations(self):
        SC.initPos()
        self.get_logger().info('set initial position...')
        if self.mess is not None:
            if self.mess.data == 'left':
                self.get_logger().info('going left...')
                self.pick_up_load()
                self.left_instructions()
            elif self.mess.data == 'right':
                self.get_logger().info('going right...')
                self.pick_up_load()
                self.right_instructions()
            else:
                self.get_logger().warning('Invalid message')

        SC.releaseAllServos()

    '''
    This method is for picking up the load from the station.
    '''
    def pick_up_load(self):
        self.get_logger().info('set to pick up load...')
        SC.moveServo(14, 110)
        #SC.moveServo(14, 140)
        #SC.moveServo(15, 130)
        #SC.moveServo(14, 90)
        SC.moveServo(15, 150)
        
        self.get_logger().info('pick up load complete')

    '''
    This method is for red cargo.
    '''
    def left_instructions(self):
        #servo_controller_main(13, 180)
        SC.moveServo(14, 140)
        SC.moveServo(12, 160)
        SC.moveServo(13, 95)
        SC.moveServo(14, 125)
        SC.moveServo(15, 0)

    '''
    This method is for blue cargo.
    '''
    def right_instructions(self):
        SC.moveServo(14, 140)
        SC.moveServo(12, 0)
        SC.moveServo(13, 95)
        SC.moveServo(14, 125)
        SC.moveServo(15, 0)


def main(args=None):
    rclpy.init(args=args)
    minimal_node = ServoHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()