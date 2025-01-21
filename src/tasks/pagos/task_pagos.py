from src.utils.multiproducto import CorreoMultiproducto
from src.utils.utils import (
    get_date, 
    get_or_create_task_path, 
    get_last_date_pagos, 
    get_or_create_folder, 
    get_hour_am_pm, 
    start_file, 
    format_excel
)
import pandas as pd
import numpy as np
import warnings
import os


warnings.filterwarnings('ignore')


class TaskPagos():
    def __init__(self):
        print("\n-------------------------------------------------")
        print("Inicializando...\n")
        self.mes_año, self.fecha = get_date()
        self.input_folder, self.output_folder = get_or_create_task_path('pagos')
        self.input_folder_asignacion, _ = get_or_create_task_path('asignacion')
        self.folder_path = get_or_create_folder(self.output_folder)
        self.last_date = get_last_date_pagos(self.input_folder)
        self.hora = get_hour_am_pm()
        
        self.base_pagos_path = f'{self.input_folder}\\Base Pagos {self.last_date}.xlsx'
        self.asignacion_path = f'{self.input_folder_asignacion}\\base_asignacion_{self.mes_año}.txt'
        print(self.base_pagos_path)
        print(self.asignacion_path)
        print("\n")
        print(self.folder_path)
        print(self.hora)
        print("\n")
        
        self.monoproducto = f'{self.folder_path}\\MONOPRODUCTO_{self.last_date}.xlsx'
        self.multiproducto = f'{self.folder_path}\\MULTIPRODUCTO_{self.last_date}.xlsx'
        self.reactiva = f'{self.folder_path}\\REACTIVA_{self.last_date}.xlsx'
        self.no_enviados = f'{self.folder_path}\\NO_ENVIADOS_{self.last_date}.xlsx'
        self.enviados = f'{self.folder_path}\\ENVIADOS_{self.last_date}.xlsx'
        
        self.mono_path = os.path.abspath(self.monoproducto)
        self.multi_path = os.path.abspath(self.multiproducto)
        self.reactiva_path = os.path.abspath(self.reactiva)
        self.no_enviados_path = os.path.abspath(self.no_enviados)
        self.enviados_path = os.path.abspath(self.enviados)
        
        self.fondos_gobierno = ['REACTIVA', 'CRECER', 'FAE']
    
    def get_base_pagos(self):
        print("\n-------------------------------------------------")
        print("Cargando base de pagos...")
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
        
        self.df_base = df_base
        print(df_base['FECHA'][0])
        print(df_base.shape)
        print("\nCarga completada")
    
    def get_base_asignacion(self):
        print("\n-------------------------------------------------")
        print("Cargando base de asignación...")
        df_asignacion = pd.read_csv(self.asignacion_path, sep='|', encoding='utf-8')
        cols_asignacion = ['CC', 'CONTRATO', 'NOMBRE_CLIENTE', 'TIPO_CARTERA', 'TIPO_FONDO', 'CARTERA', 'AGENCIA', 'FLAG']
        df_asignacion = df_asignacion[cols_asignacion]
        
        df_asignacion['CC'] = df_asignacion['CC'].astype('Int64').astype(str).str.zfill(8)
        df_asignacion['CONTRATO'] = df_asignacion['CONTRATO'].astype('Int64').astype(str).str.zfill(18)
        
        self.df_asignacion = df_asignacion
        print(df_asignacion.shape)
        print("\nCarga completada")
    
    def get_backups(self):
        self.df_base_backup = self.df_base.copy()
        self.df_asignacion_backup = self.df_asignacion.copy()
        self.base_count = self.df_base_backup.shape[0]
    
    def merge_dataframes(self):
        def actualizar_tipo_cartera(df: pd.DataFrame) -> pd.DataFrame:
            df['TIPO_CARTERA'] = np.where(
                df['TIPO_CARTERA'].eq('UNSECURED').any(), 'UNSECURED',
                np.where(
                    ~df['TIPO_CARTERA'].eq('NULL').any(), 'SECURED', 
                    np.where(
                        ~df['TIPO_CARTERA'].eq('SECURED').any(), 'NULL', 'SECURED/NULL'
                    )
                )
            )
            return df
        
        self.df_base_backup = self.df_base_backup.merge(self.df_asignacion_backup, on='CC', how='left')
        self.df_base_backup.sort_values(by=['CC', 'TIPO_CARTERA'], ascending=[True, False], inplace=True)
        
        filtro = (self.df_base_backup['FLAG'] != 1) & (self.df_base_backup['FLAG'].notna())
        df_base_filtro = self.df_base_backup.loc[filtro].groupby('CC').apply(actualizar_tipo_cartera).reset_index(drop=True)
        
        self.df_base_backup = self.df_base_backup.merge(df_base_filtro[['CC', 'TIPO_CARTERA']], on='CC', how='left', suffixes=('', '_y'))
        self.df_base_backup['TIPO_CARTERA_FINAL'] = self.df_base_backup['TIPO_CARTERA_y'].fillna(self.df_base_backup['TIPO_CARTERA'])
        
        self.df_base_backup.drop(columns=['TIPO_CARTERA', 'TIPO_CARTERA_y'], inplace=True)
        self.df_base_backup.rename(columns={'TIPO_CARTERA_FINAL': 'TIPO_CARTERA'}, inplace=True)
        self.df_base_backup.drop_duplicates(subset=['CC', 'IMPORTE', 'MONEDA', 'NOMBRE'], keep='first', inplace=True)
        
        self.df_base_backup['TIPO_CARTERA'].fillna('NULL', inplace=True)
        self.df_base_backup['TIPO_FONDO'].fillna('NULL', inplace=True)
        
        self.df_base_backup['FLAG'] = self.df_base_backup['FLAG'].astype('Int64')
        self.df_base_backup['CONTRATO'] = self.df_base_backup['CONTRATO'].apply(lambda x: str(int(x)).zfill(18) if pd.notna(x) else x)
        
        cols_base = ['FECHA', 'CC', 'CLAVSERV', 'CENTROPAGO', 'IMPORTE', 'MONEDA', 'NOMBRE', 'FLAG', 'CONTRATO', 
            'TIPO_FONDO', 'CARTERA', 'NOMBRE_CLIENTE', 'FECHA_ENVIO', 'ID_RESPONSABLE', 'TIPO_CARTERA', 'AGENCIA']
        self.df_base_backup = self.df_base_backup[cols_base]
    
    def get_no_encontrados(self):
        self.df_base_ne = self.df_base_backup[self.df_base_backup['FLAG'].isnull()]
        self.ne_count = self.df_base_ne.shape[0]
    
    def get_monoproducto(self):
        self.df_mono = self.df_base_backup[self.df_base_backup['FLAG'] == 1]
        
        self.df_mono_final = self.df_mono[
            (self.df_mono['TIPO_CARTERA'] == 'UNSECURED') & 
            (~self.df_mono['TIPO_FONDO'].isin(self.fondos_gobierno))
        ]
        
        cols_mono = ['FECHA', 'CC', 'CLAVSERV', 'CENTROPAGO', 'IMPORTE', 'MONEDA', 'NOMBRE', 'FLAG', 'CONTRATO', 
            'TIPO_FONDO', 'CARTERA', 'NOMBRE_CLIENTE', 'FECHA_ENVIO', 'ID_RESPONSABLE', 'TIPO_CARTERA', 'AGENCIA']
        self.df_mono_final = self.df_mono_final[cols_mono]
        
        self.df_mono_final.sort_values(by=['FECHA', 'CC'], inplace=True)
        self.df_mono_final.reset_index(drop=True, inplace=True)
        self.df_mono_final.to_excel(self.monoproducto, index=False)
        self.mono_count = self.df_mono_final.shape[0]
        
        print('Base Bagos: ', self.df_base.shape)
        print('-------------------------------------------------')
        print('Monoproducto:', self.df_mono_final.shape)
        print('Importe Monoproducto:', round(self.df_mono_final['IMPORTE'].sum(), 2),'\n')
    
    def get_monoproducto_reactiva(self):
        self.df_reactiva = self.df_mono[
            (self.df_mono['TIPO_CARTERA'] == 'UNSECURED') & 
            (self.df_mono['TIPO_FONDO'].isin(self.fondos_gobierno))
        ]
        
        self.df_reactiva['TIPO_PAGO'] = None
        
        cols_reactiva = ['FECHA', 'CC', 'CLAVSERV', 'CENTROPAGO', 'IMPORTE', 'MONEDA', 'NOMBRE', 
            'FLAG', 'CONTRATO', 'TIPO_FONDO', 'CARTERA', 'TIPO_PAGO', 'FECHA_ENVIO', 'ID_RESPONSABLE', 'AGENCIA']
        self.df_reactiva = self.df_reactiva[cols_reactiva]
        
        self.df_reactiva.sort_values(by=['FECHA', 'CONTRATO'], inplace=True)
        self.df_reactiva.reset_index(drop=True, inplace=True)
        self.df_reactiva.to_excel(self.reactiva, index=False)
        self.reactiva_count = self.df_reactiva.shape[0]
    
    def get_monoproducto_no_enviados(self):
        self.df_mono_no_enviado = self.df_mono[(self.df_mono['TIPO_CARTERA'] != 'UNSECURED')]
        self.mono_no_enviado_count = self.df_mono_no_enviado.shape[0]
    
    def get_multiproducto(self):
        self.df_multi = self.df_base_backup[self.df_base_backup['FLAG'] > 1]
        self.multi_count = self.df_multi.shape[0]
        
        self.df_multi_final = self.df_multi[self.df_multi['TIPO_CARTERA'] == 'UNSECURED']
        
        self.df_multi_final['CONTRATO'] = None
        self.df_multi_final['TIPO_FONDO'] = None
        self.df_multi_final['CARTERA'] = None
        self.df_multi_final['TIPO_PAGO'] = None
        
        cols_multi = ['FECHA', 'CC', 'CLAVSERV', 'CENTROPAGO', 'IMPORTE', 'MONEDA', 'NOMBRE', 'FLAG', 'CONTRATO', 
            'TIPO_FONDO', 'CARTERA', 'TIPO_PAGO', 'NOMBRE_CLIENTE', 'FECHA_ENVIO', 'ID_RESPONSABLE']
        self.df_multi_final = self.df_multi_final[cols_multi]
        
        self.df_multi_final.drop_duplicates(subset=['CC', 'IMPORTE', 'MONEDA', 'NOMBRE'], inplace=True)
        self.df_multi_final.sort_values(by=['FECHA', 'FLAG', 'CC'], inplace=True)
        self.df_multi_final.reset_index(drop=True, inplace=True)
        self.df_multi_final.to_excel(self.multiproducto, index=False)
        self.multi_count = self.df_multi_final.shape[0]
    
    def get_multiproducto_no_enviados(self):
        self.df_multi_no_enviado = self.df_multi[(self.df_multi['TIPO_CARTERA'] != 'UNSECURED')]
        self.multi_no_enviado_count = self.df_multi_no_enviado.shape[0]
    
    def get_no_enviados(self):
        self.df_no_enviados = pd.concat([self.df_mono_no_enviado, self.df_multi_no_enviado, self.df_base_ne])
        self.df_no_enviados['FLAG'] = self.df_no_enviados['FLAG'].astype('Int64').fillna(0)
        
        self.df_no_enviados['CONTRATO'] = self.df_no_enviados.apply(lambda x: None if x['FLAG'] != 1 else x['CONTRATO'], axis=1)
        self.df_no_enviados['TIPO_FONDO'] = self.df_no_enviados.apply(lambda x: None if x['FLAG'] != 1 else x['TIPO_FONDO'], axis=1)
        self.df_no_enviados['FLAG'] = self.df_no_enviados['FLAG'].apply(lambda x: 'NE' if x == 0 else x)
        self.df_no_enviados.fillna('NULL', inplace=True)
        
        self.df_no_enviados.sort_values(by=['FECHA', 'FLAG', 'CC'], inplace=True)
        self.df_no_enviados.reset_index(drop=True, inplace=True)
        self.df_no_enviados.to_excel(self.no_enviados, index=False)
    
    def get_multiproducto_agencias(self):
        df_1 = pd.read_excel(f'{self.folder_path}/agencias/RJ.xlsx', dtype={'CC': str, 'CONTRATO': str})
        df_2 = pd.read_excel(f'{self.folder_path}/agencias/CLASA.xlsx', dtype={'CC': str, 'CONTRATO': str})
        df_3 = pd.read_excel(f'{self.folder_path}/agencias/MORNESE.xlsx', dtype={'CC': str, 'CONTRATO': str})
        
        cols_multi = ['FECHA', 'CC', 'CLAVSERV', 'CENTROPAGO', 'IMPORTE', 'MONEDA', 'NOMBRE', 'FLAG', 'CONTRATO', 
            'TIPO_FONDO', 'CARTERA', 'TIPO_PAGO', 'NOMBRE_CLIENTE', 'FECHA_ENVIO', 'ID_RESPONSABLE']
        
        df_1 = df_1[cols_multi]
        df_2 = df_2[cols_multi]
        df_3 = df_3[cols_multi]
        
        df_1['AGENCIA'] = 'ASESCOM RJ'
        df_2['AGENCIA'] = 'CLASA MORA'
        df_3['AGENCIA'] = 'MORNESE MORA'
        
        contratos_rj = df_1['CONTRATO'].notna().value_counts()[True]
        contratos_clasa = df_2['CONTRATO'].notna().value_counts()[True]
        contratos_mornese = df_3['CONTRATO'].notna().value_counts()[True]
        print('Contratos RJ:', contratos_rj)
        print('Contratos CLASA:', contratos_clasa)
        print('Contratos MORNESE:', contratos_mornese)
        print('Total:', contratos_rj + contratos_clasa + contratos_mornese)
        print("-------------------------------------------------")
        
        df_agencias = pd.concat([df_1, df_2, df_3])
        df_agencias.dropna(subset=['CONTRATO'], inplace=True)
        df_agencias['CONTRATO'] = df_agencias['CONTRATO'].apply(
            lambda x: str(int(x)).replace(' ', '').zfill(18) 
            if 16 <= len(str(x).replace(' ', '')) <= 18 
            else None)
        df_agencias.dropna(subset=['CONTRATO'], inplace=True)
        df_agencias.reset_index(drop=True, inplace=True)
        
        df_multi = pd.read_excel(self.multi_path, dtype={'CC': str, 'CLAVSERV': str, 'CENTROPAGO': str, 'CONTRATO': str})
        df_multi['AGENCIA'] = 'NULL'
        
        print('Multiproducto Original:', df_multi.shape[0])
        print('Multiproducto Agencias:', df_agencias.shape[0])
        print("-------------------------------------------------")
        
        df_multi_contact = pd.concat([df_multi, df_agencias])
        df_multi_contact['CC'] = df_multi_contact['CC'].astype(str).replace(' ', '').astype('Int64').astype(str).str.zfill(8)
        df_multi_contact.drop(columns=['TIPO_FONDO', 'CARTERA'], inplace=True)
        df_multi_contact.sort_values(by=['CC', 'CONTRATO'], inplace=True)
        df_multi_contact.drop_duplicates(subset=['CC', 'IMPORTE', 'MONEDA', 'NOMBRE'], keep='first', inplace=True)
        df_multi_contact.reset_index(drop=True, inplace=True)
        
        self.df_asignacion_backup['CC'] = self.df_asignacion_backup['CC'].astype('Int64').astype(str).str.zfill(8)
        self.df_asignacion_backup['CONTRATO'] = self.df_asignacion_backup['CONTRATO'].apply(lambda x: str(int(x)).replace(' ', '').zfill(18) if pd.notna(x) else x)
        
        df_multi_final = df_multi_contact.merge(self.df_asignacion_backup, on='CONTRATO', how='left')
        df_multi_final.rename(columns={'CC_x': 'CC'}, inplace=True)
        df_multi_final.drop(columns=['CC_y'], inplace=True)
        
        df_multi_final['CLAVSERV'] = df_multi_final['CLAVSERV'].astype(str).str.zfill(4)
        df_multi_final['CENTROPAGO'] = df_multi_final['CENTROPAGO'].astype(str).str.zfill(4)
        df_multi_final['CONTRATO'].fillna('NULL', inplace=True)
        df_multi_final['TIPO_FONDO'].fillna('NULL', inplace=True)
        df_multi_final['CARTERA'].fillna('NULL', inplace=True)
        df_multi_final['TIPO_CARTERA'].fillna('NULL', inplace=True)
        df_multi_final['AGENCIA_y'].fillna('NULL', inplace=True)
        
        df_multi_final['AGENCIA_y'] = df_multi_final.apply(
            lambda x: x['AGENCIA_y'] 
            if x['AGENCIA_y'] == x['AGENCIA_x'] else f'{x['AGENCIA_x']}/{x['AGENCIA_y']}', 
            axis=1)
        
        df_multi_final.drop(columns=['AGENCIA_x', 'FLAG_y', 'NOMBRE_CLIENTE_y'], inplace=True)
        df_multi_final.rename(columns={'AGENCIA_y': 'AGENCIA', 'FLAG_x': 'FLAG', 'NOMBRE_CLIENTE_x': 'NOMBRE_CLIENTE'}, inplace=True)
        
        cols_multi_final = ['FECHA', 'CC', 'CLAVSERV', 'CENTROPAGO', 'IMPORTE', 'MONEDA', 'NOMBRE', 'FLAG', 'CONTRATO', 'TIPO_FONDO', 'CARTERA', 'TIPO_PAGO', 'NOMBRE_CLIENTE', 'FECHA_ENVIO', 'ID_RESPONSABLE', 'TIPO_CARTERA', 'AGENCIA']
        df_multi_final = df_multi_final[cols_multi_final]
        df_multi_final.sort_values(by=['FECHA', 'FLAG', 'CC'], inplace=True)
        df_multi_final.reset_index(drop=True, inplace=True)
        
        # No Enviados Multiproducto
        df_no_enviados_multi = df_multi_final[(df_multi_final['CONTRATO'] == 'NULL') | (df_multi_final['TIPO_CARTERA'] != 'UNSECURED')]
        df_no_enviados_multi['AGENCIA'] = df_no_enviados_multi.apply(lambda x: 'AGENCIA NO IDENTIFICA' if x['CONTRATO'] == 'NULL' else x['AGENCIA'], axis=1)
        df_no_enviados_multi.drop(columns=['TIPO_PAGO'], inplace=True)
        print('No enviados Multiproducto:', df_no_enviados_multi.shape[0])
        
        # Reactivas Multiproducto
        df_reactivas_multi = df_multi_final[(df_multi_final['TIPO_CARTERA'] == 'UNSECURED') & (df_multi_final['TIPO_FONDO'].isin(self.fondos_gobierno))]
        df_reactivas_multi.drop(columns=['NOMBRE_CLIENTE', 'TIPO_CARTERA'], inplace=True)
        print('Reactivas Multiproducto:', df_reactivas_multi.shape[0])
        
        # Total Multiproducto
        df_multi_final = df_multi_final[(df_multi_final['CONTRATO'] != 'NULL') & 
                                        (df_multi_final['TIPO_CARTERA'] == 'UNSECURED') & 
                                        (~df_multi_final['TIPO_FONDO'].isin(self.fondos_gobierno))]
        df_multi_final.drop(columns=['TIPO_PAGO'], inplace=True)
        df_multi_final.to_excel(self.multiproducto, index=False)
        print('Total Multiproducto:', df_multi_final.shape[0])
        
        #Total No Enviados
        df_no_enviados_final = pd.concat([self.df_no_enviados, df_no_enviados_multi])
        df_no_enviados_final['CONTRATO'].fillna('NULL', inplace=True)
        df_no_enviados_final['TIPO_FONDO'].fillna('NULL', inplace=True)
        df_no_enviados_final['CARTERA'].fillna('NULL', inplace=True)
        df_no_enviados_final['TIPO_CARTERA'].fillna('NULL', inplace=True)
        df_no_enviados_final['NOMBRE_CLIENTE'].fillna('NULL', inplace=True)
        df_no_enviados_final['AGENCIA'].fillna('NULL', inplace=True)
        df_no_enviados_final['CLAVSERV'] = df_no_enviados_final['CLAVSERV'].apply(lambda x: str(int(x)).replace(' ', '').zfill(4))
        df_no_enviados_final.sort_values(by=['FECHA', 'FLAG', 'CC'], inplace=True)
        df_no_enviados_final.reset_index(drop=True, inplace=True)
        df_no_enviados_final.to_excel(self.no_enviados, index=False)
        
        #Total Reactiva
        df_reactiva = pd.read_excel(self.reactiva_path, dtype={'CC': str, 'CLAVSERV': str, 'CENTROPAGO': str, 'CONTRATO': str})
        df_reactiva_final = pd.concat([df_reactiva, df_reactivas_multi])
        df_reactiva_final['TIPO_PAGO'] = df_reactiva_final['TIPO_PAGO'].str.upper().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        df_reactiva_final['TIPO_PAGO'] = df_reactiva_final['TIPO_PAGO'].replace(' ', '').replace('TOTAL', 'CANCELACION').replace('PARCIAL', 'AMORTIZACION')
        df_reactiva_final.to_excel(self.reactiva, index=False)
        
        # Total Enviados
        df_enviados = pd.concat([self.df_mono_final, df_multi_final])
        df_enviados['CLAVSERV'] = df_enviados['CLAVSERV'].apply(lambda x: str(int(x)).zfill(4))
        df_enviados['CENTROPAGO'] = df_enviados['CENTROPAGO'].apply(lambda x: str(int(x)).zfill(4))
        df_enviados.sort_values(by=['FECHA', 'FLAG', 'CC'], inplace=True)
        df_enviados.reset_index(drop=True, inplace=True)
        df_enviados.to_excel(self.enviados, index=False)
        
        print('\n------------------------ REPORTE FINAL ------------------------')
        print('Base Bagos: ', self.df_base.shape)
        print('-------------------------------------------------')
        print('Monoproducto:', self.df_mono_final.shape)
        print('Importe Monoproducto:', round(self.df_mono_final['IMPORTE'].sum(), 2))
        print('-------------------------------------------------')
        print('Multiproducto:', df_multi_final.shape)
        print('Importe Multiproducto:', round(df_multi_final['IMPORTE'].sum(), 2))
        print('-------------------------------------------------')
        print('Reactiva:', df_reactiva_final.shape)
        print('Importe Reactiva:', round(df_reactiva_final['IMPORTE'].sum(), 2))
        print('-------------------------------------------------')
        print('No Enviados:', df_no_enviados_final.shape, '\n')
    
    def format_file(self, dict_files: dict[str, str]):
        for file, validator in dict_files.items():
            format_excel(file, validator)
    
    def open_file(self, file: str | list[str]):
        start_file(file)
    
    def execute_step_1(self):
        print("\n-------------------------------------------------")
        print("Inicializando paso 1...")
        self.get_backups()
        self.merge_dataframes()
        self.get_no_encontrados()
        self.get_monoproducto()
        self.get_monoproducto_reactiva()
        self.get_monoproducto_no_enviados()
        self.get_multiproducto()
        self.get_multiproducto_no_enviados()
        self.get_no_enviados()
        self.format_file({self.mono_path: 'mono', self.multi_path: 'multi_agencias', self.reactiva_path: 'react_agencias', self.no_enviados_path: 'noenv'})
        self.open_file([self.mono_path, self.multi_path, self.reactiva_path, self.no_enviados_path])
        print('\nPaso 1 completado')
    
    def send_email(self):
        print("\n-------------------------------------------------")
        print("Enviando correo...")
        flag_reactiva = self.reactiva_count != 0
        CorreoMultiproducto(self.last_date, self.folder_path, self.hora, flag_reactiva).enviar_correo()
        print('\nEnvio de correo completado')
    
    def execute_step_2(self):
        print("\n-------------------------------------------------")
        print("Inicializando paso 2...")
        self.get_multiproducto_agencias()
        self.format_file({self.multi_path: 'multi', self.reactiva_path: 'reactiva', self.no_enviados_path: 'noenv', self.enviados_path: 'env'})
        self.open_file([self.multi_path, self.reactiva_path, self.no_enviados_path, self.enviados_path])
        print('\nPaso 2 completado')
