# K2It-Intermship
This is the work that I was making at an intermship in K2It.
Readme (Russian language only):
Представляю свой скрипт для проекта по бегопоиску.
Данный скрипт позволяет получить данные о спортивных мероприятиях и записать их в csv-файл, который можно открыть и просматривать в виде таблицы в Microsoft excel.
Приведу сайты, с которых выкачивается информация.
http://russiarunning.com/events
http://reg.place
http://trilife.ru
http://iron-star.com

Необходимые компоненты для работы скрипта:
Для работы скрипта вам необходимы следующие компоненты:
1.	Браузер google chrome
2.	Chrome driver для работы с вебстраницами (он уже лежит в папке «скрипт» рядом с файлом скрипта и запускным файлом).
3.	Среда python. Ее вы сможете скачать с офсайта: http://python.org

Использование:
1.	Убедитесь, что все вышеприведенные компоненты установлены, иначе, скрипт просто откажется работать.
2.	В папке «скрипт» запустите файл «запуск.bat», если вы работаете в windows. Если вы работаете в macOS, то лучше запускать программу через терминал, который вы сможете найти в папке утилит. Ее можно открыть сочитанием command+shift+u, находясь в finder.
3.	Запустите скрипт с помощью приведенных выше способов. При успешном запуске скрипта у вас должен открыться браузер google chrome и скрипт должен начать работу. Он выкачает данные с четырех сайтов, затем скрипт запишет данные в csv-файл, а затем браузер закроется и скрипт можно будет закрыть. В папке, где вы запускали скрипт, должен появится файл «data.csv”. Если его открыть, то вы увидите таблицу excel с полученными данными. В качестве примера готового файла в папке с проектом вы сможете найти точно такой же файл “data.csv”, который я положил в качестве примера.
Скрипт будет перезаписывать данные в файл каждый раз, когда вы его будете запускать.
Примечание:
В windows при запуске скрипта появиться ошибка о том, что не удается найти драйвер chrome. Чтобы исправить ее, попробуйте в файле закоментировать строчку, начинающуюся со слова “path”, а в строке browser = webdriver.Chrome(path) уберите слово “path” из скобок. Должно все заработать.


