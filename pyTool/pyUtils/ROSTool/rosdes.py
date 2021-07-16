#!/usr/bin/env python3
import argparse
import json
import os
from socket import socket, AF_INET, SOCK_DGRAM

parser = argparse.ArgumentParser(
	formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument('-ip', type=str, default="localhost")
parser.add_argument('-m', action='store_true', default=False)
parser.add_argument('-s', action='store_true', default=False)
parser.add_argument('-r', action='store_true', default=False)
args = parser.parse_args()
assert not (args.m and args.ip != "localhost")
path = os.path.dirname(os.path.realpath(__file__))
core = {"IP": args.ip}

s = socket(AF_INET, SOCK_DGRAM)
s.connect(('8.8.8.8', 1))
ownIP = s.getsockname()[0]
s.close()
if args.s and args.r:
	print("Can not save and restore at the same time")
if args.s or args.r:
	with open('{}/data.rosdes.json'.format(path), 
				'w' if args.s else 'r' , 
				encoding='utf-8') as f:
		if args.s:
			json.dump(core, f, ensure_ascii=False, indent=4)
			print("Core IP saved -> {}".format(core["IP"]))
		else:
			core = json.load(f)
			print("Core IP loaded -> {}".format(core["IP"]))
ROS_MASTER_URI = "export ROS_MASTER_URI=http://{}:11311\n".format("localhost" if args.m else core["IP"])
ROS_IP = 'export ROS_IP={}\n'.format(ownIP)
with open("{}/rosdes.sh".format(path), "w") as file:
	file.write("#!/bin/sh\n")
	file.write(ROS_MASTER_URI)
	file.write("echo ROS Master URL is now set to $ROS_MASTER_URI\n")
	file.write(ROS_IP)
	file.write("echo ROS IP is now set to $ROS_IP\n")
	file.write("rm {}/rosdes.sh".format(path))
print("Run the following commands:\n\n. rosdes.sh")