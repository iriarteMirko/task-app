import flet as ft

class DashboardComponent:
    def __init__(self, page):
        self.page = page
    
    def render(self):
        return ft.Column(
            controls=[
                ft.Text(value="Bienvenido a Task App", size=24, weight="bold"),
                ft.Text(value="Seleccione un proceso para ejecutar:", size=18),
                ft.ElevatedButton(text="Proceso 1", on_click=self.run_process_1),
                ft.ElevatedButton(text="Proceso 2", on_click=self.run_process_2),
            ]
        )
    
    def run_process_1(self, e):
        print("Ejecutando Proceso 1")
    
    def run_process_2(self, e):
        print("Ejecutando Proceso 2")
