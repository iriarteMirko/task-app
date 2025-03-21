import flet as ft
from src.tasks.pagos.task_pagos import TaskPagos
from src.components.components import button, text, image


def create_task_buttons(task_pagos: TaskPagos):
    # Crear referencias para los botones y sus estados
    get_asignacion_button = button("Cargar Base de Asignación", on_click=None)
    get_asignacion_status = ft.Container(content=image("more"))
    
    get_pagos_button = button("Cargar Base de Pagos", on_click=None)
    get_pagos_status = ft.Container(content=image("more"))
    
    step_1_button = button("Paso 1", on_click=None)
    step_1_status = ft.Container(content=image("more"))
    
    send_email_button = button(image("send"), on_click=None, width=50, bgcolor=None)
    send_email_status = ft.Container(content=image("more"))
    
    step_2_button = button("Paso 2", on_click=None)
    step_2_status = ft.Container(content=image("more"))
    
    # Lista de todos los botones
    all_buttons = [
        get_asignacion_button,
        get_pagos_button,
        step_1_button,
        send_email_button,
        step_2_button,
    ]
    
    def disable_buttons():
        """Deshabilita todos los botones y cambia su color."""
        for btn in all_buttons:
            btn.disabled = True
            btn.update()
    
    def enable_buttons():
        """Habilita todos los botones y restaura su color."""
        for btn in all_buttons:
            btn.disabled = False
            btn.update()
    
    # Funciones para los eventos de los botones
    def on_get_asignacion_click(e):
        disable_buttons()
        task_pagos.get_base_asignacion()
        get_asignacion_status.content = image("check")
        get_asignacion_status.update()
        enable_buttons()
    
    def on_get_pagos_click(e):
        disable_buttons()
        task_pagos.get_base_pagos()
        get_pagos_status.content = image("check")
        get_pagos_status.update()
        enable_buttons()
    
    def on_step_1_click(e):
        disable_buttons()
        task_pagos.execute_step_1()
        step_1_status.content = image("check")
        step_1_status.update()
        enable_buttons()
    
    def on_send_email_click(e):
        disable_buttons()
        task_pagos.send_email()
        send_email_status.content = image("check")
        send_email_status.update()
        enable_buttons()
    
    def on_step_2_click(e):
        disable_buttons()
        task_pagos.execute_step_2()
        step_2_status.content = image("check")
        step_2_status.update()
        enable_buttons()
    
    # Asociar las funciones a los botones utilizando on_click
    get_asignacion_button.on_click = on_get_asignacion_click
    get_pagos_button.on_click = on_get_pagos_click
    step_1_button.on_click = on_step_1_click
    send_email_button.on_click = on_send_email_click
    step_2_button.on_click = on_step_2_click
    
    return ft.Column(
        [
            ft.Row([get_asignacion_button, get_asignacion_status], spacing=10),
            ft.Row([get_pagos_button, get_pagos_status], spacing=10),
            ft.Row([step_1_button, step_1_status], spacing=10),
            ft.Row(
                [
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                image("email"),
                                text("Enviar Correo"),
                                send_email_button,
                            ],
                            alignment="center",
                            spacing=10,
                        ),
                        width=250,
                        height=35,
                        padding=ft.padding.symmetric(horizontal=10),
                        border_radius=ft.border_radius.all(0),
                    ),
                    send_email_status,
                ],
                spacing=10,
                alignment="start",
            ),
            ft.Row([step_2_button, step_2_status], spacing=10),
        ],
        spacing=20,
    )