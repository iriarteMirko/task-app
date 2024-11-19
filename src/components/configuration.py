import flet as ft
from src.config import AppConfig
from src.components.content import ContentArea


class Configuration:
    def __init__(self, content_area: ContentArea):
        self.content_area = content_area
        self.dropdown = ft.Dropdown(
            label="Selecciona el tema",
            options=[
                ft.dropdown.Option("Claro"),
                ft.dropdown.Option("Oscuro"),
            ],
            value="Claro",  # Tema por defecto
            on_change=self.change_theme,
        )
        self.container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Configuración",
                        size=AppConfig.TEXT_STYLES["title"]["size"],
                        weight=AppConfig.FONT_FAMILY["bold"],
                        color=AppConfig.COLORS["bbva_medium_blue"],
                    ),
                    self.dropdown,
                ],
                spacing=20,
            ),
            expand=True,
            bgcolor=AppConfig.COLORS["bbva_white"],
            alignment=ft.alignment.center,
        )
    
    def change_theme(self, e):
        """Cambia el tema de la aplicación."""
        selected_theme = e.control.value
        if selected_theme == "Claro":
            self.content_area.container.page.theme_mode = "light"
        elif selected_theme == "Oscuro":
            self.content_area.container.page.theme_mode = "dark"
        self.content_area.container.page.update()
    
    def load_configuration(self):
        """Carga el contenido de la sección 'Configuración' en el área dinámica."""
        self.content_area.container.content = self.container
        self.content_area.container.update()
