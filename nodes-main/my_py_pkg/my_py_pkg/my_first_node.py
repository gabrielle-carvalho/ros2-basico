#!/usr/bin/env python3
import rclpy #ros2 em python
from rclpy.node import Node

class MyNode(Node):
	def __init__(self):
		super().__init__("py_test")
		self._counter = 0
		self.get_logger().info("Hello ROS2 World!")
  
def main(args=None):
	rclpy.init(args=args) #inicializa o processo de comunicação com o ros2
	node = MyNode()
	rclpy.spin(node) #coloca o programa em espera
	rclpy.shutdown() #finaliza o processo de comunicaçãp=o com o ros2
	
if __name__ == "__main__":
	main()
	
#nó é dentro da main e tem que ser com nome diferente
