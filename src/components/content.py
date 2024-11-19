import flet as ft
from src.config import AppConfig


class ContentArea:
    def __init__(self):
        self.container = ft.Container(
            content=ft.Text(
                "Bienvenido al inicio",
                size=AppConfig.TEXT_STYLES["body"]["size"],
                font_family=AppConfig.FONT_FAMILY["regular"],
                color=AppConfig.COLORS["bbva_navy"],
            ),
            expand=True,
            bgcolor=AppConfig.COLORS["bbva_white"],
            alignment=ft.alignment.center,
        )
    
    def update_content(self, new_text):
        """Actualiza el contenido del área dinámica."""
        self.container.content = ft.Text(
            new_text,
            size=AppConfig.TEXT_STYLES["body"]["size"],
            font_family=AppConfig.FONT_FAMILY["regular"],
            color=AppConfig.COLORS["bbva_navy"],
        )
