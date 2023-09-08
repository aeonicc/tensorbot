#!/usr/bin/env python

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def main():
    rospy.init_node('camera_node', anonymous=True)
    pub = rospy.Publisher('camera_image', Image, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    cap = cv2.VideoCapture(0)  # Change the device index if needed
    bridge = CvBridge()

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:
            image_message = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            pub.publish(image_message)
        rate.sleep()

    cap.release()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
