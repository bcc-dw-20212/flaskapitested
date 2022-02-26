# flaskapitested
 Uma API feita em flask puro e com testes

Para preparar um ambiente python virtual, execute:

`$ python -m venv .venv`

Para ativar o ambiente criado:

`$ source .venv/bin/activate` (linux e creio que macOS também)

ou

`.\.venv\Scripts\activate` (Windows command prompt ou PowerShell - ambos testados)

Se você quiser reproduzir este projeto, instale o requirements:

`pip install -r requirements.txt`

Sinta-se a vontade para experimentar, alterar a api exemplificada, alterar a lógica ou torná-la mais complexa.

Para testar se os casos planejados funcionam, execute:

`pytest`

Para ter um relatório de cobertura de testes, principalmente se você alterar a API ou criar novos endpoints:

`pytest --cov`

Se quiser gerar um HTML com o report:

`pytest --report-cov html --cov`