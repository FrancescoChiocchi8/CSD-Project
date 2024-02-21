import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#TODO da implementare

class CameraHandler(Node):
    def __init__(self):
        super().__init__('camera_handler')
        self.publisher_ = self.create_publisher(String, 'obj_topic', 10)
        #self.published = False
        timer_period = 15
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()

def main(args=None):
    rclpy.init(args=args)
    publisher_node = CameraHandler()
    rclpy.spin(publisher_node)    
    publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()