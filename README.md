## Комментарии к заданию №1
В рамках выполнения задания я проанализировал предоставленную страницу и выделил основные баги, которые могут негативно повлиять на пользовательский опыт или репутацию компании. Основные проблемы были оформлены в виде отчётов о дефектах (папка Task-1). Остальные замечания, я перечислю ниже:

>(хоть в задании сказано просто перечислить все имеющиеся баги)

#### Проблема с отображением категорий:
- Если идти по категориям `Главная > Хобби и отдых > Велосипеды > Горные`,
 то последняя выбранная категоря `Горные` не будет отображаться
 (Сразу под логотипом Avito). Не критично ведь у нас есть выбор категории в фильтрации

#### Ошибка в тексте кнопки:
 - На кнопке `Все категории` не хватает буквы второй `И`. 
 Не критично но думаю, пользователи буду обращать на это внимание

#### Неточность в описании объявления:
 - Последнее объявление MTB A-gang Gangsta в до метро трикотажная идти `11 - 15 ч.` Не критично, но может вводить в заблуждение.
 (Возможно, это связано с интеграцией с сервисами Яндекса)

___
 Плашка `Попробуйте обновить страницу или загляемте позже - мыобязательно всё починим.` вводит в заблуждение, как на неё реагировать и при каких условиях она появляется - неизвестность
.
___

Аномальное объявление с велосипедом `Atom 240ds`, при поиске бренда Author, без цены, с неправильным отображением города и метро.
То, что нет цены это баг и выпало из сначала из липецка, а не из Москвы и впринципе это не подходящее под фильтры. Но если нет подходящих объявлений поиск будет подсовывать другие варианты, с этим я часто сталкиваюсь, когда сам смотрю объявления на сайте. 
Сейчас если на Авито применить такие фильтры с брендом Author в поиске будут пирожки (скрины прикреплю ниже)
___

В баг-репорте №4 я подсвечиваю количество страниц, хотя при 61 объявлении должно быть не 100 страниц, а ~5. Но иногда на сайте действительно присутствуют пустые страницы (скрин ниже)

___

### Ограничения тестового задания

Так как задание выполняется на основе статичной картинки, у меня нет возможности:
- Взаимодействовать с системой и наблюдать её поведение в реальном времени.
- Уточнить требования или изучить документацию(авито документация/портал разработчика - не даёт информацию о том как это должно работать на самом деле)
- Проверить логи или получить дополнительную информацию для анализа.

___

Постарался максимально подробно описать все обнаруженные проблемы. В работе ориентировался на улучшение пользовательского опыта и минимизацию рисков для репутации компании. Если бы у меня была возможность взаимодействовать с системой, можно было бы провести более глубокий анализ.

___

### Скрины:

### Пустые страницы
![Header](https://github.com/GitHoms/Avito-Internship-assignments-2025/blob/main/Assets/EmptyP.jpg?raw=true)
### Пирожки
![Header](https://github.com/GitHoms/Avito-Internship-assignments-2025/blob/main/Assets/real.jpg?raw=true)
