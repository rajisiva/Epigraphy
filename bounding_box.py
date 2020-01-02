import cv2
img = cv2.imread("./Final_set/script4/07.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)
(_,contours, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# contours, _ = cv2.findContours(thresh1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
i = 0
for c in contours:
    rect = cv2.boundingRect(c)
    if rect[2] < 30 or rect[3] < 30: continue
    print(cv2.contourArea(c))
    area = cv2.contourArea(c)
    # if area < 50: continue
    x,y,w,h = rect
    #cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),0)
    crop_img = img[y:y+h, x:x+w]
    cv2.imwrite("cropped_char/"+str(i)+".png",crop_img)
    i = i + 1
    # cv2.putText(img,'Moth Detected',(x+w+10,y+h),0,0.3,(0,255,0))

# cv2.imshow("cropped", crop_img)
cv2.imshow("Show",img)
cv2.waitKey()  
cv2.destroyAllWindows()
cv2.imwrite("bounded_image.png",img)
