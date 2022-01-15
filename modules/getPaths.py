import os


def get_image_paths(directory: str) -> list[:str]:
    file_paths: list[:str] = []
    for file in os.listdir(".\\" + directory):
        if file.endswith((".jpg", ".png", ".bmp")):
            file_paths.append(os.path.join(directory, file))
    return file_paths
