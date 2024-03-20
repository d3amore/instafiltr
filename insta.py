from PIL import Image
obrazek = Image.open("dog.jpg")
sirka, vyska = obrazek.size
x = 0
while x < sirka:
    y = 0
    while y < vyska:
        r, g, b = obrazek.getpixel((x,y))
        prumer = int((r+g+b)/3)
        obrazek.putpixel((x,y),(min(int(r * 1.5), 255), min(int(g * 0.5), 255), min(int(b * 2.0), 255)))
        y += 1
    x += 1
display(obrazek)

#r,r,r
#r , b, r
#r, 0, 0 -red
#0, g, 0 -green 
#g, r, b - greenish
#(255 - r, 255 - g, 255 - b) - inverse 
#(int(r * 1.2), 0, int(b * 1.2)) -pinkk
#(min(int(r * 1.5), 255), min(int(g * 0.5), 255), min(int(b * 2.0), 255)) - cyberpunk