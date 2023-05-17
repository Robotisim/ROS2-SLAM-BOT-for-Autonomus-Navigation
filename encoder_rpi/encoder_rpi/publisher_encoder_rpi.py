#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
import RPi.GPIO as GPIO

A_pin = 21
B_pin = 20

# import random
class EncoderNode(Node):
    def __init__(self):
        super().__init__("encoder")
        self.outcome = [0,1,-1,0,-1,0,0,1,1,0,0,-1,0,-1,1,0]
        self.last_AB = 0b00
        self.counter = 0

        self.encoder_publisher_ = self.create_publisher(
            Int64, "encoder", 10)
        self.encoder_timer_ = self.create_timer(
            0.0001, self.publish_encoder)
    def publish_encoder(self):
        A = GPIO.input(A_pin)
        B = GPIO.input(B_pin)
        self.current_AB = (A << 1) | B
        self.position = (self.last_AB << 2) | self.current_AB
        self.counter += self.outcome[self.position]
        self.last_AB = self.current_AB
        msg = Int64()
        msg.data = self.counter
        self.encoder_publisher_.publish(msg)
def main(args=None):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(A_pin, GPIO.IN)
    GPIO.setup(B_pin, GPIO.IN)

    rclpy.init(args=args)
    node = EncoderNode()
    rclpy.spin(node)
    rclpy.shutdown()
    GPIO.cleanup()
if __name__ == "__main__":
    main()