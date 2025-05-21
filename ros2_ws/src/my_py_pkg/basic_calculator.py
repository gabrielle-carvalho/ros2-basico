import rclpy
from rclpy.node import Node
from my_py_pkg.srv import CalcService
from std_msgs.msg import String

class BasicCalculator(Node):
    def __init__(self):
        super().__init__('basic_calculator_node')
        self.service = self.create_service(CalcService, 'calculate', self.handle_calculation)
        self.display_pub = self.create_publisher(String, 'display', 10)
        self.get_logger().info("Serviço 'calculate' disponível.")
        
    def handle_calculation(self, request, response):
        operation = request.operation
        operand1 = request.operand1
        operand2 = request.operand2
        result = None
        status = "Operação realizada com sucesso"

        if operation == '+':
            result = operand1 + operand2
        elif operation == '-':
            result = operand1 - operand2
        elif operation == '*':
            result = operand1 * operand2
        elif operation == '/':
            if operand2 != 0:
                result = operand1 / operand2
            else:
                result = float('nan')
                status = "Erro: divisão por zero"
        else:
            status = "Operação inválida"
        
        response.result = result
        response.status = status
        self.display_pub.publish(String(data=f"{operand1} {operation} {operand2} = {result}"))

        return response

def main(args=None):
    rclpy.init(args=args)
    basic_calculator = BasicCalculator()
    rclpy.spin(basic_calculator)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
