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
        self.publisher = self.create_publisher(String, 'armComm_topic', 10)
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
        if self.mess is not None:
            if self.mess.data == 'GRAB':
                self.pick_up_load()
                self.mess.data = "GRABBED"
                self.publisher.publish(self.mess)
                self.get_logger().warning('Forwarded grabbed')
            elif self.mess.data == 'RELEASE':
                self.release_cargo()
            elif self.mess.data == 'INCOMING':
                SC.initPos()
            else:
                self.get_logger().warning('Invalid message')

    '''
    This method is for picking up the load from the station.
    '''
    def pick_up_load(self):
        SC.moveServo(15, 180, 5)
        SC.releaseAllServos()

    '''
    This method is for release cargo.
    '''
    def release_cargo(self):
        SC.moveServo(12, 160, 4)
        SC.moveServo(15, 0, 3)
        SC.releaseAllServos()


def main(args=None):
    rclpy.init(args=args)
    minimal_node = ServoHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()