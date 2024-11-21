import flet as ft
from src.components.components import row_image_text, text


class Exit:
    def __init__(self, page: ft.Page):
        self.page = page
    
    def destroy_app(self):
        """Muestra un cuadro de diálogo de confirmación para cerrar la aplicación."""
        def close_app(e):
            self.page.window_close()
        
        def dismiss_dialog(e):
            self.page.dialog.open = False
            self.page.update()
        
        # Crear el cuadro de diálogo
        self.page.dialog = ft.AlertDialog(
            modal = True,
            shape = ft.RoundedRectangleBorder(radius=0),
            title = ft.Container(
                content = row_image_text("Confirmación", "warning", "subtitle", "bbva_medium_blue"),
            ),
            content = text("¿Está seguro de que desea cerrar la aplicación?", "body", "bbva_dark_gray"),
            actions = [
                ft.Row(
                    controls=[
                        ft.TextButton(
                            content = row_image_text("Sí", "right", "bbva_medium_blue", "body"),
                            style = ft.ButtonStyle(
                                shape = ft.RoundedRectangleBorder(radius=0),
                                padding = ft.padding.only(left=20, right=20, top=20, bottom=20),
                            ),
                            on_click = close_app
                        ),
                        ft.TextButton(
                            content = row_image_text("No", "wrong", "bbva_medium_blue", "body"),
                            style = ft.ButtonStyle(
                                shape = ft.RoundedRectangleBorder(radius=0),
                                padding = ft.padding.only(left=20, right=20, top=20, bottom=20),
                            ),
                            on_click = dismiss_dialog
                        ),
                    ],
                    alignment = "center",
                    spacing = 20,
                )
            ],
            actions_alignment = "center",
        )
        
        # Abrir el cuadro de diálogo
        self.page.dialog.open = True
        self.page.update()
