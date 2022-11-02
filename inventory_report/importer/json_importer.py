from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith('json'):
            with open(path) as file:
                return json.loads(file.read())
        else:
            raise ValueError("Arquivo inválido")
