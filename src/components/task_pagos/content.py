import flet as ft
from src.tasks.task_pagos import TaskPagos
from src.components.task_pagos.buttons import create_task_buttons

class ContentTaskPagos(ft.Container):
    def __init__(self):
        super().__init__()
        self.task_pagos = TaskPagos()
        self.content = ft.Column(
            [
                ft.Text("Task Pagos",size=20,),
                create_task_buttons(self.task_pagos),
            ],
            spacing=10,
        )
        self.expand = True
        self.alignment = ft.alignment.center