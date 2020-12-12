#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
	global n
	n = message.data
	
	if message == "0":
		with open("/dev/myled0", "w") as f:
			f.write("0\n" )
	
	if message == "1":
		with open("/dev/myled0", "w") as f:
			f.write("1\n" )

	if message == "2":
		with open("/dev/myled0", "w") as f:
			f.write("2\n" )
	
	if message == "3":
		with open("/dev/myled0", "w") as f:
			f.write("3\n" )

	if message == "4":
		with open("/dev/myled0", "w") as f:
			f.write("4\n" )

	if message == "5":
		with open("/dev/myled0", "w") as f:
			f.write("5\n" )
	
	if message == "6":
		with open("/dev/myled0", "w") as f:
			f.write("6\n" )
			
	if message == "7":
		with open("/dev/myled0", "w") as f:
			f.write("7\n" )


if __name__ == "__main__":
	rospy.init_node("ledsub")
	sub = rospy.Subscriber("led", Int32, cb)
	rospy.spin()
