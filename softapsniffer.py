#!/usr/bin/env python3

import subprocess
import scapy.all as scapy
import argparse
import time
import threading
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def enable_ip_forwarding():
    """Enable IP forwarding for internet sharing."""
    subprocess.run("sudo sysctl -w net.ipv4.ip_forward=1", shell=True, check=True)
    logging.info("IP forwarding enabled.")

def configure_nat():
    """Set up NAT with iptables for internet sharing."""
    subprocess.run("sudo iptables --table nat -A POSTROUTING -o eth0 -j MASQUERADE", shell=True, check=True)
    subprocess.run("sudo iptables -A FORWARD -i wlan0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT", shell=True, check=True)
    subprocess.run("sudo iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT", shell=True, check=True)
    logging.info("NAT configuration completed.")

def start_hostapd(interface, ssid, passphrase):
    """Set up the Soft AP using hostapd."""
    hostapd_conf = f"""
    interface={interface}
    driver=nl80211
    ssid={ssid}
    hw_mode=g
    channel=7
    wpa=2
    wpa_passphrase={passphrase}
    auth_algs=1
    """
    
    conf_file = "/tmp/hostapd.conf"
    with open(conf_file, 'w') as f:
        f.write(hostapd_conf)

    subprocess.run(["sudo", "hostapd", conf_file], check=True)
    logging.info("Soft AP started.")

def capture_packets(interface):
    """Capture HTTP requests and DNS queries from the client devices."""
    def process_packet(packet):
        # Check for HTTP requests
        if packet.haslayer(scapy.IP):
            ip_src = packet[scapy.IP].src
            ip_dst = packet[scapy.IP].dst

            if packet.haslayer(scapy.TCP) and packet[scapy.TCP].dport == 80:  # HTTP traffic
                if packet.haslayer(scapy.Raw):
                    payload = packet[scapy.Raw].load
                    logging.info(f"HTTP Request from {ip_src} to {ip_dst}: {payload.decode(errors='ignore')}")
            elif packet.haslayer(scapy.UDP) and packet[scapy.UDP].dport == 53:  # DNS traffic
                dns_query = packet[scapy.DNS].qd.qname.decode(errors='ignore')
                logging.info(f"DNS Query from {ip_src}: {dns_query}")

    logging.info("Starting packet capture...")
    scapy.sniff(iface=interface, store=0, prn=process_packet)

def main():
    parser = argparse.ArgumentParser(description="SoftAPSniffer - Set up Soft AP and capture client traffic.")
    parser.add_argument("--interface", required=True, help="Wireless interface for Soft AP (e.g., wlan0)")
    parser.add_argument("--ssid", required=True, help="SSID for the Soft AP")
    parser.add_argument("--passphrase", required=True, help="WPA2 passphrase for the Soft AP")
    
    args = parser.parse_args()

    # Enable IP forwarding and configure NAT
    enable_ip_forwarding()
    configure_nat()

    # Start the Soft AP
    threading.Thread(target=start_hostapd, args=(args.interface, args.ssid, args.passphrase)).start()
    
    # Start packet capture in parallel
    capture_thread = threading.Thread(target=capture_packets, args=(args.interface,))
    capture_thread.start()

if __name__ == "__main__":
    main()
