import flet as ft
from src.tasks.pagos.task_pagos import TaskPagos
from src.components.components import title, separator
from src.components.task_pagos.task_pagos_buttons import create_task_buttons
from src.components.task_pagos.task_pagos_busqueda import ContentTaskPagosBusqueda


class ContentTaskPagos(ft.Container):
    def __init__(self):
        super().__init__()
        self.task_pagos = TaskPagos()
        self.title = title("Instrucción de Pagos")
        self.separator = separator()
        self.buttons = create_task_buttons(self.task_pagos)
        self.busqueda = ContentTaskPagosBusqueda()
        self.content = ft.Column(
            controls = [
                self.title,
                self.separator,
                self.buttons,
                self.busqueda.content,
            ],
            spacing = 20,
        )
