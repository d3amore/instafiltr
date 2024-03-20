from PIL import Image
print('Hello!')
print('Which filter do you want to use?')
choice =  int(input("1.green/ 2.inverse 3.pink 4.red 5. blue 6.cyberpunk"))
obrazek = Image.open("dog.jpg")
sirka, vyska = obrazek.size
x = 0
if choice == "1":
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y),(g, r, b))
            y += 1
        x += 1
    obrazek.save("modified_dog.jpg")    
    obrazek.show()

#r,r,r
#r , b, r
#r, 0, 0 -red
#0, g, 0 -green 
#g, r, b - greenish
#(255 - r, 255 - g, 255 - b) - inverse 
#(int(r * 1.2), 0, int(b * 1.2)) -pinkk
#(min(int(r * 1.5), 255), min(int(g * 0.5), 255), min(int(b * 2.0), 255)) - cyberpunk