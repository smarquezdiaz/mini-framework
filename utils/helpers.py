from datetime import datetime
import pathlib


def assert_visible(page, selector, msg="Elemento no visible"):
    assert page.locator(selector).is_visible(), msg

def screenshot_path(name: str) -> str:
    out = pathlib.Path("reports") / "screenshots"
    out.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return str(out / f"{ts}_{name}.png")