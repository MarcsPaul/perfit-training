# install the following:
# pip install imageio
# pip install imageio-ffmpeg
# pip install pygifsicle
from pathlib import Path
import imageio

image_path = Path('source_images')
images = list(image_path.glob('*.jpg'))
image_list = []
for file_name in images:
    image_list.append(imageio.imread(file_name))
imageio.mimwrite('animated_from_images.gif', image_list)
