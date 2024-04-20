import cv2
import dlib
import base64
from tools.create_cropping import create

class FaceCropping:
    def __init__(self, image_path: str):
        """Получение лица с фото документа
        :params image_path: Путь к фото
        :func crop_face: Обработка фото
        """

        self.image_path = image_path
        self.detector = dlib.get_frontal_face_detector()

    @property
    def crop_face(self):
        """Обработка фото и выдача BASE64"""


        # Загрузите изображение
        image = cv2.imread(self.image_path)

        # Обнаружение лиц на изображении
        faces = self.detector(image)

        # Если найдено лицо, обрезаем вокруг него
        if len(faces) > 0:
            # Получаем координаты первого найденного лица
            face = faces[0]

            # Определяем границы области вокруг лица с запасом и пропорционально
            x = max(face.left() - int(0.3 * face.width()), 0)
            y = max(face.top() - int(0.4 * face.height()), 0)
            width = min(face.width() + int(0.5 * face.width()), image.shape[1] - x)
            height = min(face.height() + int(0.7 * face.height()), image.shape[0] - y)

            # Вырезаем область вокруг лица
            cropped_face = image[y:y+height, x:x+width]

            # Конвертируем обрезанное изображение в строку base64
            _, img_encoded = cv2.imencode('.png', cropped_face)
            image_base64 = base64.b64encode(img_encoded).decode()

            # Конвертируем обрезанное изображение в строку base64 затем в "face.png"
            create(image_base64)
            return image_base64
        
        else:
            return None

if __name__ == "__main__":
    face_cropper = FaceCropping(image_path='/Users/coder/Desktop/CV-Form/tools/pg.jpeg').crop_face
    file_name = create(base64_string=face_cropper)
    print(file_name)