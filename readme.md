# Обрезка ссылок с помощью VK

С помощью данного скрипта можно обрезать(укоротить) ссылку через VK_API, а также, получить информацию о количество переходов по укороченной ссылке.

##Окружение

Для работы скрипта понадобится [сервисный токен VK](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/tokens/service-token).
Если нету аккаунта в VK [зарегестрируйтесь](https://vk.com/).


##Зависимости

Необходимые библиотеки указаны в файле `requirements.txt`. Для установки зависимостей можно воспользоваться командой `pip3 install -r requirements.txt`.

###Переменные окружения

Сервисный токен приложения выглядит примерно так: `82a02da882a02da882a02da8a981b7f3cc882a082a02da8e4af9c41e8551329276dde72`.
После получения сервисного токена необходимо его записать в файл `.env`, который должен находится в корневой папке скрипта.
Название переменной необходимо записать как `VK_API_TOKEN`.
Пример: `VK_API_TOKEN=82a02da882a02da882a02da8a981b7f3cc882a082a02da8e4af9c41e8551329276dde72`.

## Запуск

Скрипт подчиняется простой логике: если ссылка укорочена с помощью VK - показывает статистику переходов по ссылке, если нет, то укорачивает её с помощью VK API.
Ссылку необходимо передать сразу при запуске скрипта: `~\User\VK\python main.py https:\\some.url`.