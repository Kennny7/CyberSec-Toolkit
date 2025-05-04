# modules/wifi_analyzer.py
import subprocess
import re
from .base_module import BaseModule

class WiFiAnalyzer(BaseModule):
    def __init__(self):
        super().__init__()
        self.console.print("[+] WiFi Analyzer Module Activated", style="bold green")

    def scan_networks(self):
        try:
            output = subprocess.check_output(['iwconfig'], text=True)
            # Parse wireless interfaces
            interfaces = re.findall(r'(\w+)\s+IEEE 802.11', output)
            
            for interface in interfaces:
                scan_cmd = f"iwlist {interface} scan"
                scan_output = subprocess.check_output(scan_cmd.split(), text=True)
                self._parse_scan_results(scan_output)
                
        except Exception as e:
            self.console.print(f"[!] Error: {e}", style="bold red")

    def _parse_scan_results(self, data):
        # Advanced parsing of wireless networks
        networks = re.split(r'Cell \d+ -', data)[1:]
        for net in networks:
            network_info = {
                'SSID': re.search(r'ESSID:"(.*?)"', net).group(1),
                'BSSID': re.search(r'Address: ([\w:]+)', net).group(1),
                'Channel': re.search(r'Channel:(\d+)', net).group(1),
                'Encryption': re.search(r'IE:.*?(WPA\d?)', net).group(1) if re.search(r'IE:.*?(WPA\d?)', net) else 'Open'
            }
            self.results.append(network_info)


# Additional methods in WiFiAnalyzer class
def enumerate_connected_devices(self):
    try:
        # Use arp-scan or similar tools
        arp_output = subprocess.check_output(['arp', '-a'], text=True)
        devices = re.findall(r'\((\d+\.\d+\.\d+\.\d+)\) at ([\w:]+)', arp_output)
        
        for ip, mac in devices:
            device_info = self._get_device_details(ip, mac)
            self.results.append(device_info)
            
    except Exception as e:
        self.console.print(f"[!] Error: {e}", style="bold red")

def _get_device_details(self, ip, mac):
    # Use nmap or custom vulnerability checks
    return {
        'ip': ip,
        'mac': mac,
        'vendor': self._mac_lookup(mac),
        'open_ports': self._port_scan(ip),
        'vulnerabilities': self._check_cves(ip)
    }