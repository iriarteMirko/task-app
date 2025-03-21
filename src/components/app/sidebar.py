import flet as ft
from src.config import AppConfig


def create_sidebar(on_select):
    """Crea la barra de navegación lateral con indicador de selección vertical."""
    return ft.Container(
        content = ft.NavigationRail(
            selected_index = 0,
            label_type = ft.NavigationRailLabelType.ALL,
            bgcolor = AppConfig.COLORS["bbva_core_blue"],
            indicator_color = AppConfig.COLORS["bbva_sky_light_blue"],
            indicator_shape = ft.RoundedRectangleBorder(radius=0),
            selected_label_text_style = ft.TextStyle(
                color=AppConfig.COLORS["bbva_sky_light_blue"], 
                size=AppConfig.TEXT_STYLES["body"]["size"], 
                weight=AppConfig.TEXT_STYLES["body"]["weight"], 
                font_family=AppConfig.TEXT_STYLES["body"]["font_family"]
            ),
            unselected_label_text_style = ft.TextStyle(
                color=AppConfig.COLORS["bbva_medium_blue"], 
                size=AppConfig.TEXT_STYLES["caption"]["size"], 
                weight=AppConfig.TEXT_STYLES["caption"]["weight"], 
                font_family=AppConfig.TEXT_STYLES["caption"]["font_family"]
            ),
            destinations = [
                ft.NavigationRailDestination(
                    icon_content = ft.Image(src=AppConfig.ICONS["home"], width=20, fit=ft.ImageFit.CONTAIN),
                    label = "Inicio",
                ),
                ft.NavigationRailDestination(
                    icon_content = ft.Image(src=AppConfig.ICONS["dollar"], width=20, fit=ft.ImageFit.CONTAIN),
                    label = "Pagos",
                ),
                ft.NavigationRailDestination(
                    icon_content = ft.Image(src=AppConfig.ICONS["graphics"], width=20, fit=ft.ImageFit.CONTAIN),
                    label = "Dashboard",
                ),
            ],
            on_change = on_select,
        ),
        margin = ft.margin.only(right=-10),
        width = 100,
    )
