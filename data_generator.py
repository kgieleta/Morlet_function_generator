import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import random
from PIL import Image

def morlet_wavelet(t, w0, phi=0):
    return np.pi**(-1/4) * np.exp(1j * (w0 * t + phi)) * np.exp(-t**2 / 2)

def generate_morlet_images(num_samples, img_size=28, output_dir='morlet_dataset'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    t = np.linspace(-5, 5, img_size)
    for i in range(num_samples):
        fig, ax = plt.subplots(figsize=(2, 2), dpi=img_size//2)
        w0 = np.random.uniform(5, 15)
        phi = np.random.uniform(0, 2 * np.pi)
        f = morlet_wavelet(t, w0, phi)
        noise = np.random.normal(0, 0.1, size=f.shape)
        
        # Draw anly real part of the function
        ax.plot(t, f.real + noise, color='blue', alpha=0.7)
        ax.axis('off')
        plt.tight_layout(pad=0)
        
        img_path = os.path.join(output_dir, f'morlet_{i}.png')
        fig.savefig(img_path, format='png', bbox_inches='tight', pad_inches=0)
        plt.close(fig)

        # Conversion to size 28x28 and save in RGB color space
        img = Image.open(img_path).convert('RGB')
        img = img.resize((img_size, img_size), Image.ANTIALIAS)
        img.save(img_path)

def create_dataset(input_dir='morlet_dataset', output_dir='mnist_like_morlet', train_ratio=0.8):
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    train_dir = os.path.join(output_dir, 'train')
    test_dir = os.path.join(output_dir, 'test')
    os.makedirs(train_dir)
    os.makedirs(test_dir)
    
    # Split data into train and test datasets
    image_files = [f for f in os.listdir(input_dir) if f.endswith('.png')]
    random.shuffle(image_files)
    train_size = int(len(image_files) * train_ratio)
    
    train_files = image_files[:train_size]
    test_files = image_files[train_size:]
    
    for f in train_files:
        shutil.copy(os.path.join(input_dir, f), os.path.join(train_dir, f))
    
    for f in test_files:
        shutil.copy(os.path.join(input_dir, f), os.path.join(test_dir, f))

if __name__ == '__main__':
    # Generate Morlet function and save to file

    # Number of samples to generate
    num_samples = 1000
    generate_morlet_images(num_samples)
    
    create_dataset()
