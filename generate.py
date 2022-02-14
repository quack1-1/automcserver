#!/usr/bin/env python3
import os
import threading
import time
import argparse

def plugins():
	os.system("echo waiting on download...")
	os.system("gdown https://drive.google.com/uc?id=1BKw6Q4XRueChvmzo-td0v3uiHRai2He8")
	os.system("unzip plugins.zip")
	print("done")

def vanilla_executable():
	print("use start.sh to startup server")
	os.system("echo '#!/bin/bash\njava -Xmx6G -Xms6G -jar Paper_Latest.jar --nogui' >> start.sh")
	os.system("echo '#!/bin/bash\njava -Xmx6G -Xms6G -jar Paper_Latest.jar' >> start_gui.sh")
	os.system("gdown https://drive.google.com/uc?id=1BbIyIo5qk4WVQYkY7NUfNSsfLopj223N")
	os.system("sudo chmod +x start.py")
	os.system("sudo chmod +x start.sh")
	os.system("sudo chmod +x start_gui.sh")

def fabric_executable():
	print("use start.sh to startup server")
	os.system("echo '#!/bin/bash\njava -Xmx6G -Xms6G -jar Paper_Latest.jar --nogui' >> start.sh")
	os.system("echo '#!/bin/bash\njava -Xmx6G -Xms6G -jar Paper_Latest.jar' >> start_gui.sh")
	os.system("gdown https://drive.google.com/uc?id=1BbIyIo5qk4WVQYkY7NUfNSsfLopj223N")
	os.system("sudo chmod +x start.py")
	os.system("sudo chmod +x start.sh")
	os.system("sudo chmod +x start_gui.sh")

def server_props():
	os.system("echo waiting on download...")
	#server.properties download
	os.system("gdown https://drive.google.com/uc?id=1AvgcS9Q7SvlGxrT6Qf4WgX1QGNN9kXn2")
	#eula.txt download
	os.system("gdown https://drive.google.com/uc?id=1AtqU4GK_iE0QdthnEQswXAuq_5BeZpVy")
	print("done")

def paper_executable():
	print("use start.py to startup server")
	os.system("echo '#!/bin/bash\njava -Xmx6G -Xms6G -jar Paper_Latest.jar --nogui' >> start.sh")
	os.system("echo '#!/bin/bash\njava -Xmx6G -Xms6G -jar Paper_Latest.jar' >> start_gui.sh")
	os.system("gdown https://drive.google.com/uc?id=1BbIyIo5qk4WVQYkY7NUfNSsfLopj223N")
	os.system("sudo chmod +x start.py")
	os.system("sudo chmod +x start.sh")
	os.system("sudo chmod +x start_gui.sh")


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--auto-start',
	dest='start', 
	help='auto-start minecraft server after generated',
	action='store_true')
parser.add_argument('-g', '--gui',
	help='enable gui for auto-start (BY DEFAULT OFF, ONLY USE FLAG IF WANTED)',
	dest='gui',
	action='store_true')
parser.add_argument('-v', '--vanilla',
	dest='vanilla',
	help='create vanilla mc server',
	action='store_true')
parser.add_argument('-p', '--paper',
	dest='paper',
	help='create papermc server',
	action='store_true')
parser.add_argument('-f', '--fabric',
	dest='fabric',
	help='create fabric mc server',
	action='store_true')
parser.add_argument('-c', '--custom',
	dest='custom',
	help='create premade custom server',
	action='store_true')

def main():
	args = parser.parse_args()
	custom = args.custom
	paper = args.paper
	vanilla = args.vanilla
	fabric = args.fabric
	start = args.start
	gui = args.gui
	if custom == True:
		plugins()
		os.system("echo ")
		os.system("gdown https://drive.google.com/uc?id=1Anyd0KD1v6d6heXfV9JfeTkb3Pa3twMg")
		server_props()
		paper_executable()
	if paper == True:
		os.system("gdown https://drive.google.com/uc?id=1Anyd0KD1v6d6heXfV9JfeTkb3Pa3twMg")
		server_props()
		paper_executable()
	if vanilla == True:
		os.system("gdown https://drive.google.com/uc?id=1Baz9KxRxHRKlFyxFBDmfTQsr62Wd_R68")
		server_props()
		vanilla_executable()
	if fabric == True:
		os.system("curl -OJ https://meta.fabricmc.net/v2/versions/loader/1.18.1/0.13.1/0.10.2/server/jar")
		server_props()
		fabric_executable()
	if start == True:
		print("server downloaded. now starting..")
		if gui == True:
			os.system("./start.py --g")
		if gui == False:
			os.system("./start.py")
main()