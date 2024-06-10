Encrypt an Image:
Call the encrypt_image function with the input image path, output path for the encrypted image, the key, and the method ('additive', 'xor', or 'swap').
Example: encrypt_image('input.jpg', 'encrypted.png', 50, 'swap')

Decrypt an Image:
Call the decrypt_image function with the encrypted image path, output path for the decrypted image, the same key, and the same method used for encryption.
Example: decrypt_image('encrypted.png', 'decrypted.jpg', 50, 'swap')
This implementation provides a basic framework for experimenting with different image encryption techniques. For practical applications, especially those requiring robust security, more sophisticated algorithms should be employed.

There are many methods for image encryption, some of them are as follows:
Additive Method:
This is the initial method we used where each pixel's RGB values are incremented by a key value.

XOR Operation:
This method applies the XOR operation between each pixel's RGB values and the key. The same XOR operation is used for both encryption and decryption.

Pixel Swapping:
This method swaps pixels based on a key. The swap_pixels function shuffles the pixel indices in a deterministic way using the key. For decryption, the same key is used to reverse the swap.
