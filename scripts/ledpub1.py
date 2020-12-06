#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32



if __name__ == "__main__":
	rospy.init_node("led_pub")
	pub = rospy.Publisher("led", Int32, queue_size=1)
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            s = input()
	    pub.publish(s)
            rate.sleep()
