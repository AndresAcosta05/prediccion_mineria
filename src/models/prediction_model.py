import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np

from config import Conecction

class predictionModel:

    @classmethod
    def md_prediction_predict(cls, data):
        with open('data.csv', 'r') as file:
            # importamos el archivo para la data
            df = pd.read_csv(file)
            edad = data["edad"]
            locacion = data["locacion"]
            tamaño = data["tamaño"]
            color = data["color"]
            temporada = data["temporada"]
            descuento = data["descuento"]
            cod_promocion = data["cod_promocion"]
            previas_compras = data["previas_compras"]
            # transformamos los datos para que puedan ser entrenados
            df['Gender'] = LabelEncoder().fit_transform(df['Gender'])
            df['Item Purchased'] = LabelEncoder().fit_transform(df['Item Purchased'])
            df['Category'] = LabelEncoder().fit_transform(df['Category'])
            df['Location'] = LabelEncoder().fit_transform(df['Location'])
            df['Size'] = LabelEncoder().fit_transform(df['Size'])
            df['Color'] = LabelEncoder().fit_transform(df['Color'])
            df['Season'] = LabelEncoder().fit_transform(df['Season'])
            df['Previous Purchases'] = LabelEncoder().fit_transform(df['Previous Purchases'])
            df['Shipping Type'] = LabelEncoder().fit_transform(df['Shipping Type'])
            df['Discount Applied'] = LabelEncoder().fit_transform(df['Discount Applied'])
            df['Promo Code Used'] = LabelEncoder().fit_transform(df['Promo Code Used'])
            df['Payment Method'] = LabelEncoder().fit_transform(df['Payment Method'])
            df['Frequency of Purchases'] = LabelEncoder().fit_transform(df['Frequency of Purchases'])
            # creamos las variables dependientes e independientes
            independientes = df[['Age','Location','Size','Color','Season','Discount Applied','Promo Code Used','Previous Purchases']]
            dependientes = df['Subscription Status']
            # entrenamos el algoritmo de regresion logistica
            entrenoX, testX, entrenoY, testY = train_test_split(independientes, dependientes, test_size=0.3, random_state=4)
            r_logistica = LogisticRegression(max_iter=1000)
            r_logistica = r_logistica.fit(entrenoX, entrenoY.values.ravel())
            score = r_logistica.score(entrenoX, entrenoY)
            # tenemos un score de 0.7326007326007326
            predict = r_logistica.predict([[edad, locacion, tamaño, color, temporada, descuento, cod_promocion, previas_compras]])
            return predict[0]