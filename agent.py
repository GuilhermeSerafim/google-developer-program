
# Importa a biblioteca para trabalhar com caminhos de arquivos.
from pathlib import Path

# Importa os SDKs do Google Cloud Storage e Cloud Vision.
from google.cloud import storage, vision

# Importa a classe Agent do Google ADK.
from google.adk.agents.llm_agent import Agent


# Caminho da imagem que será utilizada pelas ferramentas.
# __file__ representa o arquivo agent.py.
# .parent identifica a pasta healthy_hints.
IMAGE_PATH = (
    Path(__file__).resolve().parent
    / "images"
    / "Ingredients-list.jpg"
)


# ============================================================
# TOOL 1 — UPLOAD IMAGE (GOOGLE CLOUD STORAGE)
# ============================================================

def upload_image() -> str:
    """Uploads an ingredients image to Google Cloud Storage."""

    # Inicializa o cliente do Google Cloud Storage.
    # Ele utiliza as credenciais disponíveis no ambiente.
    storage_client = storage.Client()

    bucket_name = "healthy-hints-guiler-uscentral1-20261009"

    # Obtém uma referência ao bucket.
    bucket = storage_client.bucket(bucket_name)

    # Define o nome do objeto que será armazenado.
    blob = bucket.blob("Ingredients-list.jpg")

    # Envia a imagem local para o bucket.
    # Esta linha executa uma operação real no Google Cloud.
    blob.upload_from_filename(str(IMAGE_PATH))

    # Retorna o endereço do arquivo armazenado.
    return f"Image uploaded to gs://{bucket_name}/{blob.name}"


# ============================================================
# TOOL 2 — READ INGREDIENTS (GOOGLE CLOUD VISION)
# ============================================================

def read_ingredients() -> str:
    """Reads ingredients from an image using Google Cloud Vision."""

    # Inicializa o cliente da API Cloud Vision.
    vision_client = vision.ImageAnnotatorClient()

    # Abre a imagem local em modo de leitura binária.
    with IMAGE_PATH.open("rb") as image_file:

        # Lê todos os bytes da imagem.
        content = image_file.read()

    # Cria um objeto de imagem aceito pelo Cloud Vision.
    image = vision.Image(content=content)

    # Envia a imagem para o serviço de reconhecimento de texto.
    # Esta operação utiliza a API Cloud Vision.
    response = vision_client.text_detection(image=image)

    # Obtém os textos reconhecidos.
    texts = response.text_annotations

    # Caso nenhum texto seja identificado, retorna uma mensagem.
    if not texts:
        return "No text detected."

    # Retorna o texto completo identificado na imagem.
    return texts[0].description


# ============================================================
# ROOT AGENT — GOOGLE ADK
# ============================================================

root_agent = Agent(

    # Modelo de linguagem utilizado pelo agente.
    model="gemini-2.5-flash",

    # Identificador interno do agente.
    name="healthy_hints_agent",

    # Descrição da finalidade do agente.
    description=(
        "Agent to upload an image to Google Cloud Storage, "
        "read its ingredients and explain whether "
        "each ingredient is healthy."
    ),

    # Instruções que orientam o comportamento do modelo.
    instruction=(
        "You are a helpful agent who will upload the image "
        "to Google Cloud Storage using the upload_image tool, "
        "read the ingredients using the read_ingredients tool "
        "and explain whether each ingredient is healthy "
        "or not in one line."
    ),

    # Registra as duas funções como ferramentas do agente.
    tools=[upload_image, read_ingredients],
)
