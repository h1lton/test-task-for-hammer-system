<a name="readme-top"></a>
<br>
<div align="center">
  <a href="https://github.com/h1lton/test-task-for-hammer-system">
    <img src="https://img.icons8.com/?size=80&id=rT0QUnswQvfg&format=png" alt="Logo">
  </a>
  <h3>Referral System</h3>
  <p>
    Тестовое задание на DRF
    <br>
    <a href="https://github.com/h1lton/test-task-for-hammer-system"><strong>Explore the docs »</strong></a>
    <br>
    <br>
  </p>

  <img src="https://skillicons.dev/icons?i=py,django,postgres,docker,postman&theme=light" alt="Tech">

  <p>
    <br>
    <a href="https://github.com/h1lton/test-task-for-hammer-system">View Demo</a>
    ·
    <a href="https://github.com/h1lton/test-task-for-hammer-system/issues">Report Bug</a>
    ·
    <a href="https://github.com/h1lton/test-task-for-hammer-system/issues">Request Feature</a>
    ·
    <a href="https://documenter.getpostman.com/view/29629600/2s9YJhxfiX">Postman Collection</a>
  </p>
</div>


<details>
  <summary>Оглавление</summary>
  <ol>
    <li><a href="#задание">Задание</a></li>
    <li><a href="#стек-технологий">Стек технологий</a></li>
    <li><a href="#установка">Установка</a></li>
    <li>
      <a href="#функционал">Функционал</a>
      <ul>
        <li><a href="#верификация">Верификация</a></li>
        <li><a href="#профиль">Профиль</a></li>
      </ul>
    </li>
    <li><a href="#тестирование">Тестирование</a></li>
    <li><a href="#примечание">Примечание</a></li>
  </ol>
</details>

## Задание

Реализовать простую реферальную систему. Минимальный интерфейс для тестирования

Реализовать логику и API для следующего функционала :

- Авторизация по номеру телефона. Первый запрос на ввод номера телефона.
  Имитировать отправку 4х значного кода авторизации. Второй запрос на ввод кода.

- Если пользователь ранее не авторизовывался, то записать его в бд.

- Запрос на профиль пользователя.

- Пользователю нужно при первой авторизации нужно присвоить рандомно сгенерированный
  6-значный инвайт-код(цифры и символы).

- В профиле у пользователя должна быть возможность ввести чужой инвайт-код(при вводе проверять на существование).
  В своем профиле можно активировать только 1 инвайт код, если пользователь уже когда-то активировал инвайт код,
  то нужно выводить его в соответсвующем поле в запросе на профиль пользователя.

- В API профиля должен выводиться список пользователей(номеров телефона),
  которые ввели инвайт код текущего пользователя.

- Реализовать и описать в readme Api для всего функционала.

- Создать и прислать Postman коллекцию со всеми запросами. ([Вот она](https://documenter.getpostman.com/view/29629600/2s9YJhxfiX))

<p align="right">(<a href="#readme-top">вернуться наверх</a>)</p>

## Стек технологий

- <img src="https://skillicons.dev/icons?i=py&theme=light" alt="icon" style="width: 25px"> Python 3.9
- <img src="https://skillicons.dev/icons?i=django&theme=light" alt="icon" style="width: 25px"> Django 4.2.5
- <img src="https://skillicons.dev/icons?i=django&theme=light" alt="icon" style="width: 25px"> Django REST Framework 3.14.0
- <img src="https://skillicons.dev/icons?i=django&theme=light" alt="icon" style="width: 25px"> drf-yasg 1.21.7
- <img src="https://skillicons.dev/icons?i=django&theme=light" alt="icon" style="width: 25px"> django-phonenumber-field 7.1.0
- <img src="https://skillicons.dev/icons?i=postgres&theme=light" alt="icon" style="width: 25px"> Postgres
- <img src="https://skillicons.dev/icons?i=docker&theme=light" alt="icon" style="width: 25px"> Docker & Docker Compose
- <img src="https://skillicons.dev/icons?i=postman&theme=light" alt="icon" style="width: 25px"> Postman

<p align="right">(<a href="#readme-top">вернуться наверх</a>)</p>

## Установка

1. Клонируйте репозиторий
   ```sh
   git clone https://github.com/h1lton/test-task-for-hammer-system.git
   cd test-task-for-hammer-system
   ```
2. Создайте файл .env
   ```sh
   cp .env.example .env
   ```
   _Можете поменять поля связанные с DB и SECRET_KEY,
   вот [link](https://djecrety.ir/) для быстрого создания секретного ключа._
3. Запустите контейнеры
   ```sh
   docker-compose up
   ```
   _1 примечание: если будите запускать в первый раз, это займёт продолжительный промежуток времени._

   _2 примечание: если у вас нету логов в консоли, пропишите следующую команду:_
   ```sh
   docker-compose logs -f
   ```
4. Выполните миграции
   ```sh
   docker-compose exec dj python manage.py migrate
   ```
5. Проверьте работоспособность по http://localhost:8000/docs/ должна открыться документация.

<p align="right">(<a href="#readme-top">вернуться наверх</a>)</p>

## Функционал

Здесь описан функционал в общих чертах, если хотите узнать более подробную
информацию о endpoints обратитесь в [документацию](http://localhost:8000/docs/).

### Верификация

Верификация нужна что-бы получить токен авторизации, он нужен для доступа к функционалу с профилем.

Процесс верификации:

1. Отправьте POST запросом в `/verf/send_code/` номер телефона в любом формате с кодом региона.

   ```json
   {
      "tel": "+79993451234"
   }
   ```
   Вы должны получить 204 статус код.

   Данный endpoint отправит на указанный номер телефона код верификации.

   Примеры форматов номера телефона:
   - +79993451234
   - +7 (999) 345 12-34
   - +7-999-345-12-34

   Примеров можно привести сотни, самое главное все они должны подражать первому примеру.

2. Далее мы должны полученный код передать POST запросом в `/verf/check_code/`.

   ```json
   {
      "tel": "+79993451234",
      "code": "8093"
   }
   ```

   Вы должны получить токен авторизации.

   ```json
   {
      "auth_token": "2b2ea1f18dea1esa5c5s7cba133c99c1b8cc2zf"
   }
   ```
   _Примечание: так как мы используем имитацию отправки sms с кодом, на самом деле он выводится в логи._

Более подробная информация об endpoints в [документации](http://localhost:8000/docs/).

<p align="right">(<a href="#readme-top">вернуться наверх</a>)</p>

### Профиль

Что бы получить доступ нужно в header указать токен авторизации следующим образом:

| Key           | Value              |
|---------------|--------------------|
| Authorization | Token `auth_token` |

В нём можно:

1. Получить профиль в котором есть информация:
    - Номер телефона пользователя.
    - Реферальный код пользователя.
    - Введённый реферальный код.
    - Все номера телефонов рефералов. (Referrals - люди которые вводили реферальный код реферера)
2. Установить реферера по его реферальному коду. (Referrer - человек который пригласил реферала)

<br>

- Что бы получить профиль мы должны отправить GET запрос в `/profile/`.

  Так выглядит профиль с рефералами и введённым реферальным кодом:
  ```json
  {
    "tel": "+79993451234",
    "your_ref_code": "ba3с44",
    "used_ref_code": "a98ak38",
    "referrals": [
      "+79056881199",
      "+79085059889",
      "+79995552244",
      "+79117005050"
    ]
  }
  ```
- Что бы установить реферера передайте его реферальный код POST запросом в `/profile/referrer/` следующим образом:
  ```json
  {
    "ref_code": "a98ak38"
  }
  ```
  Если реферер будет успешно установлен вы получите 204 статус код.

Более подробная информация об endpoints в [документации](http://localhost:8000/docs/).

<p align="right">(<a href="#readme-top">вернуться наверх</a>)</p>

## Тестирование

Что бы запустить тесты:

```sh
docker-compose exec dj python manage.py test
```

Предварительно у вас должны быть запущены контейнеры.

<p align="right">(<a href="#readme-top">вернуться наверх</a>)</p>

___

p.s. Делал это тестовое чисто для себя, взял его из данного [репо](https://github.com/yury-yury/hammer_system)
