import base64
from PIL import Image
import requests
import io

def generate_diagram(graph):
  graphbytes = graph.encode("ascii")
  base64_bytes = base64.b64encode(graphbytes)
  base64_string = base64_bytes.decode("ascii")
  img = Image.open(io.BytesIO(requests.get('https://mermaid.ink/img/' + base64_string).content))
  return img