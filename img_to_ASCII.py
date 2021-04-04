from PIL import Image
chars = ' .,:;i1lwbhHB#@╬░▒▓█'
img = Image.open('human.jpg').convert('L')
img_pixels = img.load()
width, height = img.size
with open('human_text.txt', 'w', encoding='utf8') as f:
    for x in range(height):
        for y in range(width):
            f.write((chars[-abs(int(img_pixels[y, x] // 12.8)-1)]) + ' ')
        f.write('\n')