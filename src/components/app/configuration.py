import flet as ft
from src.components.components import title, row_image_text


class Configuration:
    def __init__(self, content_area):
        self.content_area = content_area
        self.title = title("Configuración")
        self.dropdown = ft.Dropdown(
            label = "Seleccionar el tema",
            options = [
                ft.dropdown.Option(
                    key = "Claro",
                    content = row_image_text("Claro", "theme_light", "bbva_medium_blue", "body"),
                ),
                ft.dropdown.Option(
                    key = "Oscuro",
                    content = row_image_text("theme_dark", "Oscuro", "bbva_medium_blue", "body"),
                ),
            ],
            value = "Claro" if content_area.container.page.theme_mode == "light" else "Oscuro",
            on_change = self.change_theme,
            width = 250,
        )
        self.container = ft.Container(
            content = ft.Column(
                controls = [
                    ft.Container(
                        content = self.title,
                        alignment = ft.alignment.top_left,
                        padding = ft.padding.only(left=20, right=20, top=20, bottom=10),
                    ),
                    ft.Container(
                        content = self.dropdown,
                        alignment = ft.alignment.top_left,
                        padding = ft.padding.only(left=20, right=20, top=10, bottom=20),
                        width = 250,
                    ),
                ],
                alignment = ft.alignment.top_left,
            ),
            expand = True,
            alignment = ft.alignment.top_left,
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
