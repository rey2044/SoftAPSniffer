# SoftAPSniffer

**SoftAPSniffer** is a tool that allows you to set up a Soft Access Point (AP) on a Linux system and capture HTTP and DNS requests from connected client devices. This tool is useful for monitoring and analyzing traffic from clients connecting to your Soft AP.

## Features:
- Create a Soft AP with WPA2 encryption.
- Capture HTTP and DNS requests from client devices.
- Provide internet access to connected clients.

## Installation:

### Prerequisites:
- Linux-based system (Ubuntu/Debian recommended).
- Python 3.
- `hostapd`, `iptables`, and `scapy` dependencies.

### Install via script:
1. Clone the repository or download the tool.
2. Run the installation script:
   ```bash
   sudo ./install.sh


softapsniffer --interface <wlan0> --ssid <SSID> --passphrase <PASSWORD>
