import flet as ft
from src.config import AppConfig


class ContentArea:
    def __init__(self):
        self.container = ft.Container(
            content=ft.Text(
                "Bienvenido al inicio",
                size=20,
                weight="bold",
                color=AppConfig.COLORS["text"],
            ),
            expand=True,
            bgcolor=AppConfig.COLORS["content"],
            alignment=ft.alignment.center,
        )
    
    def update_content(self, new_text):
        """Actualiza el contenido del área dinámica."""
        self.container.content = ft.Text(
            new_text, size=20, weight="bold", color=AppConfig.COLORS["text"]
        )
