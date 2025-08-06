# Diffusion Model for Generating Morlet Wavelets

This project was developed by a two-person team as part of the university subject *"Deep Neural Networks in Digital Media"*.  
The goal was to implement a diffusion model capable of generating one-dimensional mathematical signals—specifically, Morlet wavelets—from fully noise-corrupted data.

Due to computational constraints, the project focused on mathematical functions instead of images, without compromising the theoretical alignment with diffusion models.

## Project Objective

The objective was to create a generative model that learns to replicate Morlet wavelets through a process of adding and removing noise. The project focused on:

- building a dataset of synthetic Morlet wavelets,
- propagating noise to and from the data based on the theory of probabilistic diffusion models,
- evaluating the quality of the generated wavelets through visualizations and the loss function.

## Technologies Used

- Python 3.10+
- PyTorch
- PyTorch Lightning
- NumPy
- Matplotlib

## Workflow Structure

1. **Dataset Generation**  
   The dataset is dynamically generated during training — producing various versions of Morlet wavelets.

2. **Diffusion Model**  
   Implementation based on a one-dimensional U-Net. The architecture was simplified compared to classical image-based solutions.

3. **Diffusion Process**  
   - Noise is progressively added using a normal distribution (forward process).  
   - The model learns to remove it by predicting the noise added at each step (reverse process).

4. **Loss Function**  
   The loss minimizes the mean squared error between the predicted and actual noise (following the DDPM approach).

5. **Experiments**  
   Experiments were conducted with different beta schedules and visualizations of reconstruction quality.

## Results

The model successfully learned to generate waves with a structure close to the original Morlet wavelets, even from fully noise-corrupted data. Example results include:

- original wavelets,
- noise-corrupted wavelets,
- wavelets denoised by the model.

<img width="1790" height="590" alt="3" src="https://github.com/user-attachments/assets/538f63c9-ece1-4856-87d5-216c66d08d29" />
<img width="1790" height="590" alt="2" src="https://github.com/user-attachments/assets/f21336d6-a771-46d6-852e-898033da7701" />
<img width="1790" height="590" alt="1" src="https://github.com/user-attachments/assets/4fda56d2-b230-4d43-b023-40e71685ae39" />
<img width="1790" height="590" alt="4" src="https://github.com/user-attachments/assets/a17be655-e7bb-4572-ae76-2d5307081e70" />



