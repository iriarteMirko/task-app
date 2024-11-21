import flet as ft
from src.config import AppConfig
from src.components.app.profile import Profile
from src.components.app.configuration import Configuration
from src.components.app.exit import Exit
from src.components.components import row_image_text, image


def create_appbar(content_area):
    """Crea la barra superior con un menú desplegable y altura personalizada."""
    return ft.Container(
        content = ft.Row(
            controls = [
                image("bbva_tag_white", width=250),
                ft.Container(expand=True),
                ft.PopupMenuButton(
                    menu_position = ft.PopupMenuPosition.UNDER,
                    shape = ft.RoundedRectangleBorder(radius=0),
                    content = image("menu", width=30),
                    items = [
                        ft.PopupMenuItem(
                            content = row_image_text("Perfil", "profile", "bbva_medium_blue", "body"),
                            on_click = lambda e: Profile(content_area).load_profile(),
                        ),
                        ft.PopupMenuItem(
                            content = row_image_text("Configuración", "settings", "bbva_medium_blue", "body"),
                            on_click = lambda e: Configuration(content_area).load_configuration(),
                        ),
                        ft.PopupMenuItem(
                            content = row_image_text("Salir", "on_off", "bbva_medium_blue", "body"),
                            on_click = lambda e: Exit(content_area.container.page).destroy_app(),
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
