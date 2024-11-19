import flet as ft
from src.config import AppConfig


def create_appbar(page: ft.Page):
    """Crea la barra superior con un menú desplegable."""
    return ft.AppBar(
        title=ft.Text("Task App - BBVA", color=AppConfig.COLORS["white"]),
        bgcolor=AppConfig.COLORS["primary"],
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        text="Tema Claro",
                        icon=ft.Image(src=AppConfig.ICONS["theme_light"], width=24),
                        on_click=lambda e: set_theme(page, "light"),
                    ),
                    ft.PopupMenuItem(
                        text="Tema Oscuro",
                        icon=ft.Image(src=AppConfig.ICONS["theme_dark"], width=24),
                        on_click=lambda e: set_theme(page, "dark"),
                    ),
                ]
            )
        ],
    )

def set_theme(page: ft.Page, theme: str):
    """Cambia el tema de la aplicación."""
    page.theme_mode = theme
    page.update()
