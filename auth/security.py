# auth/security.py
import bcrypt
import socket
from rich.console import Console
from questionary import password

class UserAuth:
    def __init__(self):
        self.console = Console()
        self.stored_hash = b'$2b$12$Bw5w/TA4ucZR1Y8D2C3YgeVhQ4v9vQ7z8bW8cJfJ6dKkL1aNp6rO'  # Sample hash
    
    def check_ip_port(self):
        """Check system IP and open ports"""
        ip = socket.gethostbyname(socket.gethostname())
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_status = not sock.connect_ex(('localhost', 8080))
        return ip, port_status

    def authenticate(self):
        ip, port_open = self.check_ip_port()
        self.console.print(f"[!] System IP: {ip}", style="bold red")
        
        if not port_open:
            self.console.print("[!] Critical port closed!", style="bold red")
            return False
            
        pwd = password("Enter master password:").ask()
        return bcrypt.checkpw(pwd.encode(), self.stored_hash)