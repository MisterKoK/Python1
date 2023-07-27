from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window
Window.size = (480, 853)
from googletrans import Translator

# запуск экранной клавиатуры
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')


class Container(GridLayout):

    def translate_text(self):
        text_input = self.text_input.text

        if text_input:
            try:
                translator = Translator()
                translation1 = translator.translate(text_input, dest='en')
                translation2 = translator.translate(text_input, dest='vi')

                self.english_label.text = translation1.text
                self.vietnamese_label.text = translation2.text

                #self.output_label.text = translation.text
            except:
                self.english_label.text = 'Ошибка при переводе'
                self.vietnamese_label.text = 'Ошибка при переводе'
        else:
            self.english_label.text = 'Введите текст для перевода'

    def clear_text(self):
        self.text_input.text = ''

class TranslatorApp(App):  # Наш класс будет наследовать свойства от App
    title = 'Keva Translator'

    def build(self):  # Этот метод создает окно и выводит виджеты
        return Container()


if __name__ == '__main__':
    TranslatorApp().run()

