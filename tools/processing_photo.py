# -*- coding: utf-8 -*-
# РАЗРАБОТКА ОТ T.ME/FELIX4

from PIL import Image, ImageEnhance, ImageFilter

# Обработка качество фото
class Processing_photo_quality():
    """Обработка качество фото"""

    def __init__(self, file_path: str, enhance: int=1) -> None:
        self.__enhance = enhance
        self.__file_path = file_path

    @property
    def processing_photo(self) -> None:
        """Улучшение качество фото для дольнейшей обработки
        :params self.__enhance: Кофециент контрастности (по умолчании 1.5)
        :params self.__file_path: Путь к фото"""

        # Загрузка изображение
        image = Image.open(fp=self.__file_path)

        # Улучшение контрастности
        enhancer = ImageEnhance.Contrast(image)
        image_contrast = enhancer.enhance(self.__enhance)

        # Улучшение резкости
        sharp_image = image_contrast.filter(ImageFilter.SHARPEN)

        # Сохраните улучшенное изображение
        sharp_image.save(self.__file_path)
