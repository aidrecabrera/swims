from pathlib import Path

CURRENT_PATH = Path(__file__).parent
ASSETS_PATH = CURRENT_PATH / 'assets' / 'frame0'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)