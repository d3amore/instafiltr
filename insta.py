from PIL import Image

print('Hello!')
print('Which filter do you want to use?')
choice = input("1. Green\n2. Inverse\n3. Pink\n4. Red\n5. Blue\n6. Cyberpunk\nEnter your choice: ")

obrazek = Image.open("dog.jpg")
sirka, vyska = obrazek.size

if choice == "1":
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x, y))
            prumer = int((r + g + b) / 3)
            obrazek.putpixel((x, y), (g, r, b))
            y += 1
        x += 1
    obrazek.save("modified_dog.jpg")
    obrazek_modified = Image.open("modified_dog.jpg")
    obrazek_modified.show()

#r,r,r
#r , b, r
#r, 0, 0 -red
#0, g, 0 -green 
#g, r, b - greenish
#(255 - r, 255 - g, 255 - b) - inverse 
#(int(r * 1.2), 0, int(b * 1.2)) -pinkk
#(min(int(r * 1.5), 255), min(int(g * 0.5), 255), min(int(b * 2.0), 255)) - cyberpunk