import flet as ft
from src.config import AppConfig
from src.components.appbar import create_appbar
from src.components.sidebar import create_sidebar
from src.components.content import ContentArea


class TaskApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Task App - BBVA"
        self.page.theme_mode = "light"
        page.padding = 0
        self.page.fonts = AppConfig.FONTS
        self.content_area = ContentArea()
        self.build_ui()
    
    def build_ui(self):
        """Construye la interfaz principal."""
        self.page.appbar = create_appbar(self.page, self.content_area)
        self.page.add(
            ft.Row(
                [
                    create_sidebar(self.sidebar_changed),
                    self.content_area.container,
                ],
                expand=True,
            )
        )
    
    def sidebar_changed(self, e):
        """Gestiona el cambio de selección en la barra lateral."""
        if e.control.selected_index == 0:
            self.content_area.update_content("Bienvenido al inicio")
        elif e.control.selected_index == 1:
            self.content_area.update_content("Contenido del Proceso 1")
        elif e.control.selected_index == 2:
            self.content_area.update_content("Contenido del Proceso 2")
        self.page.update()