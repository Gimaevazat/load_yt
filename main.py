import os
import shutil
import argparse
from load_urls import load_urls_from_txt
from yt_load import load_video_and_audio
from make_video import merge_video_audio
from pytubefix.helpers import reset_cache


if __name__ == '__main__':
    #Парсим доп аргументы
    parser = argparse.ArgumentParser(description="Пример использования флагов в Python.")
    parser.add_argument('-r', '--reset_cache', action='store_true',
                        help='Установите этот флаг для сброса кэша')
    parser.add_argument('-d', '--delete_temp', action='store_true',
                        help='Удалять временные файлы после создания итогового видео. Уменьшает кол-во занятой памяти')

    args = parser.parse_args()

    #Загрузка url'ов из файла
    urls = load_urls_from_txt('urls.txt')

    #Сброс кэша, если установлен флаг
    if args.reset_cache:
        reset_cache()

    titles = []
    for index, url in enumerate(urls):
        #Загрузка видео и аудио
        title = load_video_and_audio(url, output_path=str(index))
        #Запись названий видосов
        titles.append(title)

    #Удаляем папку, где будут храниться итоговые видосы
    #Да, харкод. А что ты мне сделаешь, я в другом городе за мат извени?
    if os.path.exists('result_videos') and os.path.isdir('result_videos'):
        shutil.rmtree('result_videos')
    #Создаем папку, где будут храниться итоговые видосы
    os.mkdir('result_videos')

    print('\n---------------------------------\n')
    print('Склейка')

    #Склейка видео с аудио
    for index, title in enumerate(titles):
        #Видеофайл
        video_path = './' + str(index) + '/video.mp4'
        #Аудиофайл
        audio_path = './' + str(index) + '/audio.m4a'
        #Итоговый файл
        #title[0:20] нужен, тк при больших названиях код сыпется
        outputfile = './result_videos/' + title[0:20] + '.mp4'

        print('Создается ' + title)

        #Склейка видео с аудио
        merge_video_audio(video_path, audio_path, outputfile)

        print(title + ' готов')

        #Удаляем "временные" файлы, если флаг установлен
        if args.delete_temp:
            shutil.rmtree('./' + title)
