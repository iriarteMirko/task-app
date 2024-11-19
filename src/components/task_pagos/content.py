import flet as ft
from src.tasks.task_pagos import TaskPagos
from src.components.task_pagos.buttons import create_task_buttons

class ContentTaskPagos(ft.Container):
    def __init__(self):
        super().__init__()
        self.task_pagos = TaskPagos()
    
    def render(self):
        self.content = create_task_buttons(self.task_pagos)
        self.update()