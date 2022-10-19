import pandas as pd

data = pd.read_excel(
    r"F:\打工人\10.18_citiation\data\Table_1_Authors_career_2021_pubs_since_1788_wopp_extracted_202209.xlsx",
    sheet_name="Data")
print(data)
