
from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent
IMAGE = BASE_DIR / "images" / "Ingredients-list.jpg"
DESTINATION = BASE_DIR / "test_storage" / IMAGE.name


def upload_image_local() -> str:
    """Simulates an image upload using local storage."""
    if not IMAGE.is_file():
        return "error: image not found"

    DESTINATION.parent.mkdir(exist_ok=True)
    shutil.copy2(IMAGE, DESTINATION)

    return f"success: image stored at {DESTINATION}"


if __name__ == "__main__":
    print(upload_image_local())
