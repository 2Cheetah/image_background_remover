from rembg import remove
from PIL import Image
from pathlib import Path
from os import listdir
from os.path import splitext, abspath


def remove_bg():
    list_of_extensions = ['.png', '.jpg']
    all_files = [pic for pic in listdir('./input_pics') if splitext(pic)[1] in list_of_extensions]
    # print(all_files)
    output_filenames = [splitext(pic)[0]+'_wo_bg'+splitext(pic)[1] for pic in all_files]
    
    for index, pic in enumerate(all_files):
        input_path_filename = Path('./input_pics/' + pic)
        # print(abspath(input_path_filename))
        output_path_filename = Path('./output_pics/' + splitext(pic)[0] + '_wo_bg' + '.png')
        # print(abspath(output_path_filename))

        input_image = Image.open(input_path_filename)
        output_image = remove(input_image)
        output_image.save(output_path_filename)

        print(f'Completed: {index + 1}/{len(all_files)}')

if __name__ == '__main__':
    remove_bg()
