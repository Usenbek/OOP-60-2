import emoji
# внешняя библиотека эмодзи

print(emoji.emojize('Python is :thumbs_up:'))  # превращает текстовое значение определенного эмодзи в символ самого эмодзи
# Python is 👍
print(emoji.demojize('Python is 😂')) # превращает символ эмодзи в текст обозначающий эту эмодзи
# Python is :face_with_tears_of_joy:
print(emoji.emojize('Python is :thumbsup:', language='alias'))
# Python is 👍 # позволяет сократить написание текстового эмодзи
print(emoji.emojize("Python is fun :red_heart:"))
# Python is fun ❤ (возможно в терминале оно отобразится как красное сердце в связи новой версией виндоуса или самой настроек консоли которые показывают автоматически перекрашенное красное сердце
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
# Python is fun ❤️ # это стопроцентно должно давать в терминале красное сердце
print(emoji.is_emoji("❤️"))
# True # проверяет, является ли символ эмодзи показывая в терминале булевое значение