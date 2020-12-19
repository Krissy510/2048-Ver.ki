from PIL import Image
lst = ['sourcepic\\tile2.jpg', 'sourcepic\\tile4.jpg', 'sourcepic\\tile8.jpg', 'sourcepic\\tile16.jpg', 'sourcepic\\tile32.jpg', 'sourcepic\\tile64.jpg', 'sourcepic\\tile128.jpg', 'sourcepic\\tile256.jpg', 'sourcepic\\tile512.jpg', 'sourcepic\\tile1024.jpg', 'sourcepic\\tile2048.jpg']
for path in lst:
    image = Image.open(path)
    new_img = image.resize((120, 120))
    new_img.save(path)