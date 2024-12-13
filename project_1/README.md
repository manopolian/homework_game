# Проект 1. Угадай число.

## Оглавление  
[1. Описание проекта](https://github.com/manopolian/homework_game/tree/first_commit/project_1/README.md#Описание_проекта)  
[2. Какой кейс решаем?](https://github.com/manopolian/homework_game/tree/first_commit/project_1/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/manopolian/homework_game/tree/first_commit/project_1/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/manopolian/homework_game/tree/first_commit/project_1/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/manopolian/homework_game/tree/first_commit/project_1/README.md#Результат)    
[6. Выводы](https://github.com/manopolian/homework_game/tree/first_commit/project_1/README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](https://github.com/manopolian/homework_game/tree/first_commit/project_1/README.md#Оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая загадывает число и угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python.
Работать c платформой GIT HUB


### Краткая информация о данных 

...........
  
:arrow_up:[к оглавлению](https://github.com/manopolian/homework_game/tree/first_commit/project_1/README.md#Оглавление)


### Этапы работы над проектом  
- написали код для игры угадай число, где компьютер загадывает - мы угадываем
- создали функцию random_predict ([type]) для угадывания числа за наименьшее число попыток используя код первой игры и усовершенствовали поиск с помощью наименьшего и наибольшего значений.
- создали функцию score_game(random_predict), где первая является аргументом второй и находим среднее зачение колличества попыток за 1000 повторений

:arrow_up:[к оглавлению](https://github.com/manopolian/homework_game/tree/first_commit/project_1/README.md#Оглавление)

### Результаты: 

- среднее колличество выходит 5 попыток, после проведения небольшого тестирования было выявлено, что при разных значениях повторений результат варьируется от 5 до 9 попыток. 

:arrow_up:[к оглавлению](https://github.com/manopolian/homework_game/tree/first_commit/project_1/README.md#Оглавление)


### Выводы:  
- с помощью бинарного поиска получили практически минимальное колличество попыток угадывания числа. 

:arrow_up:[к оглавлению](https://github.com/manopolian/homework_game/tree/first_commit/project_1/README.md#Оглавление)
