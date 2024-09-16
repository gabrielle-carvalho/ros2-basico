import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class radioStationNode(Node):

#As Rádios AM transmitem as mensagens na frequência de 1 Hz.
#A Rádio Educadora transmite na frequência AM a mensagem “Transmitindo em AM: Olá Bahia” .
    def __init__(self):
        super().__init__("radiostationam")
        self.publisher =self.create_publisher(String, "EducadoraAM", 10)
        self._timer=self.create_timer(1.0,self.publish_message)
        self.get_logger().info("Transmitindo em AM: Olá Bahia")
        
    
#As Rádios FM transmitem as mensagens na frequência de 10 Hz
#A Rádio Educadora transmite na frequência FM a mensagem “Transmitindo em FM: Olá Bahia”            
    def publish_message(self):
        msg = String()
        msg.data = "Transmitindo em AM: Olá Bahia"
        self.publisher.publish(msg)
        
        
    # def __init__(self):
    #         super().__init__("radiostationFM")
    #         self.publisher =self.create_publisher(String, "EducadoraFM", 20)
    #         self._timer=self.create_timer(2.5,self.publish_message)
    #         self.get_logger().info("Transmitindo em FM: Olá Bahia")    

def main(args=None):
    rclpy.init(args=args)
    node =radioStationNode()
    rclpy.spin(node)
    rclpy.shutdown()


#As rádios do interior retransmitem as mensagens da Rádio Educadora
#acrescentando no início da mensagem a String “Retransmitindo – “