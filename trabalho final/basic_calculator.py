import rospy
from std_msgs.msg import String, Float64MultiArray, Float64
from std_srvs.srv import Empty

class BasicCalculator:
    def __init__(self):
        rospy.init_node('basic_calculator_node')
        self.service = rospy.Service('calculate', Empty, self.handle_calculation)
        self.display_pub = rospy.Publisher('display', String, queue_size=10)
        self.last_result = ""
        rospy.spin()

    def handle_calculation(self, req):
        # Parse a operação e operandos da requisição (simplificado)
        operation = req.operation
        operand1 = req.operand1
        operand2 = req.operand2
        result = None
        status = "operação realizada"

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
                status = "operação não realizada"
        
        self.last_result = f"{operand1} {operation} {operand2} = {result}"
        self.display_pub.publish(self.last_result)

        return Float64(result), status

if __name__ == '__main__':
    BasicCalculator()
