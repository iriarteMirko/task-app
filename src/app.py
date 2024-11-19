import flet as ft
from src.config import AppConfig
from src.components.app.appbar import create_appbar
from src.components.app.sidebar import create_sidebar
from src.components.app.content import ContentArea
from src.components.task_pagos.task_pagos_content import ContentTaskPagos


class TaskApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Task App - BBVA"
        self.page.theme_mode = "light"
        self.page.padding = 0
        self.page.fonts = AppConfig.FONTS
        self.content_area = ContentArea()
        self.task_pagos_content = ContentTaskPagos()
        self.build_ui()
    
    def build_ui(self):
        """Construye la interfaz principal."""
        self.page.appbar = create_appbar(self.content_area)
        self.page.add(
            ft.Row(
                [create_sidebar(self.sidebar_changed), self.content_area.container],
                expand=True,
            )
        )
    
    def sidebar_changed(self, e):
        """Gestiona el cambio de selección en la barra lateral."""
        content_mapping = {
            0: lambda: self.content_area.update_content(),
            1: lambda: self.content_area.update_content(self.task_pagos_content),
            2: lambda: self.content_area.update_content(),
        }
        content_mapping.get(e.control.selected_index, lambda: None)()
        self.page.update()