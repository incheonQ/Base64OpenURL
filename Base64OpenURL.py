import base64
import webbrowser
import clipboard

def base64_encode(contents):
    contents_bytes = contents.encode('ascii')
    contents_base64 = base64.b64encode(contents_bytes)
    base64_str = contents_base64.decode('ascii')
    return base64_str

def base64_decode(base64_str):
    contents = base64.b64decode(base64_str).decode('ascii')
    return contents

contents = clipboard.paste()

try:
    url = base64_decode(contents)
    webbrowser.open(url)
except:
    encoded = base64_encode(contents)
    clipboard.copy(encoded)
