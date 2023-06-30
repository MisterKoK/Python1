from nicegui import ui
from pytube import YouTube
import time


class Demo:
    def __init__(self):
        self.number = 0.00

    def progressbar(self):
        for i in range(10):
            time.sleep(0.10)
            self.number = self.number + 0.10
        self.number = round(self.number)

demo = Demo()

def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")
    ui.notify(f'Download is completed successfully!')


def notif():
    ui.notify(f'Загрузка началась!')
    global link
    link = input.value
    print('Вы скачиваете это видео: ', link)
    download(link)
    demo.progressbar()


# наведем красоту с расположением элементов
with ui.row():
    with ui.avatar('favorite_border', text_color='grey-11', square=True):
        ui.tooltip('I like this').classes('bg-green')
    with ui.column():
        ui.label('Загрузчик с Ютуба').style('color: #85004B; font-weight: bold')
        ui.label('Keva Downloader').style('color: #85004B; font-weight: bold')

with ui.column():
    input = ui.input(label='Вставьте ссылку', placeholder='start typing',
                 on_change=lambda e: result.set_text('Вы напечатали: ' + e.value),
                 validation={'Input too long': lambda value: len(value) < 300},
                 )
    result = ui.label()
    input.props("size=80")  # ширина поля ввода ссылки

    slider = ui.slider(min=0, max=1, step=0.10).bind_value(demo, 'number')



# группирую кнопку и прогресс бар
with ui.row():
    ui.button('Download!', on_click=notif)
    # Прогресс бар
    ui.spinner('dots', size='lg', color='red')
    ui.circular_progress().bind_value_from(slider, 'value')
    ui.linear_progress().bind_value_from(slider, 'value')

ui.link('Связаться с автором', 'https://vk.com/misterkok')


# кнопки меняют фон
def set_background(color: str) -> None:
    ui.query('body').style(f'background-color: {color}')

with ui.row():
    ui.button('Blue', on_click=lambda: set_background('#ddeeff'))
    ui.button('Orange', on_click=lambda: set_background('#ffeedd'))

ui.run(title='Keva Downloader')
