SoftAPSniffer

SoftAPSniffer is a powerful network tool that allows you to set up a Soft Access Point (AP) on a Linux system and capture network traffic from client devices that connect to it. The tool provides internet access to connected clients while simultaneously sniffing and analyzing the HTTP and DNS requests they make. It is ideal for monitoring, debugging, or analyzing network traffic in real-time.
Features

    Create a Soft Access Point (AP) on a Linux machine.
    Capture network traffic (HTTP requests, DNS queries) from client devices connected to your Soft AP.
    Provides internet access to connected clients using NAT and IP forwarding.
    Written in Python, using scapy for packet sniffing.

Prerequisites

Before installing and running SoftAPSniffer, ensure your system meets the following requirements:
System Requirements:

    A Linux-based operating system (Ubuntu/Debian is recommended).
    A wireless network adapter (e.g., TP-Link) that supports Access Point (AP) mode.
    hostapd and iptables installed for Soft AP setup and NAT.
    Python 3 installed (recommended version: Python 3.6 or higher).
    scapy Python library for packet sniffing.

Dependencies:

    scapy: Used for packet sniffing and network traffic analysis.

Installation

To install SoftAPSniffer, follow these steps:
1. Clone the Repository

Clone the repository to your local machine:

git clone https://github.com/rey2044/SoftAPSniffer.git
cd SoftAPSniffer

2. Install Required Packages

Run the installation script to install dependencies and make the tool executable:

chmod +x install.sh
sudo ./install.sh

This will:

    Install Python 3, scapy, hostapd, and iptables if they are not already installed.
    Make the softapsniffer.py script executable and place a symlink in /usr/local/bin/ for easy command-line access.

3. Install Python Dependencies

If you haven't already installed Python dependencies, use the requirements.txt file:

pip3 install -r requirements.txt

4. Check Hostapd and Network Configuration

Make sure hostapd and your wireless adapter are properly configured for AP mode. You may need to edit your network interface settings or troubleshoot any potential issues with your adapter.
Usage

Once the installation is complete, you can start using SoftAPSniffer to create a Soft AP and capture traffic.
Command Line Syntax

To run the tool, use the following command:

softapsniffer --interface <interface> --ssid <SSID> --passphrase <PASSWORD>

    <interface>: Your wireless network interface (e.g., wlan0).
    <SSID>: The name (SSID) of your Soft AP.
    <PASSWORD>: The WPA2 password for the Soft AP.

Example:

softapsniffer --interface wlan0 --ssid MySoftAP --passphrase MyPassword123

This will:

    Set up a Soft AP on interface wlan0 with SSID MySoftAP.
    The passphrase for the AP will be MyPassword123.
    It will also begin sniffing network traffic from connected devices (HTTP requests, DNS queries).

Basic Tutorial
Step 1: Set Up the Soft AP

Run the tool with your desired settings:

softapsniffer --interface wlan0 --ssid "MySoftAP" --passphrase "MySecurePassword"

This will create a Soft AP, allowing client devices to connect to it. Once connected, the client will be able to access the internet (thanks to NAT and IP forwarding).
Step 2: Capture Client Traffic

After starting the Soft AP, the tool will begin sniffing traffic from connected clients. Any HTTP requests and DNS queries made by these devices will be captured and logged in real-time in your terminal.

For example:

    HTTP Requests: You might see requests like GET / HTTP/1.1 when a client accesses a website.
    DNS Queries: You may capture DNS queries like example.com when a client resolves a domain.

Step 3: Monitor Traffic and Analyze Logs

Once client devices start connecting to your Soft AP, you can monitor the captured requests in your terminal. The tool will print out details about each HTTP request and DNS query made by clients, such as:

HTTP Request from 192.168.1.101 to 192.168.1.1: GET /index.html HTTP/1.1
DNS Query from 192.168.1.101: www.example.com

This information can be used to:

    Monitor the websites or services being accessed.
    Debug network traffic and request patterns.
    Perform simple network analysis or auditing.

Configuration

You can configure various parameters in the softapsniffer.py script, such as:

    The channel number for the Soft AP.
    The authentication type used (e.g., WPA2).
    Network interface settings (make sure your wireless adapter supports AP mode).

You can also customize the packet capture logic to analyze additional types of network traffic, including other protocols like FTP, SMTP, etc.
Troubleshooting
1. No Wireless Network Adapter Detected

Ensure your network adapter supports Access Point (AP) mode. You can check if your adapter supports it with the following command:

iw list

Look for "AP" in the list of supported interface modes.
2. hostapd Configuration Errors

If you encounter issues with hostapd not starting, check your wireless driver settings or try running hostapd manually with a configuration file to troubleshoot.
3. No Internet for Clients

Ensure that IP forwarding is enabled, and that NAT is correctly configured using iptables. You can verify the NAT rule with:

sudo iptables -t nat -L

License

SoftAPSniffer is released under the MIT License. See the LICENSE file for details.
Additional Notes

    This tool should be used ethically. Only monitor networks that you own or have explicit permission to capture traffic from.
    HTTPS traffic will not be captured in plaintext because it is encrypted. However, you can still capture SNI (Server Name Indication) from the SSL handshake to see which websites the client is trying to access.
