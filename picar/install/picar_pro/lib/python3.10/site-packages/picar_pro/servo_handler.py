import rclpy, time
from rclpy.node import Node
from std_msgs.msg import String
import picar_pro.ServoController as SC

class ServoHandler(Node):
    def __init__(self):
        super().__init__('servo_handler')
        self.subscription = self.create_subscription(String, 'servo_topic', self.listener_callback, 10)
        self.mess = None

    def listener_callback(self, msg):
        self.mess = msg
        self.get_logger().info('Received picar -> servo message: "%s"' % msg.data)

        if(msg.data == "GRAB"):
            SC.moveServo(4, 100, 4) #apre la mano
            SC.moveServo(2, 0, 2) #si abbassa parallelo al terreno
            SC.moveServo(1, 0, 5) #gira verso destra alla piattaforma con il blocco e ci da tempo di piazzarlo
            SC.moveServo(4, 0, 4) #chiude la mano
            SC.moveServo(1, 115, 2) #gira il braccio avanti
            SC.moveServo(2, 150, 2) #alza il braccio
            SC.releaseAllServos()
        elif(msg.data == "LOWER"):
            SC.moveServo(2, 0, 2)
        elif(msg.data == "RELEASE"):
            SC.moveServo(4, 100, 4)
            SC.releaseAllServos()

def main(args=None):
    rclpy.init(args=args)
    minimal_node = ServoHandler()
    rclpy.spin(minimal_node)
    minimal_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()