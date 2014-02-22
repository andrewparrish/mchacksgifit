import cv2

def test():
	vidcap = cv2.VideoCapture('zp.mp4')
	count = 0
	success = True
	while success:
		success, image = vidcap.read()
		cv2.imwrite('frame%d.jpg' % count, image)
		if cv2.waitKey(10) == 27:
			break
		count += 1
