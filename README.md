# yandex.video.dowloader
Скрипт скачивает любое видео с Яндекс.Диска.
Для работы необходимо экспортировать файл со ссылками в формате .csv (как в примере), а также установить yt_dlp:

pip install yt-dlp

Желательна установка ffmpeg.

Опционально можно использовать (например, для скачивания низкого качества mp4-видео с хорошим звуком):
    ydl_opts = {'cookiefile':'cookies.txt',
                'quality':'worstvideo',
                'format':'mp4',
                'merge-output-format':'mp4'}

Другой проект, также скачивающий видео Яндекса через API: https://github.com/uglev/yadi.sk
