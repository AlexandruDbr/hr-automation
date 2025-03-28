import pandas as pd
import os 
from datetime import date

hr_file = r"C:\Users\alexandru.dobre\OneDrive - Brillio\Desktop\Internship files\Project\BI projects\Automation tool_myself\Project_files\Pontaj 2025.xlsx"
appendix_table = r"C:\Users\alexandru.dobre\OneDrive - Brillio\Desktop\Internship files\Project\BI projects\Automation tool_myself\Project_files\Calculation_table.xlsx"
export_path = r"C:\Users\alexandru.dobre\OneDrive - Brillio\Desktop\Internship files\Project\BI projects\Automation tool_myself\Project_files\Pontaj_final.csv"

df_hr_file = pd.read_excel(hr_file, sheet_name=0)
df_appendix = pd.read_excel(appendix_table)

max_col = len(df_hr_file.columns)
start_col = max_col+1


# Write to the Excel sheet starting at the new column
new_df = pd.DataFrame(pd.concat([df_hr_file, df_appendix],axis=1))

new_df.to_csv(export_path)


