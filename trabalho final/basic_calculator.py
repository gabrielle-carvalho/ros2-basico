import rospy
from std_msgs.msg import String
from your_package.srv import CalcService, CalcServiceResponse

class BasicCalculator:
    def __init__(self):
        rospy.init_node('basic_calculator_node')
        self.service = rospy.Service('calculate', CalcService, self.handle_calculation)
        self.display_pub = rospy.Publisher('display', String, queue_size=10)
        self.last_result = ""
        rospy.spin()

    def handle_calculation(self, req):
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
                result = float('nan')
                status = "operação não realizada: divisão por zero"
        
        self.last_result = f"{operand1} {operation} {operand2} = {result}"
        self.display_pub.publish(self.last_result)

        return CalcServiceResponse(result, status)

if __name__ == '__main__':
    BasicCalculator()
