from PIL import Image, ImageDraw, ImageFont
import os
import random
increment = 1

output_directory = "C:\\dataset"


if not os.path.exists(output_directory):
    os.makedirs(output_directory)
png = '.png'




font_size = 10

def letters(fontsize, offsetX, offsetY):
    
    for i in range(26):
        global increment
        
        letter=chr(65+i)
        
        letter_directory = os.path.join(output_directory, letter)
        if not os.path.exists(letter_directory):
            os.makedirs(letter_directory)
        
        img = Image.new('L', (24, 24), color='white')
        
        draw = ImageDraw.Draw(img)
        
        font = ImageFont.truetype(random.choice(os.listdir("C:\\Users\\Danielko2\\ttf")), fontsize)
        
        text_width, text_height = draw.textsize(letter, font=font)
        x = (24 - text_width) / 2 + offsetX
        y = (24 - text_height) / 2 + offsetY
        
        draw.text((x, y), chr(65+i), fill='black', font=font)
        img = img.point(lambda p: p > 200 and 255)
        img.save(os.path.join(letter_directory, str(increment)+png))
        

        
        img = Image.new('L', (24, 24), color='black')
        
        draw = ImageDraw.Draw(img)
        
        font = ImageFont.truetype(random.choice(os.listdir("C:\\Users\\Danielko2\\ttf")), fontsize)
        
        text_width, text_height = draw.textsize(letter, font=font)
        x = (12 - text_width) / 2 + offsetX
        y = (12 - text_height) / 2 + offsetY
        
        draw.text((x, y), chr(65+i), fill='white', font=font)
        img = img.point(lambda p: p > 55 and 255)
        img.save(os.path.join(letter_directory, str(increment+1)+png))
        increment += 2
        
def randomletters():
    size = 12
    for q in range(10):
        for y in range(-4, 5):
            for x in range(-4, 5):
                letters(size, x, y)
        size += 1



increment = 0

while(True):
    randomletters()

print("Hotovo!")
