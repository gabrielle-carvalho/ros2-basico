import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RadioDoInteriorNode(Node):
    def __init__(self, name, input_topic, output_topic):
        super().__init__(name)
        
        self.publisher = self.create_publisher(String, output_topic, 10)
        self.subscription = self.create_subscription(
            String,
            input_topic,
            self.listener_callback,
            10
        )
        self.get_logger().info(f'Listening to {input_topic} and publishing to {output_topic}')

    def listener_callback(self, msg):
        retransmit_msg = String()
        retransmit_msg.data = f"Retransmitindo – {msg.data}"
        self.publisher.publish(retransmit_msg)

def main(args=None):
    rclpy.init(args=args)

    # Instanciando dois nós para representar rádios do interior (exemplo)
    radio1 = RadioDoInteriorNode("radio_do_interior_1", "educadora_fm", "radio_do_interior_fm")
    radio2 = RadioDoInteriorNode("radio_do_interior_2", "educadora_am", "radio_do_interior_am")

    rclpy.spin(radio1)
    rclpy.spin(radio2)
    rclpy.shutdown()
