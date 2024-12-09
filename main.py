from PIL import Image
from PIL import ImageOps

def Main():
    print("working")
    img1 = Image.open("before1.jpg")
    img2 = Image.open("before2.jpg")
    img3 = Image.open("before3.jpg")
    blend = Image.open("shirt.png")
    simg1 = ImageOps.fit(img1, blend.size,method=0,bleed=0.0, centering=(0.5, 0.5))
    simg1.paste(blend, (0,0), blend)
    simg1.show()
    simg2 = ImageOps.fit(img2, blend.size,method=0,bleed=0.0, centering=(0.5, 0.5))
    simg2.paste(blend, (0,0), blend)
    simg2.show()
    simg3 = ImageOps.fit(img3, blend.size,method=0,bleed=0.0, centering=(0.5, 0.5))
    simg3.paste(blend, (0,0), blend)
    simg3.show()
    simg3.save("result1.jpg")
    simg2.save("result2.jpg")
    simg1.save("result3.jpg")

if __name__ == "__main__":
    Main()