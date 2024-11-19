from src.utils.multiproducto import CorreoMultiproducto
from src.utils.utils import (
    get_date, 
    get_last_date_pagos, 
    get_or_create_folder, 
    get_hour_am_pm, 
    clean_columns, 
    start_file, 
    format_excel
)
import pandas as pd
import numpy as np
import warnings


warnings.filterwarnings('ignore')


class Instruccion_Pagos():
    def __init__(self):
        self.mes_año, self.fecha = get_date()
        self.last_date = get_last_date_pagos(f'input/pagos/{self.fecha}')
        self.folder_path = get_or_create_folder('files', pagos=True)
        self.hora = get_hour_am_pm()
        self.flag_reactiva = True
        self.sender = CorreoMultiproducto(self.fecha, self.folder_path, self.hora, self.flag_reactiva).enviar_correo()