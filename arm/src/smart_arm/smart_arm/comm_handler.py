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
        self.armComm_subscription = self.create_subscription(String, 'armComm_topic', self.armComm_callback, 10)
        self.comm_publisher = self.create_publisher(String, '/comm_topic', 10)

        self.commMsg = None
        self.servoMsg = None

    '''
    This method is for reading the message sent by the machine robot. If the object identified by the machine's camera is red, 
    it forwards a message to the arm_handler node instructing it to pick up the object from the station and place it on the left; 
    if it's blue, instead, it forwards a message to the arm_handler node instructing it to pick up the object from the station 
    and place it to the right of the robot. Other colors have not been considered, but the code is easily extendable 
    to consider additional cases.
    '''
    def armComm_callback(self, msg):
        self.commMsg = msg
        self.get_logger().info('Received arm_comm message: "%s"' % msg.data)

        self.comm_publisher.publish(self.commMsg)
        self.get_logger().info('Forwarded ext_comm message: "%s"' % self.commMsg.data)            

def main(args=None):
    rclpy.init(args=args)
    minimal_node = CommHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()