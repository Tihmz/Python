import cv2

#get the file and read it
path=input("enter image path : ") # ex: /home/user/downloads/
img_name = input("enter image name : ") # ex: filename.jpeg
img = cv2.imread(path+img_name)

#convert to gray scale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#invert the new image (negative)
invert_img= 255 - gray_img

#blur the image and invert it
blur_img= cv2.GaussianBlur(invert_img, (21, 21),0)
invert_blur_img = 255 - blur_img

#creating the sketch
sketch = cv2.divide(gray_img, invert_blur_img, scale = 256.0)

#show the original picture and the new picture
cv2.imshow('old image', img)
cv2.imshow('new image', sketch)

#save the sketch
newName="New"+img_name
sketchDir=path+newName
cv2.imwrite(sketchDir, sketch) #save in the same directoy of the original picture

#wait for a key press to close
cv2.waitKey(0)
