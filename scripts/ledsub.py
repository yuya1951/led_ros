#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
	global n
	n = message.data
	
	if n == 0:
		with open("/dev/myled0", "w") as f:
			f.write("0\n" )
	
	elif n == 1:
		with open("/dev/myled0", "w") as f:
			f.write("1\n" )

	elif n == 2:
		with open("/dev/myled0", "w") as f:
			f.write("2\n" )
	
	elif n == 3:
		with open("/dev/myled0", "w") as f:
			f.write("3\n" )

	elif n == 4:
		with open("/dev/myled0", "w") as f:
			f.write("4\n" )

	elif n == 5:
		with open("/dev/myled0", "w") as f:
			f.write("5\n" )
	
	elif n == 6:
		with open("/dev/myled0", "w") as f:
			f.write("6\n" )
			
	elif n == 7:
		with open("/dev/myled0", "w") as f:
			f.write("7\n" )


if __name__ == "__main__":
	rospy.init_node("ledsub")
	sub = rospy.Subscriber("led", Int32, cb)
	rospy.spin()
