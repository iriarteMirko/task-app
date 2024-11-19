import flet as ft

def create_task_buttons(task_instance):
    def on_load_bases_click(e):
        task_instance.load_bases()
    
    def on_subproccess_1_click(e):
        task_instance.subproccess_1()
    
    def on_send_email_click(e):
        task_instance.send_email()
    
    def on_subproccess_2_click(e):
        task_instance.subproccess_2()
    
    return ft.Column(
        [
            ft.ElevatedButton("Cargar Bases", on_click=on_load_bases_click),
            ft.ElevatedButton("Ejecutar Paso 1", on_click=on_subproccess_1_click),
            ft.ElevatedButton("Enviar Correo", on_click=on_send_email_click),
            ft.ElevatedButton("Ejecutar Paso 2", on_click=on_subproccess_2_click),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )
