from PIL import Image

img = Image.open("img/pokemontile.png")
print("Original:", img.size)  # deve mostrar (256, 528)

novo = img.resize((img.width * 4, img.height * 4), Image.NEAREST)
novo.save("img/pokemontile_64.png")
print("Novo:", novo.size)  # deve mostrar (1024, 2112)