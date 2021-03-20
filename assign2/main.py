import cv2

image = cv2.imread('/Users/gusdn0828/desktop/images.jpeg')

pt = (-1, -1)

title = 'assignment2 someobject'
cv2.rectangle(image, (80, 40), (170, 130), (0, 0, 255), 2)
cv2.putText(image, "cat", (80, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), thickness=2)


def onMouse(event, x, y, flags, param):
    pass


cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
