import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class modelo:
    def __init__(self,colunas):
        self.colunas = colunas
        self.colunas.append('precoVenda')
        pass

    def linear_casa(self):
        df = pd.read_csv(r'modelos\datas\train.csv')
        df_personalisado = df[['YearBuilt', 'BedroomAbvGr', 'FullBath', 'GarageArea', 'SalePrice']]
        df_personalisado.columns = ['Ano', 'QtQuartos', 'QTbanheiros', 'GaragemArea', 'precoVenda']
        df_filtro = df_personalisado[self.colunas]
        x = df_filtro.drop('precoVenda', axis=1)
        y = df_filtro['precoVenda']
        X_train, Xtest, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=42)
        modelo = LinearRegression()
        modelo.fit(X_train, Y_train)
        return modelo


def retornar_df_filtro(self, filtros, df):
    colunas = filtros
    df_filtro = df[colunas]
    return df_filtro
