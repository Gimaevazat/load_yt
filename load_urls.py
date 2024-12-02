def load_urls_from_txt(txt_name: str = 'urls.txt') -> list:
    '''
    Выгрузка url из файла

    :param txt_name:
    Название файла с url

    :return:
    Массив с url
    '''
    with open(txt_name, 'r') as file:
        lines = file.readlines()

    urls = [line.strip() for line in lines]

    return urls


if __name__ == '__main__':
    print(load_urls_from_txt())
    print(r'/\:*?<>|')
