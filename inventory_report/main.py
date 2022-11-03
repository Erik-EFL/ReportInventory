import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.colored_report import ColoredReport

importers = {
    ".csv": CsvImporter,
    "json": JsonImporter,
    ".xml": XmlImporter,
}

report_types = {
    "completo": CompleteReport,
    "simples": SimpleReport,
    "colorido": ColoredReport
}


def main():
    try:
        path = sys.argv[1]
        type = sys.argv[2]
        importer = importers.get(path[-4:])
        report_type = report_types.get(type)
        inventory = InventoryRefactor(importer)
        inventory.import_data(path, type)
        if report_type == ColoredReport:
            report = ColoredReport(SimpleReport)
            colored_report = report.generate(inventory)
            sys.stdout.write(colored_report)
        else:
            sys.stdout.write(report_type.generate(inventory))
    except IndexError:
        sys.stderr.write("Verifique os argumentos\n")
