Обучающая выборка находится в файле X.mat. Она представлена из landmark'ов из папки example_data\landmarks\, которые были даны.
Данные с метками находятся в файлах y_om.mat (neutral = 0, open mouth = 1) и y_smile.mat (neutral = 0, smile = 1).
Для y_om.mat метки с 1 были взяты для картинок из папки example_data\open_mouth\.
Для y_smile.mat метки с 1 были взяты для картинок из папки example_data\smile\.
Метки с 0 были взяты для остальных картинок из папки example_data\images\.
Соответственно, обучение происходило по методу опорных векторов как для open_mouth (строка 31, в SVC_om), где в качестве меток брались y_om, так и для smile (строка 39, в SVC_smile), где в качестве меток брались y_smile.

Для вычисления положений landmark'ов по тестируемому изображению использовались данные shape_predictor_68_face_landmarks.dat (не представлена в репозитории) а также dlib (устновка по инструкции Marco D.G. в https://stackoverflow.com/questions/41912372/dlib-installation-on-windows-10).

Запуск производится с командной строки, например:
python Detection_project_GIT.py "img1.jpg" "img2.jpg" "img3.jpg"
