import sys
import numpy as np
import cv2


def add_salt_pepper_noise(src, pa, pb):
    src_copy = np.copy(src)
    num_pepper_idx = round(src.size * pa)
    pepper_col_idx = np.random.randint(0, src.shape[0], num_pepper_idx)
    pepper_row_idx = np.random.randint(0, src.shape[1], num_pepper_idx)
    src_copy[pepper_col_idx, pepper_row_idx] = 0

    num_salt_idx = round(src.size * pb)
    salt_col_idx = np.random.randint(0, src.shape[0], num_salt_idx)
    salt_row_idx = np.random.randint(0, src.shape[1], num_salt_idx)
    src_copy[salt_col_idx, salt_row_idx] = 255
    return src_copy


def add_gaussian_noise(src, mean, sigma):
    noise = np.random.normal(loc=mean, scale=sigma, size=src.shape)
    return src + noise.astype('uint8')


def test_filters(src, win_suffix=""):
    for kernal_size in ((3, 3), (5, 5), (7, 7)):
        blur_image = cv2.blur(src, (3, 3))
        cv2.imshow(f"Box Filter (Kernal Size = {kernal_size})" + win_suffix,
                   blur_image)

        gaussian_image = cv2.GaussianBlur(src, (3, 3), 1.5)
        cv2.imshow(f"Gaussian Filter (Kernal Size = {kernal_size})" + win_suffix,
                   gaussian_image)

    median_filt_image = cv2.medianBlur(src, 3)
    cv2.imshow("Median Filter" + win_suffix, median_filt_image)


if __name__ == "__main__":
    image = cv2.imread(sys.argv[1], 0)
    cv2.namedWindow("Original Image", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Original Image", image)

    gaussian_image = add_gaussian_noise(image, mean=0, sigma=5)
    cv2.imshow("Gaussian Noise", gaussian_image)
    test_filters(gaussian_image, win_suffix="(Gaussian Noise)")

    for mean in (0, 5, 10, 20):
        gaussian_image = add_gaussian_noise(image, mean=mean, sigma=5)
        cv2.imshow(f"Gaussian Noise (Mean = {mean})", gaussian_image)

    for sigma in (0, 20, 50, 100):
        gaussian_image = add_gaussian_noise(image, mean=0, sigma=sigma)
        cv2.imshow(f"Gaussian Noise (Sigma = {sigma})", gaussian_image)

    salt_pepper_image = add_salt_pepper_noise(image, 0.01, 0.01)
    cv2.imshow("Salt and Pepper Noise", salt_pepper_image)
    test_filters(salt_pepper_image, "(Salt and Pepper Noise)")

    for value in (0.01, 0.03, 0.05, 0.4):
        modified_salt_image = add_salt_pepper_noise(image, value, 0.01)
        modified_pepper_image = add_salt_pepper_noise(image, 0.1, value)
        cv2.imshow(f"Salt and Pepper Noise (Salt = {value})", modified_salt_image)
        cv2.imshow(f"Salt and Pepper Noise (Pepper = {value})", modified_pepper_image)

cv2.waitKey(0)
