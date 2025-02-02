# SoftAPSniffer

**SoftAPSniffer** is a powerful network tool that allows you to create a **Soft Access Point (AP)** on your Linux system while monitoring and capturing network traffic from client devices that connect to it. The tool provides a user-friendly interface for setting up the AP and offers the ability to capture key network traffic such as HTTP requests and DNS queries.

## Features

- **Create a Soft Access Point (AP)** on a Linux machine.
- Monitor and capture **HTTP requests** and **DNS queries** from client devices.
- Provide **internet access** to connected devices using network address translation (NAT).
- Lightweight and easy to use.
- **Python-based** with the use of popular networking libraries.

## Prerequisites

### System Requirements:
- **Linux-based operating system** (e.g., Ubuntu/Debian).
- A **wireless network adapter** capable of operating in **Access Point (AP) mode**.
- **`hostapd`** and **`iptables`** utilities installed for Soft AP setup and NAT configuration.
- **Python 3** installed (Python 3.6 or higher is recommended).

### Dependencies:
- **scapy**: This Python package is used for packet sniffing and analyzing network traffic.

## Installation

Follow these steps to install **SoftAPSniffer**:

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/rey2044/SoftAPSniffer.git
cd SoftAPSniffer
```

### 2. Install Required Packages

Run the installation script to install dependencies and configure the tool for use:

```bash
chmod +x install.sh
sudo ./install.sh
```

This script will:
- Install **Python 3**, **scapy**, **hostapd**, and **iptables** (if they are not already installed).
- Make the `softapsniffer.py` script executable and available via a system-wide path.

### 3. Install Python Dependencies

If the Python dependencies haven't been installed yet, use the following command:

```bash
pip3 install -r requirements.txt
```

This will install **scapy** and any future dependencies added to the project.

### 4. Configure Hostapd and Network

Ensure that **hostapd** is configured correctly and that your wireless adapter supports **AP mode**. You might need to adjust network interface settings depending on your system configuration.

---

## Usage

Once installed, you can start **SoftAPSniffer** with the following command:

### Command Line Syntax

```bash
softapsniffer --interface <interface> --ssid <SSID> --passphrase <PASSWORD>
```

- **`<interface>`**: The wireless network interface to be used (e.g., `wlan0`).
- **`<SSID>`**: The SSID (name) of your Soft AP.
- **`<PASSWORD>`**: The WPA2 passphrase for securing your AP.

### Example:

```bash
softapsniffer --interface wlan0 --ssid "MySoftAP" --passphrase "MySecurePassword"
```

This will:
- Set up the Soft AP on the specified interface (`wlan0`).
- Use **"MySoftAP"** as the SSID and **"MySecurePassword"** as the WPA2 passphrase.
- Enable connected devices to access the internet (through NAT and IP forwarding).

---

## Basic Tutorial

### Step 1: Set Up the Soft AP

Run the tool with your desired settings:

```bash
softapsniffer --interface wlan0 --ssid "MySoftAP" --passphrase "MySecurePassword"
```

Once the Soft AP is created, clients can connect to it using the provided SSID and password. These clients will have internet access, and the tool will monitor their network traffic.

### Step 2: Capture Traffic from Connected Clients

After starting the Soft AP, the tool will capture traffic from any devices that connect to it. It will log key network events like **HTTP requests** and **DNS queries** from connected clients.

For example, captured traffic might look like this:

```
HTTP Request from 192.168.1.101 to 192.168.1.1: GET /index.html HTTP/1.1
DNS Query from 192.168.1.101: www.example.com
```

### Step 3: Monitor and Analyze the Traffic

You can now monitor the captured requests in real-time as clients interact with the Soft AP. This will allow you to see which websites or services they are accessing, providing valuable insights into network activity.

---

## Configuration

You can adjust certain configurations directly in the `softapsniffer.py` script:

- Change the wireless **channel** or **SSID** settings for the Soft AP.
- Modify the type of traffic to capture (e.g., HTTP, DNS, etc.).
- Customize the NAT and IP forwarding configurations.

Please note that the core logic for creating the Soft AP and capturing traffic is abstracted for simplicity and security purposes.

---

## Troubleshooting

### 1. No Wireless Adapter Detected

Ensure your wireless network adapter supports **Access Point (AP) mode**. You can verify this by running the following command:

```bash
iw list
```

Look for **"AP"** in the list of supported interface modes. If your adapter does not support AP mode, you may need to use a different device.

### 2. Hostapd Configuration Issues

If you encounter errors with `hostapd` not starting, check your network interface configuration or attempt to run `hostapd` manually to troubleshoot.

### 3. Clients Can't Connect to the AP

Ensure that **IP forwarding** is enabled, and that **iptables** is correctly configured for **NAT**. You can check the NAT configuration with:

```bash
sudo iptables -t nat -L
```

Make sure the necessary rules are set up to allow client devices to access the internet.

---

## License

**SoftAPSniffer** is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contributions

Contributions to **SoftAPSniffer** are welcome! Feel free to fork the repository, submit bug reports, or create pull requests for new features or improvements.

Please note:
- **Security**: Be cautious when using this tool. Only monitor networks that you own or have explicit permission to analyze.
- **HTTPS Traffic**: Since traffic is encrypted, only the **SNI** (Server Name Indication) of HTTPS requests will be visible.

---

### Additional Notes

- **Ethical Usage**: Ensure that you are only using **SoftAPSniffer** on networks where you have permission to monitor traffic.
- **Future Features**: We are working on additional features such as more detailed traffic analysis, support for more protocols, and enhanced security.

