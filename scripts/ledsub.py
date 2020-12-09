#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def callback(messsage):

    if message == a:
        with open("/dev/myled0", "w") as f:
		f.write("0\n" )

    if message == b :
        with open("/dev/myled0", "w") as f:
		f.write("1\n" )

    if message == c:
        with open("/dev/myled0", "w") as f:
		f.write("2\n" )
	
    if message == d:
        with open("/dev/myled0", "w") as f:
		f.write("3\n" )

    if message == e :
        with open("/dev/myled0", "w") as f:
		f.write("4\n" )

    if message == g:
        with open("/dev/myled0", "w") as f:
		f.write("5\n" )
	
    if message == h:
        with open("/dev/myled0", "w") as f:
		f.write("6\n" )

    if message == i :
        with open("/dev/myled0", "w") as f:
		f.write("7\n" )

    
    
	
	
	
if __name__ == "__main__":
	a = Int32(0)
	b = Int32(1)
	c = Int32(2)
	d = Int32(3)
	e = Int32(4)
	g = Int32(5)
	h = Int32(6)
	i = Int32(7)
	j = Int32(8)
	
        
	
        rospy.init_node("ledsub")
	sub = rospy.Subscriber("led", Int32, callback)
	pub = rospy.Publisher("ledsub", Int32, queue_size = 1)
	rospy.spin()
