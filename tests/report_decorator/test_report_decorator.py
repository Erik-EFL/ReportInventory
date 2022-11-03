from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def mock_products():
    return [
        {
            "id": 1,
            "nome_da_empresa": "Dell",
            "data_de_fabricacao": "2021-07-15",
            "data_de_validade": "2022-07-15",
        },
        {
            "id": 2,
            "nome_da_empresa": "Razer",
            "data_de_fabricacao": "2021-07-15",
            "data_de_validade": "2027-01-15",
        }
    ]


def test_decorar_relatorio(mock_products):
    red = "\033[31m"
    green = "\033[32m"
    blue = "\033[36m"
    end = "\033[0m"

    report = ColoredReport(SimpleReport)
    new_report = report.generate(mock_products)

    assert f"{green}Data de fabricação mais antiga:{end}" in new_report
    assert f"{blue}2021-07-15{end}" in new_report

    assert f"{green}Data de validade mais próxima:{end}" in new_report
    assert f"{blue}2022-07-15{end}" in new_report

    assert f"{green}Empresa com mais produtos:{end}" in new_report
    assert f"{red}Dell{end}" in new_report
