from googletrans import Translator
translator = Translator()

def trans(text_input):
    translation1 = translator.translate(text_input, dest='en')
    translation2 = translator.translate(text_input, dest='vi')
    trans1 = translation1.text
    trans2 = translation2.text
    return trans1, trans2

def transru(text_input):
    translation1 = translator.translate(text_input, dest='en')
    translation2 = translator.translate(text_input, dest='ru')
    trans1 = translation1.text
    trans2 = translation2.text
    return trans1, trans2
