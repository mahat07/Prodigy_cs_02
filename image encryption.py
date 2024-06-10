from PIL import Image
import numpy as np
import random

def encrypt_image(image_path, output_path, key, method):
    # Open the image
    image = Image.open(image_path)
    # Convert image to numpy array
    image_data = np.array(image)

    if method == 'additive':
        # Apply encryption by adding the key to each pixel's RGB values
        encrypted_data = (image_data + key) % 256
    elif method == 'xor':
        # Apply encryption by XORing the key with each pixel's RGB values
        encrypted_data = image_data ^ key
    elif method == 'swap':
        # Apply encryption by swapping pixels deterministically based on the key
        encrypted_data = swap_pixels(image_data, key)

    # Convert the encrypted data back to an image
    encrypted_image = Image.fromarray(np.uint8(encrypted_data))
    # Save the encrypted image
    encrypted_image.save(output_path)

def decrypt_image(image_path, output_path, key, method):
    # Open the encrypted image
    image = Image.open(image_path)
    # Convert image to numpy array
    image_data = np.array(image)

    if method == 'additive':
        # Apply decryption by subtracting the key from each pixel's RGB values
        decrypted_data = (image_data - key) % 256
    elif method == 'xor':
        # Apply decryption by XORing the key with each pixel's RGB values
        decrypted_data = image_data ^ key
    elif method == 'swap':
        # Apply decryption by swapping pixels back deterministically based on the key
        decrypted_data = swap_pixels(image_data, key, decrypt=True)

    # Convert the decrypted data back to an image
    decrypted_image = Image.fromarray(np.uint8(decrypted_data))
    # Save the decrypted image
    decrypted_image.save(output_path)

def swap_pixels(image_data, key, decrypt=False):
    # Flatten the image data to a 1D array
    flat_data = image_data.flatten()
    length = len(flat_data)
    random.seed(key)

    indices = list(range(length))
    random.shuffle(indices)

    if decrypt:
        # For decryption, we need to reverse the swap
        temp = [0] * length
        for i, index in enumerate(indices):
            temp[index] = flat_data[i]
        flat_data = temp
    else:
        # Apply the swap for encryption
        temp = flat_data.copy()
        for i, index in enumerate(indices):
            flat_data[i] = temp[index]

    # Reshape the flat data back to the original image shape
    return flat_data.reshape(image_data.shape)

# Example usage
if __name__ == "__main__":
    key = 2200  # Encryption/Decryption key (must be the same for both)
    method = 'additive'  # Can be 'additive', 'xor', or 'swap'

    encrypt_image('dog.jpeg', 'encrypted.png', key, method)
    decrypt_image('encrypted.png', 'decrypted.jpg', key, method)
