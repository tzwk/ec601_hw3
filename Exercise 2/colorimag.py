import sys
import cv2


def show_and_save_planes(image, labels):
    planes = cv2.split(image)
    for plane, label in zip(planes, labels):
        cv2.imshow(label, plane)
        cv2.imwrite(label + ".png", plane)


if __name__ == "__main__":
	rgb_image = cv2.imread(sys.argv[1], 1)
	cv2.imshow("Original Image", rgb_image)
	print("RGB value of pixel (20, 25): " + str(rgb_image[20, 25]))
	blue, green, red = rgb_image.copy(), rgb_image.copy(), rgb_image.copy()
	blue[:, :, 1:] = 0
	green[:, :, (0, 2)] = 0
	red[:, :, 0:2] = 0
	for plane, label in zip((blue, green, red), ("Blue", "Green", "Red")):
    	cv2.imshow(label, plane)
    	cv2.imwrite(label + ".png", plane)


	ycrcb_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2YCrCb)
	print("YCrCb value of pixel (20, 25): " + str(ycrcb_image[20, 25]))
	show_and_save_planes(ycrcb_image, ("Y", "Cr", "Cb"))

	hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
	print("HSV value of pixel (20, 25): " + str(hsv_image[20, 25]))
	show_and_save_planes(hsv_image, ("Hue", "Saturation", "Value"))

	cv2.waitKey(0)
