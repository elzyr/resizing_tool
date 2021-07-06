import cv2, glob

division = input("how many times do I have to reduce the photo?: ")

images = glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,-1) #0 dla czarnobialych, 1 dla kolorowych -1 dla kolorowych z alpha

    re=cv2.resize(img,(int(img.shape[1]/int(division)),int(img.shape[0]/int(division))))

    cv2.imshow("checking",re)

    cv2.waitKey(500)

    cv2.imwrite("resized_"+image, re)