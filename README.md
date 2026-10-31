# Healthy Hints — estudo de agente com Google ADK

Exemplo Python que configura um agente para trabalhar com uma imagem de lista de ingredientes. O nome do repositório não implica certificação, vínculo profissional ou endosso do Google.

## Arquivos e escopo

- `agent.py` define `root_agent`, usando Google ADK e o modelo `gemini-2.5-flash` configurado no código.
- `upload_image` envia a imagem local a um bucket Google Cloud Storage configurado no fonte.
- `read_ingredients` envia a imagem à API Cloud Vision para reconhecimento de texto.
- `local_test.py` implementa somente uma cópia local da imagem para `test_storage`; não valida ADK, OCR ou o modelo.

O agente recebe instruções para comentar ingredientes. Isso descreve a intenção do exemplo, não comprova qualidade nutricional, precisão ou adequação das respostas para decisões de saúde.

## Dependências e execução

O repositório não contém `requirements.txt`, `pyproject.toml` ou versões fixadas dos SDKs. O fonte importa Google ADK e os clientes Google Cloud Storage/Vision e usa credenciais do ambiente. Antes de executar, é necessário definir ambiente Python compatível, dependências, projeto, permissões e bucket sob controle do operador.

As funções de nuvem realizam operações reais e podem consumir serviços pagos; não são mocks. O script local apenas copia a imagem no disco e não substitui a configuração dos serviços Google.
