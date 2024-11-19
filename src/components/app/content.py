import flet as ft
from src.config import AppConfig


class ContentArea:
    def __init__(self):
        self.container = ft.Container(
            content=ft.Text(
                "Bienvenido al inicio",
                size=AppConfig.TEXT_STYLES["title"]["size"],
                weight=AppConfig.FONT_FAMILY["bold"],
                color=AppConfig.COLORS["bbva_medium_blue"],
            ),
            expand=True,
            bgcolor=AppConfig.COLORS["bbva_white"],
            alignment=ft.alignment.center,
        )
    
    def update_content(self, new_content=None):
        """Actualiza el contenido del área dinámica."""
        if new_content is None:
            new_content = ft.Text(
                "Sin contenido",
                size=AppConfig.TEXT_STYLES["title"]["size"],
                weight=AppConfig.FONT_FAMILY["bold"],
                color=AppConfig.COLORS["bbva_medium_blue"],
            )
        self.container.content = new_content
