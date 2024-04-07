import pandas as pd

def funcion():
    
    dic={'time':['2024-01-01', '2024-01-02', '2024-01-03'],
         'target':[1000,2000,3000]}
    datos = pd.DataFrame(dic)
    
    return datos.to_csv('dataframe.csv')