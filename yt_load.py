from pytubefix import YouTube
from pytubefix.cli import on_progress

#Тк ютуб забанен из России, то нужно прокси
proxies = {
    'http': f'http://user:pass@IP:PORT',
    'https': f'http://user:pass@IP:PORT',
}

def load_video_and_audio(url: str, output_path: str):
    '''
    Загрузка видео и аудио
    Видео загружается в самом высоком разрешении. Аудио в видео не гарантируется
    :param url:
    Url видео
    :param output_path:
    Путь, куда будут сохраняться файлы
    :return:
    Название видео с ютуба
    '''
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback=on_progress, proxies=proxies)
    print('Загружается ' + yt.title)

    #Загрузка видео
    video = yt.streams.get_highest_resolution(progressive=False)
    video_path = video.download(output_path = output_path, filename = 'video.mp4')

    #Загрузка аудио
    audio = yt.streams.get_default_audio_track()
    audio_path = audio.first().download(output_path = output_path, filename = 'audio.m4a')

    return yt.title
