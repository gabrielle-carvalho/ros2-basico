#!/usr/bin/env python3
import rclpy #ros2 em python
from rclpy.node import Node
from example_interfaces.msg import String

class RadioStationNode(Node):
    def __init__(self):
        super().__init__("radiostation")
        self._publisher = self.create_publisher(String, "FM1075", 10)
        self._timer=self.create_timer(0.5,self.publish_message)
        self.get_logger().info("A rádio FM 107.5 entrou no ar")


    def publish_message(self):     
        msg=String()
        msg.data="Olá da FM 107.5"
        self._publisher(msg)

  
def main(args=None):
	rclpy.init(args=args) #inicializa o processo de comunicação com o ros2
	node = RadioStationNode() #chama o construtor, nome da classe
	rclpy.spin(node) #coloca o programa em espera
	rclpy.shutdown() #finaliza o processo de comunicaçãp=o com o ros2
	
	
#nó é dentro da main e tem que ser com nome diferente
