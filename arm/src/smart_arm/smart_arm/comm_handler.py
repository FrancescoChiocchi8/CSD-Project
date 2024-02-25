import rclpy
from rclpy.node import Node
from std_msgs.msg import String

'''
This node is for communication between the Picar Pro robot and the robotic arm. It is activated when the Picar Pro 
communicates to the arm that there is a load at the arm's base station, so that it can be placed into a box.
'''
class CommHandler(Node):

    def __init__(self):
        super().__init__('comm_handler')
        self.subscription = self.create_subscription(String, '/comm_topic', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(String, 'armComm_topic', 10)
        self.mess = None

    def listener_callback(self, msg):
        self.mess = msg
        self.get_logger().info('Received message: "%s"' % msg.data)
        self.read_mess()

    '''
    This method is for reading the message sent by the machine robot. If the object identified by the machine's camera is red, 
    it forwards a message to the arm_handler node instructing it to pick up the object from the station and place it on the left; 
    if it's blue, instead, it forwards a message to the arm_handler node instructing it to pick up the object from the station 
    and place it to the right of the robot. Other colors have not been considered, but the code is easily extendable 
    to consider additional cases.
    '''
    def read_mess(self):
        if self.mess.data is not None:
            msg_to_publish = String()
            if self.mess.data == 'red':
                msg_to_publish.data = 'left'
                self.publisher_.publish(msg_to_publish)
                self.get_logger().info('going left...')

            elif self.mess.data == 'blue':
                msg_to_publish.data = 'right'
                self.publisher_.publish(msg_to_publish)
                self.get_logger().info('going right...')
            
            else: 
                self.get_logger().info('Invalid message')
                

def main(args=None):
    rclpy.init(args=args)
    minimal_node = CommHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()