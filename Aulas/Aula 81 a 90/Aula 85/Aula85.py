import urllib.request

pagina = urllib.request.urlopen("https://github.com/itallok")
texto = pagina.read().decode("utf8")

print(texto)