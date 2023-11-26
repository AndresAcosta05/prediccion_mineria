import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

from config import Conecction

class predictionModel:

    @classmethod
    def md_prediction_predict(cls, data):
        with open('data.csv', 'r') as file:
            edad = int(data["edad"])
            locacion = int(data["locacion"])
            tamaño = int(data["tamaño"])
            color = int(data["color"])
            temporada = int(data["temporada"])
            descuento = int(data["descuento"])
            cod_promocion = int(data["cod_promocion"])
            compras_previas = int(data["compras_previas"])
            # importamos el archivo para la data
            df = pd.read_csv(file)
            label_encoder_location = LabelEncoder()
            label_encoder_size = LabelEncoder()
            label_encoder_color = LabelEncoder()
            label_encoder_season = LabelEncoder()
            label_encoder_descuento = LabelEncoder()
            label_encoder_promo = LabelEncoder()
            label_encoder_compras = LabelEncoder()
            # transformamos los datos para que puedan ser entrenados
            df['Location'] = label_encoder_location.fit_transform(df['Location'])
            df['Size'] = label_encoder_size.fit_transform(df['Size'])
            df['Color'] = label_encoder_color.fit_transform(df['Color'])
            df['Season'] = label_encoder_season.fit_transform(df['Season'])
            df['Discount Applied'] = label_encoder_descuento.fit_transform(df['Discount Applied'])
            df['Promo Code Used'] = label_encoder_promo.fit_transform(df['Promo Code Used'])
            df['Previous Purchases'] = label_encoder_compras.fit_transform(df['Previous Purchases'])
            # creamos las variables dependientes e independientes
            independientes = df[['Age','Location','Size','Color','Season','Discount Applied','Promo Code Used','Previous Purchases']]
            dependientes = df['Subscription Status']
            # entrenamos el algoritmo de regresion logistica
            entrenoX, testX, entrenoY, testY = train_test_split(independientes, dependientes, test_size=0.3, random_state=4)
            r_logistica = LogisticRegression(max_iter=1000)
            r_logistica = r_logistica.fit(entrenoX, entrenoY.values.ravel())
            score = r_logistica.score(entrenoX, entrenoY)
            # tenemos un score de 0.7326007326007326
            predict = r_logistica.predict([[edad, locacion, tamaño, color, temporada, descuento, cod_promocion, compras_previas]])

            # ESPACIO PARA INSERTAR
            try:
                connection = Conecction.getConecction()
                with connection.cursor() as cursor:
                    L = str(label_encoder_location.inverse_transform([locacion])[0])
                    S = str(label_encoder_size.inverse_transform([tamaño])[0])
                    C = str(label_encoder_color.inverse_transform([color])[0])
                    T = str(label_encoder_season.inverse_transform([temporada])[0])
                    D = str(label_encoder_descuento.inverse_transform([descuento])[0])
                    P = str(label_encoder_promo.inverse_transform([cod_promocion])[0])
                    B = str(label_encoder_compras.inverse_transform([compras_previas])[0])

                    sql = "INSERT INTO predictions(edad, locacion, tamaño, color, temporada, descuento, cod_promocion, compras_previas, prediccion) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql, (edad, L, S, C, T, D, P, B, str(predict[0])))
                    connection.commit()
                    return predict[0]
            
            except Exception as ex:
                print(ex)
                return False