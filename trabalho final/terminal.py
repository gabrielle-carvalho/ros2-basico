import rospy
from std_msgs.msg import String
from basic_calculator_package.srv import CalcService, CalcServiceRequest

class TerminalNode:
    def __init__(self):
        rospy.init_node('terminal_node', anonymous=True)
        self.display_sub = rospy.Subscriber('display', String, self.display_callback)

        rospy.loginfo("Aguardando pelo serviço 'calculate'...")
        rospy.wait_for_service('calculate')
        self.calculate_service = rospy.ServiceProxy('calculate', CalcService)
        rospy.loginfo("Serviço 'calculate' disponível!")

    def display_callback(self, msg):
        rospy.loginfo(f"Resultado da operação recebido: {msg.data}")

    def request_calculation(self, operation, operand1, operand2):
        if operation not in ['+', '-', '*', '/']:
            rospy.logwarn(f"Operação '{operation}' inválida! Use '+', '-', '*' ou '/'.")
            return
        try:
            calc_request = CalcServiceRequest()
            calc_request.operation = operation
            calc_request.operand1 = operand1
            calc_request.operand2 = operand2

            rospy.loginfo(f"Solicitando cálculo: {operand1} {operation} {operand2}")
            response = self.calculate_service(calc_request)

            rospy.loginfo(f"Resultado do serviço: {operand1} {operation} {operand2} = {response.result}")
            rospy.loginfo(f"Status: {response.status}")
        except rospy.ServiceException as e:
            rospy.logerr(f"Erro ao chamar o serviço de cálculo: {e}")

    def get_input_from_terminal(self):
        while not rospy.is_shutdown():
            try:
                operation = input("Digite a operação (+, -, *, /) ou 'q' para sair: ")
                if operation == 'q':
                    rospy.loginfo("Encerrando o programa.")
                    break

                operand1 = float(input("Digite o primeiro operando: "))
                operand2 = float(input("Digite o segundo operando: "))
                self.request_calculation(operation, operand1, operand2)
            except ValueError:
                rospy.logwarn("Entrada inválida! Certifique-se de digitar números válidos.")
            except Exception as e:
                rospy.logerr(f"Erro inesperado: {e}")

if __name__ == '__main__':
    try:
        node = TerminalNode()
        node.get_input_from_terminal()
    except rospy.ROSInterruptException:
        rospy.loginfo("Nó interrompido.")
