import cv2
import glob

path = "C:\\Users\\11390\\Desktop\\"
li = glob.glob(path + "\*.jpg")

for i in li:
    image_path_0_original = i
    # image_path_0_original = r"C:\Users\11390\Desktop\444.png"
    image_path_1_gray = image_path_0_original.replace('.', '_1_gray.')
    image_path_2_Inverted = image_path_0_original.replace('.', '_2_Inverted.')
    image_path_3_Sketch = image_path_0_original.replace('.', '_3_Sketch.')


    image = cv2.imread(image_path_0_original)
    # cv2.imshow(image_path_0_original, image)
    # cv2.waitKey(0)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow(image_path_1_gray, gray_image)
    # cv2.waitKey(0)


    inverted_image = 255 - gray_image
    cv2.imshow(image_path_2_Inverted, inverted_image)
    # cv2.waitKey()

    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    cv2.imshow(image_path_3_Sketch, pencil_sketch)
    # cv2.waitKey(0)

    # cv2.imshow(image_path_0_original, image)
    # cv2.imshow(image_path_3_pencil_sketch, pencil_sketch)
cv2.waitKey(0)


    # cv2.imwrite(image_path_1_gray, gray_image)
    # cv2.imwrite(image_path_2_Inverted, inverted_image)
    # cv2.imwrite(image_path_3_Sketch, pencil_sketch)

