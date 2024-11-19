import flet as ft
from src.config import AppConfig
from src.components.app.content import ContentArea


class Configuration:
    def __init__(self, content_area: ContentArea):
        self.content_area = content_area
        # Crear el título
        self.title = ft.Text(
            "Configuración",
            size=AppConfig.TEXT_STYLES["title"]["size"],
            weight=AppConfig.TEXT_STYLES["title"]["weight"],
            color=AppConfig.COLORS["bbva_medium_blue"],
        )
        # Crear el Dropdown con opciones personalizadas
        self.dropdown = ft.Dropdown(
            label="Seleccionar el tema",
            options=[
                ft.dropdown.Option(
                    key="Claro",
                    content=ft.Row(
                        controls=[
                            ft.Image(src=AppConfig.ICONS["theme_light"], width=20, fit=ft.ImageFit.CONTAIN),
                            ft.Text("Claro", size=14, color=AppConfig.COLORS["bbva_medium_blue"],),
                        ],
                        spacing=10,
                        alignment="start",
                    ),
                ),
                ft.dropdown.Option(
                    key="Oscuro",
                    content=ft.Row(
                        controls=[
                            ft.Image(src=AppConfig.ICONS["theme_dark"], width=20, fit=ft.ImageFit.CONTAIN),
                            ft.Text("Oscuro", size=14, color=AppConfig.COLORS["bbva_medium_blue"]),
                        ],
                        spacing=10,
                        alignment="start",
                    ),
                ),
            ],
            value="Claro" if content_area.container.page.theme_mode == "light" else "Oscuro",
            on_change=self.change_theme,
            width=250,
        )
        # Contenedor principal
        self.container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=self.title,
                        alignment=ft.alignment.top_left,
                        padding=ft.padding.only(left=20, right=20, top=20, bottom=10),
                    ),
                    ft.Container(
                        content=self.dropdown,
                        alignment=ft.alignment.top_left,
                        padding=ft.padding.only(left=20, right=20, top=10, bottom=20),
                        width=250,
                    ),
                ],
                alignment=ft.alignment.top_left,
            ),
            expand=True,
            alignment=ft.alignment.top_left,
        )
    
    def change_theme(self, e):
        """Cambia el tema de la aplicación y actualiza la selección."""
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
