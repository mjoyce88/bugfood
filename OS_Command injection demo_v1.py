#!/usr/bin/env python
# coding: utf-8

# In[33]:


#This script tests for a file being succeptable to command injection.
import subprocess

def test_command_injection(file_path):
    # Specify the command injection payload to test
    payload = "ping -c 5 8.8.8.8"  # Desired payload

    # Construct the command to execute it opens the file 
    command = f"{file_path} {payload}"

    try:
        # Execute the command and capture the output
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)

        # Print the output
        print("Command executed successfully:")
        print(output.decode())
    except subprocess.CalledProcessError as e:
        # An error occurred while executing the command
        print("Command execution failed:")
        print(e.output.decode())

# File_path to your file
file_path = "C:\\Users\Student\Downloads\lib2def.py"
test_command_injection(file_path)

