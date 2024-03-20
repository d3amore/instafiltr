from PIL import Image

def green_filter():
    for x in range(sirka):
        for y in range(vyska):
            r, g, b = obrazek.getpixel((x, y))
            obrazek.putpixel((x, y), (g, r, b))

def inverse_filter():
    for x in range(sirka):
        for y in range(vyska):
            r, g, b = obrazek.getpixel((x, y))
            obrazek.putpixel((x, y), (255 - r, 255 - g, 255 - b))

def pink_filter():
    for x in range(sirka):
        for y in range(vyska):
            r, g, b = obrazek.getpixel((x, y))
            obrazek.putpixel((x, y), (int(r * 1.2), 0, int(b * 1.2)))    

def red_filter():
    for x in range(sirka):
        for y in range(vyska):
            r, g, b = obrazek.getpixel((x, y))
            obrazek.putpixel((x, y), (r, 0, 0))

def blue_filter():
    for x in range(sirka):
        for y in range(vyska):
            r, g, b = obrazek.getpixel((x, y))
            obrazek.putpixel((x, y), (0 , 0, b))  

def cyberpunk_filter():
    for x in range(sirka):
        for y in range(vyska):
            r, g, b = obrazek.getpixel((x, y))
            obrazek.putpixel((x, y), (min(int(r * 1.5), 255), min(int(g * 0.5), 255), min(int(b * 2.0), 255)))                          

print('Hello!')
print('Which filter do you want to use?')
choice = input("1. Green\n2. Inverse\n3. Pink\n4. Red\n5. Blue\n6. Cyberpunk\nEnter your choice: ")

obrazek = Image.open("dog.jpg")
sirka, vyska = obrazek.size

if choice == "1":
    green_filter()
elif choice == "2":
    inverse_filter()
elif choice == "3":
    pink_filter()
elif choice == "4":
    red_filter() 
elif choice == "5":
    blue_filter()
elif choice == "6":
    cyberpunk_filter()            

                   



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