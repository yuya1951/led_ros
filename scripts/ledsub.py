#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def led_callback(msg):

    if msg == i:
        with open("/dev/myled0", "w") as f:
	    f.write("0\n" )

    if msg == j :
        with open("/dev/myled0", "w") as f:
            f.write("1\n" )

    if msg == k:
        with open("/dev/myled0", "w") as f:
            f.write("2\n" )

if __name__ == "__main__":
        i = Int32(0)
        j = Int32(1)
        k = Int32(2)
	rospy.init_node("led_pub")
	sub = rospy.Subscriber("led", Int32, led_callback)
	rospy.spin()
