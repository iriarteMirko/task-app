import flet as ft
from src.config import AppConfig
from src.components.content import ContentArea


class Destroy:
    def __init__(self, content_area: ContentArea):
        self.content_area = content_area
        self.container = ft.Container(
            content=ft.Text(
                "Cerrar App",
                size=AppConfig.TEXT_STYLES["title"]["size"],
                weight=AppConfig.FONT_FAMILY["bold"],
                color=AppConfig.COLORS["bbva_medium_blue"],
            ),
        )
    
    def load_destroy(self):
        """Carga el contenido de la sección 'Destroy App' en el área dinámica."""
        self.content_area.container.content = self.container
        self.content_area.container.update()
