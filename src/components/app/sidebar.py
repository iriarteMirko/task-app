import flet as ft
from src.config import AppConfig


def create_sidebar(on_select):
    """Crea la barra de navegación lateral con indicador de selección vertical."""
    return ft.Container(
        content=ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            bgcolor=AppConfig.COLORS["bbva_core_blue"],
            indicator_color=AppConfig.COLORS["bbva_sky_light_blue"],
            indicator_shape=ft.RoundedRectangleBorder(radius=0),
            selected_label_text_style=ft.TextStyle(color=AppConfig.COLORS["bbva_sky_light_blue"],size=14, font_family=AppConfig.FONT_FAMILY["bold"]),
            unselected_label_text_style=ft.TextStyle(color=AppConfig.COLORS["bbva_medium_blue"],size=12, font_family=AppConfig.FONT_FAMILY["regular"]),
            destinations=[
                ft.NavigationRailDestination(
                    icon_content=ft.Image(src=AppConfig.ICONS["home"], width=20, fit=ft.ImageFit.CONTAIN),
                    label="Inicio",
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Image(src=AppConfig.ICONS["process"], width=20, fit=ft.ImageFit.CONTAIN),
                    label="Instrucción de Pagos",
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Image(src=AppConfig.ICONS["process"], width=20, fit=ft.ImageFit.CONTAIN),
                    label="Proceso 2",
                ),
            ],
            on_change=on_select,
        ),
        margin=ft.margin.only(right=-10),
    )
