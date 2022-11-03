import csv
import json
import xmltodict

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:

    @classmethod
    def import_data(cls, path, report_type):
        if path.endswith(".csv"):
            product_list = cls.read_csv(path)
        if path.endswith(".json"):
            product_list = cls.read_json(path)
        if path.endswith(".xml"):
            product_list = cls.read_xml(path)
        if report_type == "simples":
            return SimpleReport.generate(product_list)
        else:
            return CompleteReport.generate(product_list)

    @classmethod
    def read_csv(cls, path):
        with open(path) as file:
            return list(csv.DictReader(file))

    @classmethod
    def read_json(cls, path):
        with open(path) as file:
            return json.loads(file.read())

    @classmethod
    def read_xml(cls, path):
        with open(path) as file:
            return xmltodict.parse(file.read())["dataset"]["record"]
