import flet as ft
from src.tasks.task_pagos import TaskPagos
from src.components.components import button


def create_task_buttons(task_pagos: TaskPagos):
    def on_load_bases_click(e):
        task_pagos.load_bases()
    
    def on_subproccess_1_click(e):
        task_pagos.subproccess_1()
    
    def on_send_email_click(e):
        task_pagos.send_email()
    
    def on_subproccess_2_click(e):
        task_pagos.subproccess_2()
    
    return ft.Column(
        [
            button("Cargar Bases", on_load_bases_click),
            button("Paso 1", on_subproccess_1_click),
            button("Enviar Correo", on_send_email_click),
            button("Paso 2", on_subproccess_2_click),
        ],
        spacing = 10,
    )
