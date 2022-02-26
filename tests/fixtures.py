""" Objetos "pré-prontos" que o pytest entrega para os testes que os requisitarem.

Alguns detalhe sobre as fixtures:
- Prefira usar yield (o yield retorna como o return mas fica 'esperando' o
  caller liberar para ele continuar o que vem depois)
- O que vem antes do yield, chamamos de etapa de setup
- O que vem depois do yield, chamamos de teardown
- Só escreva fixtures para tarefas que realmente se repitam em vários testes
- O escopo das fixtures, por padrão, é function, quer dizer que a cada teste
  ele realizará o teardown. É possível escolher outros escopos para que testes
  tenham relação
"""
import pytest

from flaskapitested.flask_app import app


@pytest.fixture()
def clearclient():
    """Este fixture entrega um cliente pra nossa API sem qualquer alteração."""
    yield app.test_client()


@pytest.fixture()
def filledclient(clearclient):
    """Já este fixture entrega um cliente com uma adição prévia."""
    """SETUP"""
    clearclient.post(
        "/",
        json={"nome": "Praça da Cruz das Almas", "descricao": "Perto da rodoviária"},
    )

    yield clearclient
    """E depois a remove para não influenciar o próximo teste."""
    """TEARDOWN"""
    clearclient.delete("/0")
