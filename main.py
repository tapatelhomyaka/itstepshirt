import sys
from PIL import Image
from PIL import ImageOps


def Main(img_files, blend_file, output_files):
    print("Processing images...")

    blend = Image.open(blend_file)

    for i, img_file in enumerate(img_files):
        img = Image.open(img_file)
        simg = ImageOps.fit(img, blend.size, method=0, bleed=0.0, centering=(0.5, 0.5))
        simg.paste(blend, (0, 0), blend)
        simg.show()
        simg.save(output_files[i])
        print(f"Saved result to {output_files[i]}")


if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python script.py blend_file img1 img2 img3 output1 output2 output3")
        sys.exit(1)

    blend_file = sys.argv[1]
    img_files = sys.argv[2:5]
    output_files = sys.argv[5:8]

    Main(img_files, blend_file, output_files)
