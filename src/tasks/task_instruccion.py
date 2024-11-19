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
import os


warnings.filterwarnings('ignore')


class Instruccion_Pagos():
    def __init__(self):
        self.mes_año, self.fecha = get_date()
        self.last_date = get_last_date_pagos(f'input/pagos/{self.fecha}')
        self.folder_path = get_or_create_folder('files', pagos=True)
        self.hora = get_hour_am_pm()
        self.base_pagos_path = f'input/pagos/{self.fecha}/Base Pagos {self.last_date}.xlsx'
        self.asignacion_path = f'input/asignacion/{self.fecha}/base_asignacion_{self.mes_año}.xlsx'
        
        self.monoproducto = f'{self.folder_path}/MONOPRODUCTO_{self.last_date}.xlsx'
        self.multiproducto = f'{self.folder_path}/MULTIPRODUCTO_{self.last_date}.xlsx'
        self.reactiva = f'{self.folder_path}/REACTIVA_{self.last_date}.xlsx'
        self.no_enviados = f'{self.folder_path}/NO_ENVIADOS_{self.last_date}.xlsx'
        self.enviados = f'{self.folder_path}/ENVIADOS_{self.last_date}.xlsx'
        
        self.mono_path = os.path.abspath(self.monoproducto)
        self.multi_path = os.path.abspath(self.multiproducto)
        self.react_path = os.path.abspath(self.reactiva)
        self.no_enviados_path = os.path.abspath(self.no_enviados)
        self.enviados_path = os.path.abspath(self.enviados)
        
        
        self.flag_reactiva = True
        self.sender = CorreoMultiproducto(self.fecha, self.folder_path, self.hora, self.flag_reactiva).enviar_correo()
    
    def load_pagos(self):
        df_base = pd.read_excel(self.base_pagos_path)
        
        fecha_formateada = pd.to_datetime('today').strftime('%d-%b')
        fecha_formateada = fecha_formateada[:3] + fecha_formateada[3:].capitalize()
        
        df_base['FECHA_ENVIO'] = fecha_formateada.replace('.', '')
        df_base['ID_RESPONSABLE'] = 'MIV'
        
        cols_base = ['FECHA', 'CODCEN', 'CLAVSERV', 'CENTROPAGO', 'IMPORTE', 'MONEDA', 'NOMBRE', 'FECHA_ENVIO', 'ID_RESPONSABLE']
        df_base = df_base[cols_base]
        df_base.rename(columns={'CODCEN': 'CC'}, inplace=True)
        
        df_base['CC'] = df_base['CC'].astype('Int64').astype(str).str.zfill(8)
        df_base['CC'] = df_base['CC'].str.replace(' ', '').str.replace(r'\D', '', regex=True).str[-8:]
        df_base['CC'] = df_base['CC'].str.zfill(8)
        
        df_base['CLAVSERV'] = df_base['CLAVSERV'].astype(str).str.zfill(4)
        df_base['CENTROPAGO'] = df_base['CENTROPAGO'].astype(str).str.zfill(4)
    
    def load_agencias():
        pass