import pandas as pd
import numpy as np

#Read in the document from excel, skip 5 rows at top, and 7 rows at bottom (meta data). Set first column as index.
divorce=pd.read_excel ('Divorce_Rates_Dirty.xlsx', skiprows=5, skipfooter=7, header=[0], index_col=0)
#Deletes all null rows in the data set.
divorce.dropna(how='all', inplace=True)  
#Stacks the states column which converts the dataset to long form. 
divorce = divorce.stack([0]).reset_index()
#Renames the column headers to the appropriate name.
divorce=divorce.rename(columns={'level_0':'state','level_1':'year', 0:'divorce_rate'})


#write the dataframe to an excel spreadsheet
divorce.to_excel(excel_writer='DIVORCE_CLEAN_PY.xls',           # name the excel file "school_clean"
                sheet_name='divorce',                            # name the sheet "school"
                na_rep='null',                                  # treat n/a as null (some programs want specific style)
                index=False)             