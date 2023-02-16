"""
Microsoft 365 Apps 32-bit Online Installer Written in Python and XML
The setup.exe is updated every 1 day after the 2nd Tuesday of a month, UTC+7
"""
import os
config_file_name = "configuration_microsoft365_x86.xml"
main_file_name = "setup.exe"
try:
	config_file = open(config_file_name, "r")
	config_file.close()
	main_file = open(main_file_name, "r")
	main_file.close()
except FileNotFoundError:
	print("Couldn\'t download or install Microsoft 365 because the configuration file is missing!")
	exit()
print("Downloading Microsoft 365")
os.system(".\\"+main_file_name+" /download "+config_file_name)
print("Downloaded Microsoft 365 successfully")
print("Installing Microsoft 365")
os.system(".\\"+main_file_name+" /configure "+config_file_name)
print("Installed Microsoft 365 successfully")