import flet as ft
from src.config import AppConfig


def create_appbar(page: ft.Page):
    """Crea la barra superior con un menú desplegable y altura personalizada."""
    return ft.Container(
        content=ft.AppBar(
            title=ft.Image(
                src=AppConfig.ICONS["bbva_white"],
                width=150,
                fit=ft.ImageFit.CONTAIN,
            ),
            bgcolor=AppConfig.COLORS["bbva_navy"],
            actions=[
                ft.Container(
                    ft.PopupMenuButton(
                        content=ft.Image(src=AppConfig.ICONS["menu"], width=30, fit=ft.ImageFit.CONTAIN,),
                        items=[
                            ft.PopupMenuItem(
                                text="Perfil",
                                content=ft.Image(src=AppConfig.ICONS["profile"], width=20, fit=ft.ImageFit.CONTAIN,),
                                on_click=lambda e: show_snack_bar(page, "Perfil seleccionado"),
                            ),
                            ft.PopupMenuItem(
                                text="Configuración",
                                content=ft.Image(src=AppConfig.ICONS["settings"], width=20, fit=ft.ImageFit.CONTAIN,),
                                on_click=lambda e: show_snack_bar(page, "Configuración seleccionada"),
                            ),
                            ft.PopupMenuItem(
                                text="On/Off",
                                content=ft.Image(src=AppConfig.ICONS["on_off"], width=20, fit=ft.ImageFit.CONTAIN,),
                                on_click=lambda e: show_snack_bar(page, "On/Off seleccionado"),
                            ),
                        ],
                    ),
                    margin=ft.margin.only(right=10),
                ),
            ],
        ),
        height=100,
    )

def show_snack_bar(page: ft.Page, message: str):
    """Muestra un mensaje temporal en la barra inferior."""
    page.snack_bar = ft.SnackBar(ft.Text(message))
    page.snack_bar.open = True
    page.update()
