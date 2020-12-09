#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data%8
    rospy.loginfo(n)

    if n == 0 :
        with open("/dev/myled0", "w") as f:
            f.write("0\n")

    elif n == 1 :
        with open("/dev/myled0", "w") as f:
            f.write("1\n")

    elif n == 2 :
        with open("/dev/myled0", "w") as f:
            f.write("2\n")

    elif n == 3 :
        with open("/dev/myled0", "w") as f:
            f.write("3\n")

    elif n == 4 :
        with open("/dev/myled0", "w") as f:
            f.write("4\n")

    elif n == 5 :
        with open("/dev/myled0", "w") as f:
            f.write("5\n")

    elif n == 6 :
        with open("/dev/myled0", "w") as f:
            f.write("6\n")

    elif n == 7 :
        with open("/dev/myled0", "w") as f:
            f.write("7\n")

    

if __name__ == '__main__':
    rospy.init_node('light')
    sub = rospy.Subscriber('count_up', Int32, cb)
    pub = rospy.Publisher('light', Int32, queue_size=1)
    rospy.spin()
