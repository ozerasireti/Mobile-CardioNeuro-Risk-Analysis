import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_ekg(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)

    signal_strength = np.mean(edges)
    signal_variation = np.std(edges)

    print("Dalga Yoğunluk:", round(signal_strength,2))
    print("Dalga Değişkenlik:", round(signal_variation,2))

    if signal_variation < 20:
        print("Sonuç: Düşük Risk - Ritim düzenli görünüyor")
    elif signal_variation < 40:
        print("Sonuç: Orta Risk - Hafif düzensizlik olabilir")
    else:
        print("Sonuç: Yüksek Risk - Belirgin düzensizlik göstergesi")

    plt.imshow(edges, cmap='gray')
    plt.title("EKG Edge Detection")
    plt.axis("off")
    plt.show()
