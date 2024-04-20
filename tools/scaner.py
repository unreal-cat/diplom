# -*- coding: utf-8 -*-
# РАЗРАБОТКА ОТ T.ME/FELIX4
# ЧТЕНИЕ И ОБРАБОТКА ДОКУМЕНТА
# SCANER | PERSON

from functools import lru_cache
from datetime import datetime, timedelta
import re
import numpy as np

import easyocr
from passporteye import read_mrz
from PIL import Image


# СКАНИРОВАНИ ДОКУМЕНТА
class Scanner():
    """Чтение документа клиента"""

    def __init__(self, file_path: str, is_passport: bool=False) -> None:
        self._file_path: str = file_path
        self.is_passport: bool = is_passport

    # Чтении файла (ФОТО)
    @property
    @lru_cache()
    def document_result(self) -> list:
        """Сканирование документа и получение списка
        :param self.__file_path: Путь к файлу (str)
        :return __result_reading_file: Результат чтении (list)"""

        # Если получен пасспорт гражданина
        if self.is_passport:
            __passport_information: dict = read_mrz(self._file_path)
            return __passport_information.to_dict()

        # Если получен пасспорт моряка
        __file_reader = easyocr.Reader(['en'])
        __file = np.array(Image.open(self._file_path))
        __result_reading_file: list = __file_reader.readtext(__file, detail=0)

        return __result_reading_file

# ПОЛУЧЕНИЕ ДАННЫХ КЛИЕНТА        
class Person():
    """Обработка данных"""

    def __init__(self, information: list[str] | dict, is_passport: bool=False) -> None:
        """Обработка данных
        :params information: list[str]: ИНФОРМАЦИЯ ИЗ ДОКУМЕНТА LIST
        :return name: ИМЯ;
        :return surname: ФАМИЛИЯ;
        :return fathers_name: ИМЯ ОТЦА;
        :return date: ДАТА;
        :return height: РОСТ;
        :return address: АДРЕС;
        :return dqk_code: DQK КОД;
        :return eyes_color: ЦВЕТ ГЛАЗ;
        :return hair_color: ЦВЕТ ВОЛОС;
        :return passport_id: НОМЕР ПАСПОРТА;
        :return document_type: ТИП ДОКУМЕНТА;
        :return passport_country: МЕСТО РОЖДЕНИИ;
        :return passport_expiration_date: СРОК ОКОНЧАНИИ ДЕЙСТВИИ ПАСПОРТА;
        :return passport_date_issue: ДАТА ВЫДАЧИ ПАСПОРТ;"""

        self.passport: list | dict = information
        self.is_passport: bool = is_passport
        self.processed_information: list = [processed_information for processed_information in information if processed_information.isupper()]

    @property
    def height(self) -> str:
        """`Получает HEIGHT | РОСТ по пасспортным данным` self.passport"""
        result: str = [height for height in self.passport if "cm" in height].pop().upper()
        return result
    
    @property
    def dqk_code(self) -> str:
        """`Получает DQK | КОД по обработанным пасспортным данным` self.processed_information"""
        result: str = " ".join(self.processed_information[-1].split())
        return result

    @property
    def surname(self) -> str:
        """`Получает SURNAME | ФАМИЛИЯ по обработанным пасспортным данным` self.processed_information"""
        result: str = self.processed_information[0]
        return result

    @property
    def fathers_name(self) -> str:
        """`Получает FATHER NAME | ИМЯ ОТЦА по обработанным пасспортным данным` self.processed_information"""
        fathers_name: str = str(self.processed_information[1]) 
        try:
            if "_" in fathers_name: result = fathers_name.split("_")[0]
            elif "." in fathers_name: result = fathers_name.split(".")[0]
            elif "," in fathers_name: result = fathers_name.split(",")[0]
            elif " " in fathers_name: result = fathers_name.split(" ")[0]
            return result
        
        except: result: str = str(self.processed_information[1])
        return result

    @property
    def name(self) -> str:
        """`Получает NAME | ИМЯ по обработанным пасспортным данным` self.processed_information"""
        name: str = str(self.processed_information[1]) 
        try:
            if "_" in name: result = name.split("_")[1]
            elif "." in name: result = name.split(".")[1]
            elif "," in name: result = name.split(",")[1]
            elif " " in name: result = name.split(" ")[1]
            return result
        
        except: result: str = str(self.processed_information[1])
        return result

    @property
    def address(self) -> str:
        """`Получает PERMANENT ADDRESS | АДРЕСС НАХОЖДЕНИИ по обработанным пасспортным данным` self.processed_information"""
        result: str = self.processed_information[3]
        return result

    @property
    def date(self) -> str:
        """`Получает DATE | ДАТА РОЖДЕНИИ по обработанным пасспортным данным` self.processed_information"""
        if self.is_passport:
            date_of_birth: str = self.passport.get("date_of_birth")
            result = datetime.strptime(date_of_birth, '%y%m%d').strftime('%d.%m.%Y')
            return result


        date_match = re.search(r'\d{2}.\d{2}.\d{4}', str(self.passport))
        if date_match: return date_match.group(0)
        else:
            # Исправление даты, замена букв на чисел
            corrected_date: list = [date.replace("L", "1").replace("A", "4")\
                .replace("Z", "7").replace("O", "0")\
                .replace("I", "1").replace("S", "5")\
                .replace("B", "5") for date in self.processed_information[4]]

            # Исправление даты, перенос из LIST в STR
            result: str = F"{''.join(corrected_date[0:2])}.{''.join(corrected_date[2:4])}.{''.join(corrected_date[4:8])}"    

        return result

    @property
    def eyes_color(self) -> str:
        """`Получает EYES COLOR | ЦВЕТ ГЛАЗ по обработанным пасспортным данным` self.processed_information"""
        result: str = self.processed_information[5]
        return result

    @property
    def hair_color(self) -> str:
        """Выдает HAIR COLOR | BLACK"""
        return "BLACK"

    @property
    def passport_id(self) -> str:
        """`Получает PASSPORT ID | НОМЕР ПАСПОРТА по обработанным пасспортным данным` self.processed_information"""
        result: str = self.passport.get("number", "")
        return result

    @property
    def document_type(self) -> str:
        """Выдает DOCUMENT TYPE | PASSPORT"""
        return "PASSPORT"

    @property
    def passport_country(self) -> str:
        """`Получает COUNTRY | СТРАНА ВЫДАЧИ по обработанным пасспортным данным` self.processed_information"""
        result: str = self.passport.get("country", "")
        
        if result == "AZE": return "AZERBAIJAN"
        return result

    @property
    def passport_expiration_date(self) -> str:
        """`Получает EXPIRATION DATE | ОКОНЧАНИЕ СРОКА ДЕЙСТВИИ ПАСПОРТА по обработанным пасспортным данным` self.processed_information"""
        try:
            expiration_date: str = self.passport.get("expiration_date") 
            result = datetime.strptime(expiration_date, '%y%m%d').strftime('%d.%m.%Y')
            return result
        
        except AttributeError: return "НЕ ОБРАБОТАН"
    
    @property
    def passport_date_issue(self) -> str:
        """`Получает DATE ISSUE | ДАТА ВЫДАЧИ ПАСПОРТА по обработанным пасспортным данным` self.processed_information"""
        try:
            expiration_date: str = self.passport.get("expiration_date") 
            formated_expiration_date = datetime.strptime(expiration_date, '%y%m%d')
            result = (formated_expiration_date - timedelta(days=365*10 + 1)).strftime('%d.%m.%Y')
            return result
            
        except AttributeError: return "НЕ ОБРАБОТАН"

# ПОЛУЧЕНИЕ ДАННЫХ VESIQE
class Vesiqe():
    """Обработка данных"""

    def __init__(self, information: list[str], switch: bool) -> None:
        """Обработка данных
        :params information: list[str]: ИНФОРМАЦИЯ ИЗ ДОКУМЕНТА LIST
        :params switch: bool: ЕСЛИ TRUE ТО НОВЫЙ ДОКУМЕНЕНТ ИНАЧЕ СТАРЫЙ
        :return name: ИМЯ;
        :return surname: ФАМИЛИЯ;
        :return fathers_name: ИМЯ ОТЦА;
        :return date: ДАТА;
        :return height: РОСТ;
        :return address: АДРЕС;
        :return eyes_color: ЦВЕТ ГЛАЗ;
        :return hair_color: ЦВЕТ ВОЛОС;
        :return passport_id: НОМЕР ПАСПОРТА;
        :return document_type: ТИП ДОКУМЕНТА;
        :return passport_country: МЕСТО РОЖДЕНИИ;
        :return passport_expiration_date: СРОК ОКОНЧАНИИ ДЕЙСТВИИ ПАСПОРТА;
        :return passport_date_issue: ДАТА ВЫДАЧИ ПАСПОРТ;"""

        self.switch: bool = switch
        self.passport: list | dict = information
        self.processed_information: list = [processed_information for processed_information in information if processed_information.isupper()]
        print(self.passport)
    
    @property
    def dat(self) -> list:
        return self.processed_information

    @property
    def number(self) -> str:
        """`Получение номера документа VESIQE | По обработанным данным` self.processed_information"""
        print(self.processed_information)
        if self.switch: number_index = self.processed_information #.index("AZE")
        else: 
            # Ищем соответствие в каждой строке списка
            # Используем регулярное выражение для поиска строки, начинающейся с 'AZE' и содержащей цифры
            result = [match.group() for item in self.processed_information for match in [re.compile(r'AZE\d+').search(item)] if match]

        if self.switch: result: str = self.processed_information[-2] #re.sub(r'([A-Z]{3})(\d+)', r'\1 \2', self.processed_information[number_index + 1])
        # else: 
            # result: str = re.sub(r'([A-Z]{3})(\d+)', r'\1 \2', self.processed_information[number_index + 1])
            # if not "AZE" in result: result: str = re.sub(r'([A-Z]{3})(\d+)', r'\1 \2', self.processed_information[number_index + 2])
        
        # print(number_index)
        print(self.passport)
        print(result)

        # Если данные от индекса на шаг в переди то он пропустит первывй шаг и возьмет второй
        return result

    @property
    def date(self) -> list:
        """`Получение дату получении и срок действия документа VESIQE | По не обработанным данным` self.passport
        
        :return List(): ['01/08/23', '01/08/28'] or ['01.08.2023', '01.08.2028']\n
        :description: [0] - Дата получении (С) [1] - Срок действия (До).
        """
        
        # Используем регулярное выражение для поиска значений, соответствующих датам (формата 'dd/mm/yy')
        data: list = self.passport
        
        # Получаем последние два значения из найденных
        if self.switch: 
            # Используем регулярное выражение для поиска дат в формате "dd.mm.yyyy"
            # Ищем все соответствия в каждой строке списка
            date_pattern = re.compile(r'\b\d{2}\.\d{2}\.\d{4}\b')
            result: list = [match.group() for item in data for match in [date_pattern.search(item)] if match]
        
        else: 
            date_pattern = re.compile(r'\b\d{2}\/\d{2}\/\d{2}\b')
            result: list = [match.group() for item in data for match in [date_pattern.search(item)] if match]

            # result: str =  re.findall(r'\d{2}/\d{2}/\d{2}', " ".join(data))[-2:]
        
        print(f"{data=}")
        print(f"{result=}")
        return result

    @property
    def country(self) -> str:
        # Используем регулярное выражение для поиска значений, соответствующих 'AZERBAIJAN; BAKU' или подобным шаблонам
        data: list = self.passport
        pattern = r'[A-Z]+; [A-Z]+'

        # Находим все соответствующие значения в списке и берем последнее
        matches = re.findall(pattern, ' '.join(data))
        last_match = matches[-1] if matches else None

        return last_match or "AZORBAYCAN"

if __name__ == "__main__":
    print(Vesiqe(Scanner(file_path="/Users/coder/Desktop/CV-Form/tools/vesiqe2.png", is_passport=False).document_result).country)
    

    

    



