import rclpy, time
from rclpy.node import Node
from std_msgs.msg import String
import picar_pro.WheelController as WC

class WheelsHandler(Node):
    def __init__(self):
        super().__init__('wheels_handler')
        self.subscription = self.create_subscription(String, 'wheels_topic', self.listener_callback, 10)
        self.mess = None
        WC.setup()

    def listener_callback(self, msg):
        self.mess = msg
        self.get_logger().info('Received picar -> wheels message: "%s"' % msg.data)

        if msg.data == "YES":
            WC.move(100, "backward", "no", 0.5)
            WC.move(100, "forward", "right", 0.5)
            WC.move(100, "forward", "left", 0.5)
            WC.move(100, "forward", "left", 0.67)
            WC.move(100, "forward", "right", 0.45)
        elif(msg.data == "REVERSE"):
            WC.move(100, "backward", "no", 1)
        else:
            movementParams = msg.data.split("/")
            WC.move(int(movementParams[0]), movementParams[1], movementParams[2], float(movementParams[3]))
         
def main(args=None):
    rclpy.init(args=args)
    minimal_node = WheelsHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()