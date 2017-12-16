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


	bmin, gmin, rmin = min(map(min, rgb_image[:,:,0])), min(map(min, rgb_image[:,:,1])), min(map(min, rgb_image[:,:,2]))
	bmax, gmax, rmax = max(map(max, rgb_image[:,:,0])), max(map(max, rgb_image[:,:,1])), max(map(max, rgb_image[:,:,2]))
	print("the range of pixelvalue in blue channel:", (bmin, bmax))
	print("the range of pixelvalue in green channel:", (gmin, gmax))
	print("the range of pixelvalue in red channel:", (rmin, rmax))	

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

	ymin, cbmin, crmin = min(map(min, ycrcb_image[:,:,0])), min(map(min, ycrcb_image[:,:,1])), min(map(min, ycrcb_image[:,:,2]))
	ymax, cbmax, crmax = max(map(max, ycrcb_image[:,:,0])), max(map(max, ycrcb_image[:,:,1])), max(map(max, ycrcb_image[:,:,2]))
	print("the range of pixelvalue in Y channel:", (ymin, ymax))
	print("the range of pixelvalue in Cr channel:", (cbmin, cbmax))
	print("the range of pixelvalue in Cb channel:", (crmin, crmax))	


	hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
	print("HSV value of pixel (20, 25): " + str(hsv_image[20, 25]))
	show_and_save_planes(hsv_image, ("Hue", "Saturation", "Value"))

	hmin, smin, vmin = min(map(min, hsv_image[:,:,0])), min(map(min, hsv_image[:,:,1])), min(map(min, hsv_image[:,:,2]))
	hmax, smax, vmax = max(map(max, hsv_image[:,:,0])), max(map(max, hsv_image[:,:,1])), max(map(max, hsv_image[:,:,2]))
	print("the range of pixelvalue in h channel:", (hmin, hmax))
	print("the range of pixelvalue in s channel:", (smin, smax))
	print("the range of pixelvalue in v channel:", (vmin, vmax))


cv2.waitKey(0)

