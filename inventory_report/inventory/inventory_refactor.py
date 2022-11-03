from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        self.data.extend(self.importer.import_data(path))

    def __iter__(self):
        return InventoryIterator(self.data)
