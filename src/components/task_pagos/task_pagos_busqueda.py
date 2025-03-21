import flet as ft
from src.tasks.pagos.task_pagos import TaskPagos
from src.components.components import button, text, image

class ContentTaskPagosBusqueda(ft.Container):
    def __init__(self):
        super().__init__()
        self.task_pagos = TaskPagos()
        
        # Crear los inputs
        self.cc_input = ft.TextField(
            label="Código Central",
            max_length=8,
            keyboard_type=ft.KeyboardType.NUMBER,
            width=200
        )
        
        self.contrato_input = ft.TextField(
            label="Contrato",
            max_length=18,
            keyboard_type=ft.KeyboardType.NUMBER,
            width=200
        )
        
        # Crear el botón de búsqueda
        self.buscar_button = button("Buscar", on_click=self.on_buscar_click)
        send_email_button = button(image("send"), on_click=None, width=50, bgcolor=None)
        send_email_status = ft.Container(content=image("more"))
        
        # Crear la tabla vacía
        self.result_table = ft.DataTable(
            columns=[
                ft.DataColumn(label=text("Código Central")),
                ft.DataColumn(label=text("Contrato")),
                # Añadir más columnas si es necesario
            ],
            rows=[]
        )
        
        # Organizar los inputs, botón y tabla en un Column
        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.cc_input,
                        self.contrato_input,
                        self.buscar_button
                    ],
                    spacing=10
                ),
                self.result_table
            ],
            spacing=20
        )
    
    def on_buscar_click(self, e):
        # Obtener los valores de los inputs
        codigo_central = self.cc_input.value
        contrato = self.contrato_input.value
        
        # Realizar la búsqueda en la base de datos o en la lógica de negocio
        resultados = self.task_pagos.buscar(codigo_central, contrato)
        
        # Limpiar las filas de la tabla
        self.result_table.rows.clear()
        
        # Añadir las filas de los resultados a la tabla
        for resultado in resultados:
            self.result_table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(text(resultado["codigo_central"])),
                        ft.DataCell(text(resultado["contrato"])),
                        # Añadir más celdas si es necesario
                    ]
                )
            )
        
        # Actualizar la tabla
        self.result_table.update()

# Crear una instancia de la clase para renderizar el contenido
content_task_pagos_busqueda = ContentTaskPagosBusqueda()