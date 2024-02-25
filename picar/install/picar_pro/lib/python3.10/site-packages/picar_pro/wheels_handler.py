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
        self.get_logger().info('Received message: "%s"' % msg.data)
        self.execute_operations()

    def execute_operations(self):
        if self.mess is not None:
            parseMovement(self)
        else:
            self.get_logger().warning('Messaggio non valido: "%s"' % self.mess.data)

def parseMovement(self):
    if self.mess is not None:
      if str(self.mess.data) == "YES":
        WC.move(100, "backward", "no", 0.5)
        WC.move(100, "forward", "right", 0.5)
        WC.move(100, "forward", "left", 0.5)
        WC.move(100, "forward", "left", 0.67)
        WC.move(100, "forward", "right", 0.45)
      else:
        movementParams = str(self.mess.data).split("/")
        WC.move(int(movementParams[0]), movementParams[1], movementParams[2], float(movementParams[3]))

def main(args=None):
    rclpy.init(args=args)
    minimal_node = WheelsHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()