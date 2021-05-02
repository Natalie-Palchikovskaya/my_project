# Разработка приложения, распознающего по изображениям названия растений #

## Цель проекта ##
Раннее была создана нейронная сеть, определяющая вид растения по его изображению. На данных момент она способна распознавать
15 видов цветов:
- ромашка
- одуванчик
- ирис
- лаванда
- лилия
- сирень
- лотос
- нарцисс
- орхидея
- пион
- мак
- роза
- сакура
- подсолнух 
- тюльпан

В рамках данного проекта необходимо создать графический интерфейс, позволяющий  пользователю загрузить фото цветка и получить его название.

## Результаты проекта ##
C помощью модуля PyQt5 был написан GUI, который решает поставленную задачу. Для начала работы следует запусить файл 
gui2.py. Тогда появится следующее окно:

![alt text](https://github.com/Natalie-Palchikovskaya/my_project/blob/main/GUI.png "Logo Title Text 1")

При нажатии на кнопку "Download picture" можно загрузить фото растения. Для получения ответа следует нажать клавишу "What 
is the flower?"

![alt text](https://github.com/Natalie-Palchikovskaya/my_project/blob/main/res_gui.png "Logo Title Text 1")

Accuracy показывает точность, с которой определен данный цветок.

## Дальнейшие планы развития проекта ##

В дальнейшем планируется сделать загрузку фотографии более легкой (например, через проводник или посредством перетаскивания картинки) и добавить краткую информацию о каждом цветке.


## Обновленная версия проекта ##

В новой версии проекта существенно упростилась подгрузка изображения. Теперь при нажатии кнопки "Download picture" запускается проводник, реализующий доступ пользователя к файлам операционной системы.

![alt text](https://github.com/Natalie-Palchikovskaya/my_project/blob/main/example1.png)

Также теперь, помимо определения цветка по фотографии, приложение дает краткую информацию по каждому распознанному растению.

![alt text](https://github.com/Natalie-Palchikovskaya/my_project/blob/main/example2.png)

Для использования новой версии программы необходимо скачать папку "project_new_version" и запросить обученную нейронную сеть у разработчика.




