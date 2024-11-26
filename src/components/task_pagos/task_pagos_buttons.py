import flet as ft
from src.tasks.task_pagos import TaskPagos
from src.components.components import button, text, image


def create_task_buttons(task_pagos: TaskPagos):
    get_asignacion_status = ft.Container(content=image("more"))
    get_pagos_status = ft.Container(content=image("more"))
    step_1_status = ft.Container(content=image("more"))
    send_email_status = ft.Container(content=image("more"))
    step_2_status = ft.Container(content=image("more"))
    
    def on_get_asignacion_click(e):
        task_pagos.get_base_asignacion()
        get_asignacion_status.content = image("check")
        get_asignacion_status.update()
    
    def on_get_pagos_click(e):
        task_pagos.get_base_pagos()
        get_pagos_status.content = image("check")
        get_pagos_status.update()
    
    def on_step_1_click(e):
        task_pagos.execute_step_1()
        step_1_status.content = image("check")
        step_1_status.update()
    
    def on_send_email_click(e):
        task_pagos.send_email()
        send_email_status.content = image("check")
        send_email_status.update()
    
    def on_step_2_click(e):
        task_pagos.execute_step_2()
        step_2_status.content = image("check")
        step_2_status.update()
    
    return ft.Column(
        [
            ft.Row(
                controls = [
                    button("Cargar Base de Asignación", on_get_asignacion_click),
                    get_asignacion_status,
                ],
                spacing = 10,
            ),
            ft.Row(
                controls = [
                    button("Cargar Base de Pagos", on_get_pagos_click),
                    get_pagos_status,
                ],
                spacing = 10,
            ),
            ft.Row(
                controls = [
                    button("Paso 1", on_step_1_click),
                    step_1_status,
                ],
                spacing = 10,
            ),
            ft.Row(
                controls = [
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                image("email"),
                                text("Enviar Correo"),
                                button(image("send"), on_send_email_click, width=50, bgcolor=None),
                            ],
                            alignment="center",
                            spacing=10,
                        ),
                        width = 250,
                        height = 35,
                        padding = ft.padding.symmetric(horizontal=10),
                        border_radius = ft.border_radius.all(0),
                    ),
                    send_email_status,
                ], 
                spacing = 10, 
                alignment = "start",
            ),
            ft.Row(
                controls=[
                    button("Paso 2", on_step_2_click),
                    step_2_status,
                ],
                spacing = 10,
            ),
        ],
        spacing=20,
    )