import flet as ft
from src.config import AppConfig
from src.components.components import title


class ContentArea:
    def __init__(self):
        self.container = ft.Container(
            content = title("Bienvenido"),
            padding = ft.padding.all(20),
            alignment = ft.alignment.top_left,
            expand = True,
        )
    
    def update_content(self, new_content=None):
        """Actualiza el contenido del área dinámica."""
        if new_content is None:
            new_content = title("Sin contenido")
        self.container.content = new_content
        self.container.update()
