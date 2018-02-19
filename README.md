# AutoArpChecker
Code by Yangfu1000

# Conditions Of Use Or "The Dont Be A Jerk" Clause
This is an open source program any one can use and edit.
If you do distribute or edit it give give credit to me.

# Purpose
Scan your network for unknown ip addresses

# Directions
Make an empty folder where you will store the program
Download the files to the folder

Run the program once to make the files
Close the program by exiting out of the command prompt

This will create several folders
A file named ignore that stores garbage
A file named ip list that stores all current ips
A file named whitelist that stores the known ips
A file named unknownList that stores a log of all unknown ips

Do not edit the file named ignore
Do not edit the file named ipList
The file named whitelist is where you type ip addresses allowed on the network
The file named unknownList is a log of what unknown ip addresses have gone through the network

Add ip addresses that are allowed in the network in the whitelist file with the format ###.###.###.### where the #'s are numbers
Put at least one space between ip addresses in the whitelist file
Double click the file named AutoArpChecker to run it
A command prompt will appear do not exit out of it unless you want to end the program
The command prompt will show unknown ip addresses every 5 seconds

To end the program exit out of the command prompt
