from imageai.Detection import ObjectDetection
import os
import shutil


def main():
    execution_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
    detector.loadModel()
    custom_objects = detector.CustomObjects(person=True)




# в аргумент функции os.walk вписать нужный каталог
    for root, dirs, files in os.walk(r'D:\pythonProjects\opcv\images'):
        for file in files:
            if file.endswith(".jpg"):
                print(file)
                file_image = os.path.join(root, file)
                detections = detector.detectCustomObjectsFromImage(custom_objects=custom_objects,
                                                                   input_image=file_image,
                                                                   output_image_path=os.path.join(execution_path + "\image", file),
                                                                   minimum_percentage_probability=30)

                if detections:
                    print("найден человек на фото" + file)
                    print("--------------------------------")
                else:
                    try:
# в path пишем директорию для сброса картинок, на которых людей не обнаружено
                        path = os.getcwd() + '/new'
                        os.mkdir(path)
                    except OSError:
                        print("Создать директорию %s не удалось" % path)
                    else:
                        print("Успешно создана директория %s " % path)
                    shutil.move(root + '/' + file, path)




main()