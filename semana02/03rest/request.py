import requests

import requests
r = requests.get("http://localhost:8000/estudiantes")
print(r.status_code, r.text)