from PIL import Image as Img
from django.core.files import File
from skimage.measure import compare_ssim as ssim
import StringIO
import cv2
import numpy as np
import os


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def compare_images(image_one_path, image_two_path):
    search_image = cv2.imread(image_one_path)
    image_from_db = cv2.imread(image_two_path)
    search_image = cv2.cvtColor(search_image, cv2.COLOR_BGR2HSV)
    image_from_db = cv2.cvtColor(image_from_db, cv2.COLOR_BGR2HSV)
    m = mse(search_image, image_from_db)
    s = ssim(search_image, image_from_db, multichannel=True)

    return m, s


def handle_image_upload(request, image_file):
    user_dir = 'temp_images/' + str(request.user.id)
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
    with open(user_dir + '/temp.jpg', 'wb+') as destination:
        image = Img.open(StringIO.StringIO(image_file.read()))
        image.thumbnail((500, 500), Img.ANTIALIAS)
        output = StringIO.StringIO()
        image.save(output, format='JPEG', quality=75)
        output.seek(0)
        image = File(output, image_file.name)
        for chunk in image.chunks():
            destination.write(chunk)
