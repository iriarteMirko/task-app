import flet as ft
from src.config import AppConfig
from src.tasks.task_pagos import TaskPagos


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
            ft.ElevatedButton("Cargar Bases", on_click=on_load_bases_click ,),
            ft.ElevatedButton("Ejecutar Paso 1", on_click=on_subproccess_1_click),
            ft.ElevatedButton("Enviar Correo", on_click=on_send_email_click),
            ft.ElevatedButton("Ejecutar Paso 2", on_click=on_subproccess_2_click),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )
