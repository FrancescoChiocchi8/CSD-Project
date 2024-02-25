import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import picar_pro.ObjectAnalysis as OA

class AnalysisHandler(Node):
    def __init__(self):
        super().__init__('analysis_handler')
        OA.setup()
        self.publisher_ = self.create_publisher(String, 'obj_topic', 10)
        timer_period = 3
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        if(OA.checkdist()<0.5):
            msg.data = "YES"
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
        else:
            msg.data = "NO"
            self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    publisher_node = AnalysisHandler()
    rclpy.spin(publisher_node)    
    publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()