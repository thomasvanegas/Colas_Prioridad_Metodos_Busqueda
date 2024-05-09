from datetime import datetime


class Review:
    def __init__(self, review_id, product_id, user_id, profile_name, helpfulness_numerator, helpfulness_denominator, score, time_unix, summary, text):
        self.review_id = review_id
        self.product_id = product_id
        self.user_id = user_id
        self.profile_name = profile_name
        self.helpfulness_numerator = helpfulness_numerator
        self.helpfulness_denominator = helpfulness_denominator
        self.score = score
        self.date = self.unix_to_date(time_unix)
        self.summary = summary
        self.text = text


# Convertir el tiempo UNIX a date

    @staticmethod
    def unix_to_date(unix_time):
        return datetime.fromtimestamp(unix_time).date()

# Limitar los strings a un maximo de 30 caracteres
    @staticmethod
    def truncate(text, max_length):
        if len(text) > max_length:
            return text[:max_length] + '...'
        return text

    def __str__(self):
        truncated_profile_name = self.truncate(self.profile_name, 30)
        truncated_summary = self.truncate(self.summary, 30)

        return (f"Review {self.review_id} by {truncated_profile_name} on {self.date}: "
                f"'{truncated_summary}' (Score: {self.score})")
