import flet as ft
from src.config import AppConfig
from src.components.app.profile import Profile
from src.components.app.configuration import Configuration
from src.components.app.exit import Exit


def create_appbar(content_area):
    """Crea la barra superior con un menú desplegable y altura personalizada."""
    return ft.Container(
        content = ft.Row(
            controls = [
                ft.Image(src=AppConfig.ICONS["bbva_tag_white"], width=250, fit=ft.ImageFit.CONTAIN),
                ft.Container(expand=True),
                ft.PopupMenuButton(
                    menu_position=ft.PopupMenuPosition.UNDER,
                    shape=ft.RoundedRectangleBorder(radius=0),
                    content=ft.Image(src=AppConfig.ICONS["menu"], width=30, fit=ft.ImageFit.CONTAIN),
                    items=[
                        ft.PopupMenuItem(
                            content=create_menu_item(AppConfig.ICONS["profile"], "Perfil"),
                            on_click=lambda e: Profile(content_area).load_profile(),
                        ),
                        ft.PopupMenuItem(
                            content=create_menu_item(AppConfig.ICONS["settings"], "Configuración"),
                            on_click=lambda e: Configuration(content_area).load_configuration(),
                        ),
                        ft.PopupMenuItem(
                            content=create_menu_item(AppConfig.ICONS["on_off"], "Salir"),
                            on_click=lambda e: Exit(content_area.container.page).destroy_app(),
                        ),
                    ],
                ),
            ],
            alignment = "center",
            vertical_alignment = "center",
        ),
        height = 100,
        bgcolor = AppConfig.COLORS["bbva_navy"],
        padding = ft.padding.only(left=20, right=20),
        margin = ft.margin.only(bottom=-10),
    )

def create_menu_item(icon_src: str, text: str):
    """Crea un elemento de menú con ícono y texto."""
    return ft.Row(
        controls = [
            ft.Image(src=icon_src, width=20, fit=ft.ImageFit.CONTAIN),
            ft.Text(text, size=14, color=AppConfig.COLORS["bbva_medium_blue"]),
        ],
        alignment="start",
        spacing=10,
    )
