#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
   global n
    n = message.data%16
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

    elif n == 8 :
        with open("/dev/myled0", "w") as f:
            f.write("8\n")

    elif n == 9 :
        with open("/dev/myled0", "w") as f:
            f.write("9\n")
           
    elif n == 10 :
        with open("/dev/myled0", "w") as f:
            f.write("10\n")
    
    elif n == 11 :
        with open("/dev/myled0", "w") as f:
            f.write(11\n")
        
    elif n == 12 :
        with open("/dev/myled0", "w") as f:
            f.write("12\n")
                    
    elif n == 13 :
        with open("/dev/myled0", "w") as f:
            f.write("13\n")
                 
    elif n == 14 :
        with open("/dev/myled0", "w") as f:
            f.write("14\n")

    elif n == 15 :
        with open("/dev/myled0", "w") as f:
            f.write("15\n")

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb)
    rospy.spin()
