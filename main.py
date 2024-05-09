from review import Review
from typing import Dict, List
from datetime import date
from sortedcontainers import SortedDict
from collections import defaultdict
from readCSV import readCsv

# Función para calcular el puntaje total por producto


def totalScore(reviews: List[Review]) -> Dict[str, int]:
    scores = defaultdict(int)

    for review in reviews:
        scores[review.product_id] += review.score
    return dict(scores)


# Método para listar los Top-M productos por puntaje


def topM(scores: Dict[str, int], top_m: int) -> None:
    sorted_scores = sorted(
        scores.items(), key=lambda x: x[1], reverse=True)

    top_products = sorted_scores[:top_m]

    print("Top-M productos por puntaje:")
    for product_id, total_score in top_products:
        print(f"Product ID: {product_id}, Total Score: {total_score}")

# Crear un árbol de búsqueda para reseñas por fecha


def reviewsPerDate(reviews: List[Review]) -> SortedDict[date, List[Review]]:
    reviewsPerDate = SortedDict()

    for review in reviews:
        review_date = review.date
        if review_date not in reviewsPerDate:
            reviewsPerDate[review_date] = []
        reviewsPerDate[review_date].append(review)
    return reviewsPerDate

# Método para listar Top-M productos en un rango de fechas


def topMPerDateRange(scores: Dict[str, int], reviewsPerDate: SortedDict[date, List[Review]], fecha_ini: date, fecha_fin: date, top_m: int) -> None:
    filtered_reviews = []

    for review_date in reviewsPerDate.irange(fecha_ini, fecha_fin):
        filtered_reviews.extend(reviewsPerDate[review_date])

    filtered_scores = defaultdict(int)
    for review in filtered_reviews:
        filtered_scores[review.product_id] += review.score

    topM(filtered_scores, top_m)


# Leer los datos del archivo CSV
reviews = readCsv("Reviews.csv")

# Calcular el puntaje total por producto
scores = totalScore(reviews)

# Imprimir los scores por producto
# for product_id, total_score in scores.items():
#    print(f"Product ID: {product_id}, Total Score: {total_score}")

# Listar los Top-5 productos
topM(scores, 15)

# Crear el árbol de búsqueda para reseñas por fecha
reviewsPerDate = reviewsPerDate(reviews)

# Listar los Top-3 productos en un rango de fechas
fecha_inicio = date(2011, 1, 1)
fecha_fin = date(2012, 12, 31)
topMPerDateRange(scores, reviewsPerDate, fecha_inicio, fecha_fin, 3)
