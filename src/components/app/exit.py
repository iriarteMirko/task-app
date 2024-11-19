import flet as ft
from src.config import AppConfig


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
            modal=True,
            shape=ft.RoundedRectangleBorder(radius=0),
            title=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Image(src=AppConfig.ICONS["warning"], width=20, fit=ft.ImageFit.CONTAIN),
                        ft.Text("Confirmar Cierre", size=20, weight="bold", color=AppConfig.COLORS["bbva_medium_blue"]),
                    ],
                    spacing=10,
                ),
            ),
            content=ft.Text(
                "¿Está seguro de que desea cerrar la aplicación?",
                size=AppConfig.TEXT_STYLES["body"]["size"],
                weight=AppConfig.TEXT_STYLES["body"]["weight"],
                color=AppConfig.COLORS["bbva_dark_gray"],
            ),
            actions=[
                ft.Row(
                    controls=[
                        ft.TextButton(
                            content=ft.Row(
                                controls=[
                                    ft.Image(src=AppConfig.ICONS["right"], width=20, fit=ft.ImageFit.CONTAIN),
                                    ft.Text("Sí", size=AppConfig.TEXT_STYLES["body"]["size"], color=AppConfig.COLORS["bbva_medium_blue"]),
                                ],
                                spacing=10,
                            ),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=0),
                                padding=ft.padding.only(left=20, right=20, top=20, bottom=20),
                            ),
                            on_click=close_app
                        ),
                        ft.TextButton(
                            content=ft.Row(
                                controls=[
                                    ft.Image(src=AppConfig.ICONS["wrong"], width=20, fit=ft.ImageFit.CONTAIN),
                                    ft.Text("No", size=AppConfig.TEXT_STYLES["body"]["size"], color=AppConfig.COLORS["bbva_medium_blue"]),
                                ],
                                spacing=10,
                            ),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=0),
                                padding=ft.padding.only(left=20, right=20, top=20, bottom=20),
                            ),
                            on_click=dismiss_dialog
                        ),
                    ],
                    alignment="center",
                    spacing=20,
                )
            ],
            actions_alignment="center",
        )
        
        # Abrir el cuadro de diálogo
        self.page.dialog.open = True
        self.page.update()
