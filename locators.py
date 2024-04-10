from selenium.webdriver.common.by import By

class SBurgersLocators:
    PERSONAL_ACCOUNT_BUTTON_MAIN = (By.XPATH, "//p[text()='Личный Кабинет']") #кнопка Личный кабинет на главной странице
    BUTTON_AUTHORIZATION_MAIN = (By.XPATH, "//button[text() = 'Войти в аккаунт']")  # кнопка Войти в аккаунт на главной странице
    REGISTRATION_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']") #кнопка Зарегистрироваться на странице авторизации
    REGISTRATION_INPUT_NAME = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input") #поле Имя на странице регистрации
    REGISTRATION_INPUT_EMAIL = (By.XPATH, "//label[text() = 'Email']/following-sibling::input") #поле Email на странице регистрации
    REGISTRATION_INPUT_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input") #поле Пароль на странице регистрации
    REGISTRATION_FINISH_BUTTON = (By.XPATH, ".//form/button[text()='Зарегистрироваться']") #кнопка Зарегистрироваться на странице регистрации
    INCORRECT_PASSWORD_ELEMENT = (By.CLASS_NAME, "input__error") #сообщение некорректный пароль под полем Пароль на странице регистрации
    AUTHORIZATION_INPUT_EMAIL = (By.XPATH, "//input[@name='name']") #поле Email на странице авторизации
    AUTHORIZATION_INPUT_PASSWORD = (By.XPATH, "//input[@name='Пароль']") #поле Пароль на странице авторизации
    AUTHORIZATION_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") #кнока Войти на странице авторизации
    AUTHORIZATION_BUTTON_REGISTRATION_FORM = (By.XPATH, "//a[text()='Войти']") #кнопка Войти на странице регистрации
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']") #кнопка Восстановить пароль на странице авторизации
    AUTHORIZATION_BUTTON_RESTORE_PASSWORD = (By.XPATH, "//a[text()='Войти']") # кнопка Войти на странице восстановления пароля
    CONSTRUCTOR_BUTTON = (By.CLASS_NAME, "AppHeader_header__linkText__3q_va")  # кнопка Конструктор
    LOGO_BUTTON = (By.CSS_SELECTOR, "svg") # Логотип
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']") #кнопка Выход в личном кабинете
    STUFFING_BUTTON = (By.XPATH, "//span[text() = 'Начинки']") #кнопка Начинки в конструкторе
    SAUCES_BUTTON = (By.XPATH, "//span[text() = 'Соусы']") #кнопка Соусы в конструкторе
    BUNS_BUTTON = (By.XPATH, "//span[text() = 'Булки']") #кнопка Булки в конструкторе
    MAKE_BURGER_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']") #текст Соберите бургер на главной странице
    ENTER_TEXT = (By.XPATH, "//h2[text()='Вход']") #текст Вход на странице авторизации