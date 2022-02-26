""" Importamos os fixtures para usar nos testes. Eles devem ser autodocumentados.
"""
from fixtures import clearclient, filledclient


def tests_if_resource_is_empty(clearclient):
    response = clearclient.get("/")
    assert len(response.get_json()) == 0


def tests_if_empty_resource_sends_404(clearclient):
    response = clearclient.get("/1")
    assert response.status_code == 404


def tests_if_all_has_items(filledclient):
    response = filledclient.get("/")
    assert len(response.get_json()) == 1


def tests_if_get_existing_item(filledclient):
    response = filledclient.get("/0")
    assert response.status_code == 200


def tests_if_gotten_item_is_right(filledclient):
    response = filledclient.get("/0")
    assert response.get_json()["nome"] == "Praça da Cruz das Almas"


def tests_if_update_on_non_existing_sends_404(filledclient):
    response = filledclient.put(
        "/2",
        json={"nome": "Praça da Cruz das Almas 2", "descricao": "Perto da rodoviária"},
    )
    assert response.status_code == 404


def tests_if_updates_existing_item(filledclient):
    response = filledclient.put(
        "/0",
        json={"nome": "Praça da Cruz das Almas 2", "descricao": "Perto da rodoviária"},
    )
    assert response.status_code == 200


def tests_if_update_item_is_right(filledclient):
    response = filledclient.put(
        "/0",
        json={"nome": "Praça da Cruz das Almas 2", "descricao": "Longe da rodoviária"},
    )
    assert response.get_json()["nome"] == "Praça da Cruz das Almas 2"
    assert response.get_json()["descricao"] == "Longe da rodoviária"


def tests_if_deleting_non_existing_sends_404(filledclient):
    response = filledclient.delete("/1")

    assert response.status_code == 404


def tests_if_delete_works(filledclient):
    response = filledclient.delete("/0")

    assert response.status_code == 200
