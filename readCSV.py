import pandas as pd
from typing import List
from review import Review

# Función para leer un archivo CSV y devolver una lista de objetos Review


def readCsv(ruta: str) -> List[Review]:

    df = pd.read_csv(ruta)
    reviews = []

    for _, row in df.iterrows():
        review = Review(
            review_id=row['Id'],
            product_id=row['ProductId'],
            user_id=row['UserId'],
            profile_name=row['ProfileName'],
            helpfulness_numerator=row['HelpfulnessNumerator'],
            helpfulness_denominator=row['HelpfulnessDenominator'],
            score=row['Score'],
            time_unix=row['Time'],
            summary=row['Summary'],
            text=row['Text']
        )
        reviews.append(review)
    return reviews
