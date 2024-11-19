import flet as ft
from src.config import AppConfig


def create_navrail(on_select):
    """Crea la barra de navegación lateral."""
    return ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        bgcolor=AppConfig.COLORS["bbva_core_light_blue"],
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Image(src=AppConfig.ICONS["home"], width=24),
                label="Inicio",
            ),
            ft.NavigationRailDestination(
                icon=ft.Image(src=AppConfig.ICONS["process"], width=24),
                label="Proceso 1",
            ),
            ft.NavigationRailDestination(
                icon=ft.Image(src=AppConfig.ICONS["process"], width=24),
                label="Proceso 2",
            ),
        ],
        on_change=on_select,
    )
