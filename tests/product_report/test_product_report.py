from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 1
    nome_do_produto = "Café"
    nome_da_empresa = "Nescafé"
    data_de_fabricacao = "2020-01-01"
    data_de_validade = "2021-01-01"
    numero_de_serie = "123456789"
    instrucoes_de_armazenamento = "em local seco e fresco"
    message = (
        f"O produto {nome_do_produto} fabricado em {data_de_fabricacao} "
        f"por {nome_da_empresa} com validade até {data_de_validade} "
        f"precisa ser armazenado {instrucoes_de_armazenamento}."
    )

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert repr(product) == message
