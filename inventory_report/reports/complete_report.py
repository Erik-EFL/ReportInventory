from collections import Counter

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self, date_list):
        self.date_list = date_list

    def simple_report(self, date_list):
        return super().generate(date_list)

    def companies(self, date_list):
        companies = list()
        all_companies = ""

        for product in date_list:
            companies.append(product["nome_da_empresa"])

        company_counter = Counter(companies).most_common()

        for index, value in company_counter:
            all_companies += f"- {index}: {value}\n"

        return all_companies

    @classmethod
    def generate(self, date_list):
        title = "Produtos estocados por empresa:"
        simple_report = self.simple_report(self, date_list)
        companies_list = self.companies(self, date_list)
        return f"{simple_report}\n{title}\n{companies_list}"
