import certifi
import easyocr
import os

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

reader = easyocr.Reader(['ch_sim','en'])

result = reader.readtext("./output/screenshot.jpg")

print(result)