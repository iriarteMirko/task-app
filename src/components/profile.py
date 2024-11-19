import flet as ft
from src.config import AppConfig


class Profile:
    def __init__(self):
        self.container = ft.Container(
            content=ft.Text(
                "Bienvenido al Perfil",
                size=AppConfig.TEXT_STYLES["title"]["size"],
                weight=AppConfig.FONT_FAMILY["bold"],
                color=AppConfig.COLORS["bbva_medium_blue"],
            ),
        )
