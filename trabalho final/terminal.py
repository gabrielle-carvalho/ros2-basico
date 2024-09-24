import rospy
from std_msgs.msg import String

class TerminalNode:
    def __init__(self):
        rospy.init_node('terminal_node')
        self.display_sub = rospy.Subscriber('display', String, self.display_callback)

    def display_callback(self, msg):
        rospy.loginfo(f"Resultado da operação: {msg.data}")

    def request_calculation(self, operation, operand1, operand2):
        # faz a requisição ao serviço `calculate`
        pass

if __name__ == '__main__':
    TerminalNode()
    rospy.spin()
