import rclpy
from rclpy.node import Node
from std_msgs.msg import String

#TODO da implementare

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher')
        self.publisher_ = self.create_publisher(String, 'obj_topic', 10)
        #self.published = False
        timer_period = 15
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        if (self.i % 2) == 0:
            msg = String()
            msg.data = 'destra'
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
            self.i += 1
           #self.published = True 
        else:
            msg = String()
            msg.data = 'sinistra'
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
            self.i += 1

def main(args=None):
    rclpy.init(args=args)
    publisher_node = PublisherNode()
    rclpy.spin(publisher_node)    
    publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()