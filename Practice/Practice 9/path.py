import os
from pdf2docx import parse
from docx2pdf import convert
from PIL import Image

cwd = os.getcwd()
print(cwd)
def change_directory(path: str) -> str:
    os.chdir(path)
    return os.getcwd()
def convert_pdf_to_docx(path: str) -> None:
    pdf_file = path
    docx_file = path[:-3] + 'docx'
    parse(pdf_file, docx_file)
def convert_docx_to_pdf(path: str) -> None:
    convert(path)
def compress_image(path: str, compression_k: int) -> None:
    image_file = Image.open(path)
    image_file.save(f"new {path}", quality=compression_k)
def find_pdf_files() -> list:
    print('Список файлов с расширением PDF в данном каталоге')
    list_with_pdf = [i for i in os.listdir(path='.') if i[-4:] == '.pdf']
    return list_with_pdf
def find_docx_files() -> list:
    print('Список файлов с расширением Docx в данном каталоге')
    list_with_docx = [i for i in os.listdir(path='.') if i[-5:] == '.docx']
    return list_with_docx
def find_image_files() -> list:
    print('Список файлов с расширением "jpeg","jpg","gif","png" в данном каталоге')
    list_with_images = [i for i in os.listdir(path='.') if
    i[-5:] == '.jpeg' or i[-4:] == '.jpg' or i[-4:] == '.gif' or i[-4:] == '.png']
    return list_with_images
def find_files_with_start(start_str: str) -> list:
    list_with_start = [i for i in os.listdir(path='.') if i.startswith(start_str)]
    return list_with_start
def find_files_with_end(end_str: str) -> list:
    list_with_end = [i for i in os.listdir(path='.') if i.split('.')[-2].endswith(end_str)]
    return list_with_end
def find_files_with_str(search_str: str) -> list:
    list_with_str = [i for i in os.listdir(path='.') if search_str in i]
    return list_with_str
def find_files_with_expansion(extension: str) -> list:
    list_with_expansion = [i for i in os.listdir(path='.') if i.endswith(extension.rstrip())]
    return list_with_expansion
def choose_option_1() -> None:
    list_with_pdf = find_pdf_files()
    for i in range(len(list_with_pdf)):
        print(f"{i + 1}. {list_with_pdf[i]}")
    print()
    number_pdf = input(
        ('Введите номер файла для преобразования в Docx (чтобы преобразовать всё, введите 0; для отмены -1): ')).strip()
    if number_pdf == '0':
        for i in range(len(list_with_pdf)):
            convert_pdf_to_docx(list_with_pdf[i])
        print(f'Преобразование файлов в каталоге из PDF в Docx прошло успешно!')
    elif number_pdf == '-1':
        print()
    else:
        convert_pdf_to_docx(list_with_pdf[int(number_pdf) - 1])
        print(f'Преобразование файла {list_with_pdf[int(number_pdf) - 1]} из PDF в Docx прошло успешно!')
def choose_option_2() -> None:
    list_with_docx = find_docx_files()
    for i in range(len(list_with_docx)):
        print(f"{i + 1}. {list_with_docx[i]}")
    print()
    number_docx = (input(('Введите номер файла для преобразования в PDF (чтобы преобразовать всё, введите 0; для отмены -1): ')))
    if number_docx == '0':
        for i in range(len(list_with_docx)):
            convert_pdf_to_docx(list_with_docx[i])
        print(f'Преобразование всех файлов в каталоге из Docx в PDF прошло успешно!')
    elif number_docx == '-1':
        print()
    else:
        convert_docx_to_pdf(list_with_docx[int(number_docx) - 1])
        print(f'Преобразование файла {list_with_docx[int(number_docx) - 1]} из Docx в PDF прошло успешно!')
def images_in_directory() -> list[str]:
    images = []
    for file in os.listdir():
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            images.append(file)
    return images
def compression_image(file: str, compression_k: int) -> None:
    '''Реализация функции сжатия изображения'''
    pass
def chosen3() -> None:
    '''Выбор 3 в меню. Функция выводит результат функции нахождения изображений в директории.
Выводит эти файлы.Потом пользователь вводит команду для сжатия изобржаений.
Если 0, то преобразуются все файлы, если -1, то действие отменяется, и мы возвращаемся в меню.'''
    list_with_images = images_in_directory()
    for i, image in enumerate(list_with_images, start=1):
        print(f"{i}. {image}")
    print()
    number_images = int(input(('Введите номер файла для сжатия (чтобы сжать всё, введите 0, для отмены -1): ')))
    compression_k = int(input('Введите на сколько надо сжать изображение от 0 до 95: '))
    if number_images == 0:
        for image in list_with_images:
            compression_image(image, compression_k)
        print('Все изображения из каталога сжаты!')
    elif number_images == -1:
        print()
    else:
        compression_image(list_with_images[number_images - 1], compression_k)
        print(f'Изображение {list_with_images[number_images - 1]} успешно сжато!')
def delete_file(path: str) -> None:
    if os.path.isfile(path):
        os.remove(path)
    else:
        for root, dirs, files in os.walk(path, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(path)
def delete(path: str) -> bool:
    if not os.path.exists(path):
        return False
    delete_file(path)
    return True
def delete_files_with_start(start_str: str) -> None:
    'Удаляет все файлы, начинающиеся с заданной строки.'
    files = [file for file in os.listdir() if file.startswith(start_str)]
    for file in files:
        delete(file)
def delete_files_with_end(end_str: str) -> None:
    '''Удаляет все файлы, заканчивающиеся заданной строкой.'''
    files = [file for file in os.listdir() if file.endswith(end_str)]
    for file in files:
        delete(file)
def delete_files_with_str(sub_str: str) -> None:
    '''Удаляет все файлы, содержащие заданную подстроку.'''
    files = [file for file in os.listdir() if sub_str in file]
    for file in files:
        delete(file)
def delete_files_with_extension(extension: str) -> None:
    '''Удаляет все файлы с заданным расширением.'''
    files = [file for file in os.listdir() if file.lower().endswith(f".{extension}")]
    for file in files:
        delete(file)
def deleted(choice: str) -> None:
    '''Программа вызывается от chosen 4.
Если выбираем 1, то удаляем по началу строки
2: удаляем все файлы по концу введённой строки
3: удаляем все файлы с введённой подстрокой
4: удаляем все файлы по введённому расишрению'''
    if choice == '1':
        start_str = input('Введите начало строки, с которой хотите удалить файл: ')
        delete_files_with_start(start_str)
    elif choice == '2':
        end_str = input('Введите конец строки, с которой хотите удалить файл: ')
        delete_files_with_end(end_str)
    elif choice == '3':
        sub_str = input('Введите подстроку, с которой хотите удалить файл: ')
        delete_files_with_str(sub_str)
    elif choice == '4':
        extension = input('Введите расширение, с которым хотите удалить файлы: ')
        delete_files_with_extension(extension)
def chosen4() -> None:
    '''Интерфейс выбора 4 в главном меню.'''
    print('1. Удалить все файлы, начинающиеся на определенную подстроку')
    print('2. Удалить все файлы, заканчивающиеся на определенную подстроку')
    print('3. Удалить все файлы, содержащие определенную подстроку')
    print('4. Удалить все файлы по расширению')
    choice = input('Введите номер команды: ')
    deleted(choice)