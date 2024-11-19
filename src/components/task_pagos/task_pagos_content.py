import flet as ft
from src.config import AppConfig
from src.tasks.task_pagos import TaskPagos
from src.components.task_pagos.task_pagos_buttons import create_task_buttons


class ContentTaskPagos(ft.Container):
    def __init__(self):
        super().__init__()
        self.task_pagos = TaskPagos()
        self.content = ft.Column(
            controls=[
                ft.Text(
                    "Instrucción de Pagos",
                    size=AppConfig.TEXT_STYLES["title"]["size"],
                    weight=AppConfig.TEXT_STYLES["title"]["weight"],
                    color=AppConfig.COLORS["bbva_medium_blue"],
                ),
                create_task_buttons(self.task_pagos),
            ],
            alignment=ft.alignment.top_left,
            spacing=10,
        )
        self.bgcolor = AppConfig.COLORS["bbva_navy"]
        self.alignment = ft.alignment.top_left
        self.expand = True