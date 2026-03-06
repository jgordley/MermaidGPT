import base64
from PIL import Image
import requests
import io

def generate_diagram(graph):
    graphbytes = graph.encode("utf-8")
    base64_bytes = base64.urlsafe_b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")
    response = requests.get("https://mermaid.ink/img/" + base64_string, timeout=15)
    response.raise_for_status()
    img = Image.open(io.BytesIO(response.content))
    return img
