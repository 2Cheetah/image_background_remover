from rembg import remove
from PIL import Image
from pathlib import Path
from os import listdir, mkdir
from os.path import splitext


def remove_bg(input_pics):
    list_of_extensions = ['.png', '.jpg', '.jpeg']
    all_files = [pic for pic in listdir(input_pics) if splitext(pic)[1] in list_of_extensions]
    output_filenames = [splitext(pic)[0]+'_wo_bg'+splitext(pic)[1] for pic in all_files]
    
    for index, pic in enumerate(all_files, start=1):
        input_path_filename = Path(input_pics + '/' + pic)
        output_path_filename = Path('./output_pics/' + splitext(pic)[0] + '_wo_bg' + '.png')
        input_image = Image.open(input_path_filename)
        output_image = remove(input_image)
        output_image.save(output_path_filename)

        print(f'Completed: {index}/{len(all_files)}')


if __name__ == '__main__':
    if 'output_pics' not in listdir():
        mkdir('output_pics')
    input_pics = input("Route to the folder with the pictures to process: ").strip().replace("'","")
    remove_bg(input_pics)
