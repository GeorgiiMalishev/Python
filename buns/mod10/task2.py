import re
import requests

url = input("Введите ссылку: ")
response = requests.get(url)
html_content = response.text

pattern = r'<h3[^>]*>.*?(?:<(?!\/?h3)[^>]*>.*?)*([^<]+).*?<\/h3>'
matches = re.findall(pattern, html_content)

print(matches)


