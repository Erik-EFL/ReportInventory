from collections import Counter
from datetime import datetime


class SimpleReport:
    def __init__(self, date_list):
        self.date_list = date_list

    def get_oldest_date(self, date_list):
        date = min(
            [product["data_de_fabricacao"] for product in date_list])
        return date

    def get_closest_date(self, date_list):
        date = min(
            [
                product["data_de_validade"]
                for product in date_list
                if datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
                > datetime.now()
            ]
        )
        return date

    def get_companies(self, date_list):
        companies = Counter(
            product["nome_da_empresa"] for product in date_list)
        return companies.most_common(1)[0][0]

    @classmethod
    def generate(self, date_list):
        oldest_date = self.get_oldest_date(self, date_list)
        closest_date = self.get_closest_date(self, date_list)
        companies = self.get_companies(self, date_list)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {companies}"
          )
