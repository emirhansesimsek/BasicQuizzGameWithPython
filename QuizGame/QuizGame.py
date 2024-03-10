# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:49:44 2024

@author: Lenovo
"""

print("Quiz Oyununa Hoşgeldin")
print("Her Doğru cevap +1 skor olarak, Her yanlış cevap -1 skor olarak hanemize yazılacaktır")
score = 0
playing = input("Oyuna başlamak ister misin? ")

if playing.lower() != "evet":
    quit()

print("Tamam Başlayalım :)")

answer = input("Yakın Tarihte Uzaya Çıkan Türkün ismi nedir? ")
if answer.lower() == "alper":
    print("Doğru Cevap")
    score += 1
else:
    print("Cevap Yanlış")
    score -= 1
answer = input("Türkiyenin başkenti neresidir. ? ")
if answer.lower() == "ankara":
    print("Doğru Cevap")
    score += 1
else:
    print("Cevap Yanlış")
    score -= 1

print("Skorunuz:" + str(score) + " dir")
if score < 0: 
    print("Doğruluk Oranımız: 0%")
else:
  print("Doğruluk Oranımız: " + str((score/4)*100) + "% dir")