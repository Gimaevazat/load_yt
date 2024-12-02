import subprocess


def merge_video_audio(video_path, audio_path, outputfile):
    '''
    Склейка видео и аудио с помощью ffmpeg

    :param video_path:
    Имя видеофайла с путем
    :param audio_path:
    Имя аудиофайла с путем
    :param outputfile:
    Имя результирующего файла с путем
    '''
    subprocess.run(f'ffmpeg -i \"{video_path}\" -i \"{audio_path}\" -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -hide_banner -loglevel error \"{outputfile}\"')
