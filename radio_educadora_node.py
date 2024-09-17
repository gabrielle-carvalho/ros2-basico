import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RadioEducadoraNode(Node):
    def __init__(self):
        super().__init__("radio_educadora")

        # Publisher para FM
        self.fm_publisher = self.create_publisher(String, "educadora_fm", 10)
        self.create_timer(0.1, self.publish_fm_message)
        
        # Publisher para AM
        self.am_publisher = self.create_publisher(String, "educadora_am", 10)
        self.create_timer(0.25, self.publish_am_message)

    def publish_fm_message(self):
        msg = String()
        msg.data = "Transmitindo em FM: Olá Bahia"
        self.fm_publisher.publish(msg)

    def publish_am_message(self):
        msg = String()
        msg.data = "Transmitindo em AM: Olá Bahia"
        self.am_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RadioEducadoraNode()
    rclpy.spin(node)
    rclpy.shutdown()
