import flet as ft
from .modules.dashboard_module import *

class TaskApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Task App - Automización"
        
        self.dashboard_component = DashboardComponent(self.page)
        
        self.show_dashboard()
    
    def show_dashboard(self):
        """Mostrar el dashboard directamente al abrir la app."""
        self.page.add(self.dashboard_component.render())
        self.page.update()
