import pytesseract as tess
import openai
from PIL import Image
import cv2
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

my_image = cv2.imread('IRBYK.jpg')
txt = tess.image_to_string(my_image)

# txt.dtype
# Display Original Image
cv2.imshow('Image', my_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Save in a txt file
# my_file = open('file1.txt', 'w')
# my_file.write(txt + '\n')
# my_file.close()

openai.api_key = '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'


while True:
    question = input("crea 10 pregunta: ")
    value = txt
    prompt=question+" "+value
    if prompt=="exit":
        break

    completion= openai.Completion.create(engine="text-davinci-003",
                            prompt=prompt,
                          
                            n=1,
                            max_tokens=2048)
    print(completion.choices[0].text)