import cv2
#for viewing photo
img = cv2.imread("C:\\Users\\Manan\\Downloads\\okay.webp") #loads the image file
if img is None:
    print("error: could open image")
else:
    cv2.imshow("image window",img) #displays the image file
    cv2.waitKey(0) #makes the picture wait until any other key is pressed #key dabane ke 0 seconds baad image band hojaegi
    cv2.destroyAllWindows()

#for capturing video 
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret , frame = cap.read()
    if not ret:
        print("error: unable to read your file")
    else:
        cv2.imshow("webcam feed",frame)
    
    if cv2.waitKey(1):
        break
    cap.release()
    cv2.destroyAllWindows()





