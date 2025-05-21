import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TerminalNode(Node):
    def __init__(self):
        super().__init__('terminal_node')
        self.display_sub = self.create_subscription(String, 'display', self.display_callback, 10)

        self.get_logger().info("Aguardando pelo serviço 'calculate'...")
        self.cli = self.create_client(CalcService, 'calculate')
        
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Serviço "calculate" ainda não disponível, aguardando...')

    def display_callback(self, msg):
        self.get_logger().info(f"Resultado da operação recebido: {msg.data}")

    def request_calculation(self, operation, operand1, operand2):
        if operation not in ['+', '-', '*', '/']:
            self.get_logger().warn(f"Operação '{operation}' inválida! Use '+', '-', '*' ou '/'.")
            return
        
        req = CalcService.Request()
        req.operand1 = operand1
        req.operand2 = operand2
        req.operation = operation

        self.get_logger().info(f"Solicitando cálculo: {operand1} {operation} {operand2}")
        future = self.cli.call_async(req)
        future.add_done_callback(self.handle_response)

    def handle_response(self, future):
        try:
            response = future.result()
            self.get_logger().info(f"Resultado do serviço: {response.result}")
            self.get_logger().info(f"Status: {response.status}")
        except Exception as e:
            self.get_logger().error(f"Erro ao chamar o serviço de cálculo: {e}")

    def get_input_from_terminal(self):
        while rclpy.ok():
            try:
                operation = input("Digite a operação (+, -, *, /) ou 'q' para sair: ")
                if operation == 'q':
                    self.get_logger().info("Encerrando o programa.")
                    break

                operand1 = float(input("Digite o primeiro operando: "))
                operand2 = float(input("Digite o segundo operando: "))
                self.request_calculation(operation, operand1, operand2)
            except ValueError:
                self.get_logger().warn("Entrada inválida! Certifique-se de digitar números válidos.")
            except Exception as e:
                self.get_logger().error(f"Erro inesperado: {e}")

def main(args=None):
    rclpy.init(args=args)
    terminal_node = TerminalNode()
    terminal_node.get_input_from_terminal()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
