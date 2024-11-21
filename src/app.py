import flet as ft
from src.config import AppConfig
from src.components.components import text, image, title, button, separator
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
        self.dynamic_contents = {
            "task_pagos_content": ContentTaskPagos()
        }
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
            0: lambda: self.content_area.update_content(self.create_home_content()),
            1: lambda: self.content_area.update_content(self.dynamic_contents["task_pagos_content"]),
            2: lambda: self.content_area.update_content(),
        }
        content_mapping.get(e.control.selected_index, lambda: None)()
        self.page.update()
    
    def update_all_contents(self, e):
        """Actualiza todas las instancias dinámicas."""
        self.dynamic_contents["task_pagos_content"] = ContentTaskPagos()
        # Agregar
        self.page.update()
    
    def create_home_content(self):
        """Crea el contenido de la pestaña Inicio con el botón Actualizar."""
        return ft.Column(
            controls=[
                title("Inicio", "home", "bbva_aqua"),
                separator(),
                ft.Row(
                    controls=[
                        image("bullet_subtitle"),
                        text("Actualizar"),
                        button(image("update"), self.update_all_contents, width=50, bgcolor=None),
                    ],
                    alignment = "start",
                    spacing = 10,
                ),
            ],
            spacing = 20,
            alignment = "start",
        )
