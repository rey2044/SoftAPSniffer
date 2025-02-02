#!/bin/bash

echo "Installing SoftAPSniffer..."

# Install dependencies
sudo apt-get update
sudo apt-get install -y python3 python3-pip hostapd iptables scapy

# Set script executable
chmod +x softapsniffer.py

# Create a symlink for easy command-line access
sudo ln -s $(pwd)/softapsniffer.py /usr/local/bin/softapsniffer

# Optional: Install dependencies listed in requirements.txt
pip3 install -r requirements.txt

echo "Installation complete! You can now use the tool by running 'softapsniffer'."
