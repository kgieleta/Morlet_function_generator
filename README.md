# Model dyfuzyjny do generowania falek Morleta

Projekt realizowany w dwuosobowym zespole w ramach przedmiotu "Głębokie sieci neuronowe w mediach cyfrowych", którego celem była implementacja modelu dyfuzyjnego generującego jednowymiarowe sygnały matematyczne – konkretnie falki Morleta – na bazie całkowicie zaszumionych danych.

Ze względu na ograniczenia obliczeniowe, projekt koncentrował się na funkcjach matematycznych zamiast na obrazach, co nie umniejsza jego zgodności z teorią diffusion models.

## Cel projektu

Celem było stworzenie modelu generatywnego uczącego się odwzorowywać falki Morleta poprzez proces dodawania i usuwania szumu. W projekcie skupiono się na:

- zbudowaniu datasetu z syntetycznymi falami Morleta,
- propagacji szumu do i od danych w oparciu o teorię dyfuzyjnych modeli probabilistycznych,
- ocenie jakości generowanych fal poprzez wizualizacje i funkcję straty.

## Wykorzystane technologie

- Python 3.10+
- PyTorch
- PyTorch Lightning
- NumPy
- Matplotlib

## Struktura działania

1. **Generacja datasetu**  
   Dataset generowany dynamicznie w trakcie uczenia – tworzy różne warianty falek Morleta.

2. **Model dyfuzyjny**  
   Implementacja oparta na U-Net w wersji jednowymiarowej. Architektura została uproszczona w stosunku do klasycznych rozwiązań obrazowych.

3. **Proces dyfuzji**  
   - Szum dodawany progresywnie na podstawie rozkładu normalnego (forward process).
   - Model uczy się go usuwać, przewidując szum dodany w danym kroku (reverse process).

4. **Funkcja straty**  
   Funkcja minimalizuje błąd średniokwadratowy między przewidywanym a rzeczywistym szumem (zgodnie z podejściem znanym z DDPM).

5. **Eksperymenty**  
   Przeprowadzono eksperymenty z różnymi harmonogramami beta oraz wizualizacjami jakości rekonstrukcji.

## Wyniki

Model nauczył się generować fale o strukturze zbliżonej do oryginalnych falek Morleta nawet z danych całkowicie zaszumionych. Przykładowe wyniki przedstawiają:

- falki oryginalne,
- falki po zaszumieniu,
- falki odszumione przez model
- 
<img width="1790" height="590" alt="3" src="https://github.com/user-attachments/assets/538f63c9-ece1-4856-87d5-216c66d08d29" />
<img width="1790" height="590" alt="2" src="https://github.com/user-attachments/assets/f21336d6-a771-46d6-852e-898033da7701" />
<img width="1790" height="590" alt="1" src="https://github.com/user-attachments/assets/4fda56d2-b230-4d43-b023-40e71685ae39" />
<img width="1790" height="590" alt="4" src="https://github.com/user-attachments/assets/a17be655-e7bb-4572-ae76-2d5307081e70" />
