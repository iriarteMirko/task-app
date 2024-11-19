import flet as ft
from src.config import AppConfig


class Configuration:
    def __init__(self):
        self.container = ft.Container(
            padding=ft.padding.all(20),
            content=ft.Column(
                controls=[
                    ft.Text("Configuración", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "Personaliza la aplicación a tu gusto.",
                        size=14,
                        color=AppConfig.COLORS["bbva_medium_blue"],
                    ),
                ],
                spacing=10,
            ),
        )