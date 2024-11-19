import flet as ft
from src.config import AppConfig
from src.components.profile import Profile
from src.components.content import ContentArea


def create_appbar(page: ft.Page, content_area: ContentArea):
    """Crea la barra superior con un menú desplegable y altura personalizada."""
    return ft.Container(
        height=100,
        padding=ft.padding.only(left=20, right=20),
        margin=ft.margin.only(bottom=-10),
        bgcolor=AppConfig.COLORS["bbva_navy"],
        content=ft.Row(
            controls=[
                ft.Image(src=AppConfig.ICONS["bbva_white"], width=150, fit=ft.ImageFit.CONTAIN),
                ft.Container(expand=True),
                ft.PopupMenuButton(
                    menu_position=ft.PopupMenuPosition.UNDER,
                    content=ft.Image(src=AppConfig.ICONS["menu"], width=30, fit=ft.ImageFit.CONTAIN),
                    items=[
                        ft.PopupMenuItem(
                            content=create_menu_item(AppConfig.ICONS["profile"], "Perfil"),
                            on_click=lambda e: load_profile(content_area),
                        ),
                        ft.PopupMenuItem(
                            content=create_menu_item(AppConfig.ICONS["settings"], "Configuración"),
                            on_click=lambda e: show_snack_bar(page, "Configuración seleccionada"),
                        ),
                        ft.PopupMenuItem(
                            content=create_menu_item(AppConfig.ICONS["on_off"], "On/Off"),
                            on_click=lambda e: show_snack_bar(page, "On/Off seleccionado"),
                        ),
                    ],
                ),
            ],
            alignment="center",
            vertical_alignment="center",
        ),
    )

def create_menu_item(icon_src: str, text: str):
    """Crea un elemento de menú con ícono y texto."""
    return ft.Row(
        controls=[
            ft.Image(src=icon_src, width=20, fit=ft.ImageFit.CONTAIN),
            ft.Text(text, size=14, color=AppConfig.COLORS["bbva_medium_blue"]),
        ],
        alignment="start",  # Alinea el ícono y el texto a la izquierda
        spacing=10,  # Espaciado entre ícono y texto
    )

def load_profile(content_area: ContentArea):
    """Carga el contenido de la sección 'Perfil' en el área dinámica."""
    content_area.container.content = Profile().container
    content_area.container.update()


def show_snack_bar(page: ft.Page, message: str):
    """Muestra un mensaje temporal en la barra inferior."""
    page.snack_bar = ft.SnackBar(ft.Text(message))
    page.snack_bar.open = True
    page.update()
