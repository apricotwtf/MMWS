from requests import get

SOURCE = "https://scratch.mit.edu/discuss/post/6429679/source/"

with open('./main.js', 'w') as file:
    file.write(get(SOURCE).text)