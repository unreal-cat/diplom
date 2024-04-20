# -*- coding: utf-8 -*-
# РАЗРАБОТКА ОТ T.ME/FELIX4
from json import loads
from secrets import token_hex


class Authorization:

    def __init__(self) -> None:
        """Процессы авторизации на сайте
        :modul: get_accounts() - Получение всех аккаунтов
        :modul: get_config() - Получение данных из config.json
        :modul: check_login() - Проверка входящего логина в базе 
        :modul: check_password() - Проверка входящего логина в базе 
        :modul: check_account() - Проверка аккаунта на наличие в базе
        :modul: check_reflink() - Проверка ссылки перенаправлении
        :modul: new_reflink() - Создание ссылки перенаправлении
        :modul: del_reflink() - Удалени ссылки перенаправлении
        """

        self.config_path = "tools/config.json"
        self.reflink_path = "tools/reflink"

    # Получение данных из config.json
    def get_config(self):
        """Получение данных из config.json
        :return: accounts.read()"""
        
        with open(self.config_path, "r") as accounts:
            return loads(accounts.read())
        
    # Получение всех аккаунтов
    def get_accounts(self): 
        """Получение всех аккаунтов"""
        config_data = self.get_config()
        return config_data["accounts"]

    # Проверка входящего логина 
    def check_login(self, user_login: str):
        """Проверка входящего логина
        :param: `user_login` Входящий логин
        :return: bool()"""
        
        for login in self.get_accounts():
            login:list = list(login.keys())
            if user_login == login[0]:return True
        return False
    
    # Проверка входящего пароля
    def check_password(self, user_password: str):
        """Проверка входящего пароля
        :param: `user_password` Входящий пароль
        :return: bool()"""

        for password in self.get_accounts():
            password:list = list(password.values())
            if user_password == password[0]: return True

        return False

    # Проверка аккаунта 
    def check_account(self, user_login: str, user_password: str):
        """Проверка данных аккаунта на наличие в базе
        :param: `user_login` Входящий логин
        :param: `user_password` Входящий пароль
        :return: bool()"""

        for login in self.get_accounts():
            account_info = login.get(user_login, False)
            if account_info and account_info == user_password: return True
            
        return False

    # Создание новой перенаправляемой ссылки
    def new_reflink(self):
        """Создание новой перенаправляемой ссылки"""
        with open(self.reflink_path, "a") as new_reflink_append:
            new_reflink = token_hex(16)
            new_reflink_append.write(F"{new_reflink}\n")
            return new_reflink
    
    # Удаление перенаправляемой ссылки
    def del_reflink(self, reflink: str):
        """Удаление перенаправляемой ссылки"""
        with open(self.reflink_path, "r") as file:
            lines = [line for line in file.readlines() if line.strip() != reflink]
            with open(self.reflink_path, 'w') as file:
                file.writelines(lines)


    # Проверка новой перенаправляемой ссылки
    def check_reflink(self, reflink: str):
        """Проверка новой перенаправляемой ссылки в базе"""
        
        with open(self.reflink_path, "r") as new_reflink:
            reflink_list: list = new_reflink.readlines()
            
            # Используем list comprehension для фильтрации ссылок
            if [ref for ref in reflink_list if ref.strip() == reflink]: return True
            return False
