import os
from PIL import Image
import cv2
import easyocr

def resize_image(input_path, output_path, size):
    """
    Redimensiona a imagem e salva no caminho especificado.
    
    :param input_path: Caminho da imagem original.
    :param output_path: Caminho para salvar a imagem redimensionada.
    :param size: Novo tamanho (largura, altura) para a imagem.
    """
    img = Image.open(input_path)
    img_resized = img.resize(size, Image.LANCZOS)
    img_resized.save(output_path)

def extract_text_from_image(image_path, language='pt'):
    """
    Extrai texto de uma imagem usando EasyOCR.
    
    :param image_path: Caminho da imagem.
    :param language: Idioma para o OCR (padrão é português).
    :return: Lista de textos extraídos.
    """
    reader = easyocr.Reader([language])
    img = cv2.imread(image_path)
    result = reader.readtext(img, detail=0)
    return result

def main():
    input_image_path = 'C:\\Users\\leomo\\Desktop\\iziocr\\placa.jpeg'
    output_image_path = 'C:\\Users\\leomo\\Desktop\\iziocr\\placa-resized.jpeg'
    new_size = (800, 600)
    
    resize_image(input_image_path, output_image_path, new_size)
    extracted_text = extract_text_from_image(output_image_path)
    
    print(extracted_text)

if __name__ == "__main__":
    main()
