# modules/base_module.py
from rich.console import Console
from rich.table import Table

class BaseModule:
    def __init__(self):
        self.console = Console()
        self.results = []

    def display_results(self):
        table = Table(title="Scan Results")
        table.add_column("IP", style="cyan")
        table.add_column("MAC Address", style="magenta")
        table.add_column("Device Type", style="green")
        # Add more columns
        
        for result in self.results:
            table.add_row(*result.values())
        
        self.console.print(table)