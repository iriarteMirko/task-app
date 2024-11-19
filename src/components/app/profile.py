import flet as ft
from src.config import AppConfig
from src.components.app.content import ContentArea


class Profile:
    def __init__(self, content_area: ContentArea):
        self.content_area = content_area
        self.container = ft.Container(
            content=ft.Text(
                "Bienvenido al Perfil",
                size=AppConfig.TEXT_STYLES["title"]["size"],
                weight=AppConfig.FONT_FAMILY["bold"],
                color=AppConfig.COLORS["bbva_medium_blue"],
            ),
        )
    
    def load_profile(self):
        """Carga el contenido de la sección 'Perfil' en el área dinámica."""
        self.content_area.container.content = self.container
        self.content_area.container.update()
