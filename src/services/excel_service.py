import pandas as pd

class ExcelService:
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def read_sheet(self, sheet_name: str|None = None) -> pd.DataFrame:
        return pd.read_excel(self.file_path, sheet_name=sheet_name)
    
    def write_sheet(self, df: pd.DataFrame, sheet_name: str):
        with pd.ExcelWriter(self.file_path, mode='a', if_sheet_exists='replace') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)