#!/usr/bin/env python3
import subprocess
import argparse
import json
import os
parser = argparse.ArgumentParser(
	formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument('-ip', type=str, default="localhost")
parser.add_argument('-s', action='store_true', default=False)
parser.add_argument('-r', action='store_true', default=False)
args = parser.parse_args()

core = {"IP": args.ip}
if args.s and args.r:
	print("Can not save and restore at the same time")
if args.s or args.r:
	path = os.path.dirname(os.path.realpath(__file__))
	with open('{}/data.json'.format(path), 
				'w' if args.s else 'r' , 
				encoding='utf-8') as f:
		if args.s:
			json.dump(core, f, ensure_ascii=False, indent=4)
			print("Core IP saved -> {}".format(core["IP"]))
		else:
			core = json.load(f)
			print("Core IP loaded -> {}".format(core["IP"]))

ROS_MASTER_URI = "export ROS_MASTER_URI=http://{}:11311".format(core["IP"])
ROS_IP = 'export ROS_IP={}'.format(core["IP"])
print(ROS_MASTER_URI)
subprocess.call(ROS_IP, shell=True)
print(ROS_IP)
subprocess.call(ROS_MASTER_URI, shell=True)
print("Done!")