from scipy import ndimage
import imageio.v2 as imageio
import matplotlib.pyplot as plt

def blur_image(image_path):
    # Load image
    image = imageio.imread(image_path)
    sigma = 5
    # Blur image
    blurred_image = ndimage.gaussian_filter(image, sigma = sigma)
    plt.figure(figsize = (15, 10))
    plt.subplot(121)
    plt.imshow(image, cmap = plt.cm.gray)
    plt.title('Original Image')
    plt.axis('Off')

    plt.subplot(122)
    plt.imshow(blurred_image, cmap = plt.cm.gray)
    plt.title(f'Blurred image (Sigma = {sigma})')
    plt.axis('Off')
    plt.show()

image = 'yourphoto.jpg'
blur_image(image)
