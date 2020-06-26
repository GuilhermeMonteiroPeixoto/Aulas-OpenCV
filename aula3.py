# AULA 3 Detector de Blobs

#Importando Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import cv2

#Importando a imagem
imagem = cv2.imread('imagem_virus2.png')
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

#blob detection only works with white background
detector = cv2.SimpleBlobDetector_create()
saida = detector.detect(imagem)

number_of_blobs = len(saida)
text = "Number of Blobs: " + str(len(saida))
print(text)
