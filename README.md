В проекте содержатся следующие тесты:

test_successful_registration.py - проверяет успешную регистрацию пользователя с валидными данными

test_unsuccessful_registration.py - проверяет отказ в регистрации пользователя с невалидными данными (пароль из пяти цифр)

test_authorization_main.py - вход по кнопке «Войти в аккаунт» на главной странице

test_authorization_personal_account.py - вход через кнопку «Личный кабинет»

test_authorization_registration_form.py - вход через кнопку в форме регистрации

test_forgot_password_authorization.py - вход через кнопку в форме восстановления пароля

test_transition_personal_account.py - переход по клику на «Личный кабинет».

test_transition_constructor.py - переход по клику на «Конструктор»

test_transition_logo.py - переход по клику на логотип Stellar Burgers

test_exit.py - выход по кнопке «Выйти» в личном кабинете

test_go_to_sections.py - переходы к разделам: «Булки», «Соусы», «Начинки».

В файле locators.py хронятся локаторы

В файле conftest.py хронится фикстура

В файле settings.py хранится ссылка на главную страницу сайта

В файле date.py хранятся Имя пользователя, Email, корректный пароль и некорректный пароль# Sprint_5
