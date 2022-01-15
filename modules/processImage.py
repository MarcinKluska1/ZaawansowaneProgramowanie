import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import time
import numpy
from modules.getPaths import get_image_paths

IMAGE_INPUT_DIRECTORY: str = "images"
IMAGE_OUTPUT_DIRECTORY: str = "processedImages"
MINIMUM_CONFIDENCE: float = 0.4
MODEL: str = "yolov4"


def process_image(image_path: str) -> tuple[list, list, list, float]:
    image: numpy.ndarray = cv2.imread(image_path)
    start: float = time.time()
    bboxes, labels, confidences = cv.detect_common_objects(
        image,
        confidence=MINIMUM_CONFIDENCE,
        model=MODEL)
    end: float = time.time()
    return bboxes, labels, confidences, end - start


def draw_bbox_for_persons(
        image_path: str,
        directory: str,
        labels: list,
        bboxes: list,
        confidences: list) -> None:
    bbox_person: list = []
    label_person: list = []
    image_name: str = image_path.split("\\")[-1]
    image: numpy.ndarray = cv2.imread(image_path)
    colors: list[:tuple] = []
    for bbox, label, confidence in zip(bboxes, labels, confidences):
        if label == 'person':
            bbox_person.append(bbox)
            label_person.append(label)
            colors.append((0, 0, 255))
    processed_image = draw_bbox(
        image,
        bbox_person,
        label_person,
        confidences,
        write_conf=True,
        colors=colors)
    cv2.imwrite(".\\" + directory + ".\\" + image_name, processed_image)


def print_picture(image_path: str) -> None:
    image: numpy.ndarray = cv2.imread(image_path)
    cv2.imshow(image_path, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_results() -> None:
    for image_path in get_image_paths(IMAGE_INPUT_DIRECTORY):
        bboxes, labels, confidences, duration = process_image(image_path)
        person_counter: int = 0
        print("========= Zdjęcie: {} ========="
              .format(image_path.split("\\")[-1]))
        for label, confidence in zip(labels, confidences):
            if label == "person":
                person_counter += 1
                print(f"Wykryto osobę z "
                      f"prawdopodobieństwem: {round(confidence * 100, 1)}%")
        if person_counter == 0:
            print(f"Nie wykryto żadnych"
                  f" osób na zdjęciu\nCzas przetworzenia zdjęcia:"
                  f" {round(duration, 2)} sekundy\n\n")
        else:
            print(
                f"Wykryto {person_counter} osób na zdjęciu\n"
                f"Czas przetworzenia zdjęcia:"
                f" {round(duration, 2)} sekundy\n\n")
            draw_bbox_for_persons(
                image_path,
                IMAGE_OUTPUT_DIRECTORY,
                labels,
                bboxes,
                confidences)
        print_picture(
            IMAGE_OUTPUT_DIRECTORY + "\\" + image_path.split("\\")[-1])
