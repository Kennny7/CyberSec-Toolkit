# main.py
from auth.security import UserAuth
from modules.wifi_analyzer import WiFiAnalyzer
from questionary import select
from rich.console import Console

class CyberTool:
    def __init__(self):
        self.console = Console()
        self.auth = UserAuth()
        self.modules = {
            'WiFi Analysis': WiFiAnalyzer,
            # Add future modules here
        }

    def main_menu(self):
        if not self.auth.authenticate():
            self.console.print("[!] Authentication Failed!", style="bold red")
            return
            
        while True:
            choice = select(
                "Select Module:",
                choices=list(self.modules.keys()) + ["Exit"]
            ).ask()
            
            if choice == "Exit":
                break
                
            module = self.modules[choice]()
            module.scan_networks()
            module.display_results()

if __name__ == "__main__":
    tool = CyberTool()
    tool.main_menu()