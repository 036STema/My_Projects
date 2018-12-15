import requests

URL = 'https://translate.yandex.net/api/v1/tr.json/translate'
params = 'id=32096114.5c0c2f12.baa47f5f-0-0&srv=tr-text&lang=%s-ru&reason=paste'

def translate(text_for_translate, lang):
    response = requests.post(URL, data={'text': text_for_translate}, params=params % lang)
    body = response.json()
    return body['text']


def translate_file(enter_path, lang, write_file):
    with  open(enter_path, 'r') as file_txt:
        for line in file_txt:
            text_translate = translate(line, lang)
            with  open(write_file, 'a') as new_file:
                new_file.write(text_translate[0])

def write_files(file):
    with  open(file, 'w') as new_file:
        new_file.write(body['text'])

if __name__ == '__main__':
    enter_an_action = input('Ввод текста = "i" , Перевод файла = "r" ')
    enter_an_action = enter_an_action.lower()
    if enter_an_action == 'i':
        lang = input('С какого языка перевести  ')
        text = input('Введите текст для перевода ')
        text_after_translate = translate(text, lang)
        print(text_after_translate)
    elif enter_an_action == 'r':
        enter_path = input('Укажите путь к файлу для перевода')
        lang = input('С какого языка перевести  ')
        write_file = input('Куда записать файл')
        text_after_translate = translate_file(enter_path, lang, write_file)
      

