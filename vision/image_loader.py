import cv2

def load_image(path):
    img = cv2.imread(path)
    if img is None:
        raise ValueError("Invalid screenshot")
    return cv2.resize(img, (1280, 720))
