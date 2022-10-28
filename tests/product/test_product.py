from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Café",
        "Nescafé",
        "2020-01-01",
        "2021-01-01",
        "123456789",
        "em local seco e fresco",
    )
    assert product.id == 1
    assert product.nome_do_produto == "Café"
    assert product.nome_da_empresa == "Nescafé"
    assert product.data_de_fabricacao == "2020-01-01"
    assert product.data_de_validade == "2021-01-01"
    assert product.numero_de_serie == "123456789"
    assert product.instrucoes_de_armazenamento == "em local seco e fresco"
