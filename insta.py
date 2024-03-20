from PIL import Image

def apply_filter(filter_func):
    for x in range(sirka):
        for y in range(vyska):
            r, g, b = obrazek.getpixel((x, y))
            obrazek.putpixel((x, y), filter_func(r, g, b))

def green_filter(r, g, b):
    return g, r, b

def inverse_filter(r, g, b):
    return 255 - r, 255 - g, 255 - b

def pink_filter(r, g, b):
    return int(r * 1.2), 0, int(b * 1.2)

def red_filter(r, g, b):
    return r, 0, 0

def blue_filter(r, g, b):
    return 0, 0, b

def cyberpunk_filter(r, g, b):
    return min(int(r * 1.5), 255), min(int(g * 0.5), 255), min(int(b * 2.0), 255)

print('Hello!')
print('Which filter do you want to use?')
choice = input("1. Green\n2. Inverse\n3. Pink\n4. Red\n5. Blue\n6. Cyberpunk\nEnter your choice: ")

filters = {
    "1": green_filter,
    "2": inverse_filter,
    "3": pink_filter,
    "4": red_filter,
    "5": blue_filter,
    "6": cyberpunk_filter
}

obrazek = Image.open("dog.jpg")
sirka, vyska = obrazek.size

if choice in filters:
    apply_filter(filters[choice])

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