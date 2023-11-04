from cvzone.ClassificationModule import Classifier
import cv2
import webbrowser
cap = cv2.VideoCapture(0)
classifier = Classifier('Model/keras_model.h5', 'Model/labels.txt')
while True:
    _, img = cap.read()
    prediction = classifier.getPrediction(img)
    print(prediction)
    classID = prediction[1]
    if classID == 0:
        #webbrowser.open('https://www.youtube.com/watch?v=FXDkK-eZeuk&ab_channel=NinjaNerd')
        print("Plastid")
        f = open("r.txt", "w")
        f.write("Plastid")
        f.close()
    elif classID == 1:
        #webbrowser.open('https://www.youtube.com/watch?v=rIo5irsTWJs&ab_channel=TopprClass8-10')
        print("Mitochondria")
        f = open("r.txt", "w")
        f.write("Mitochondria")
        f.close()
    elif classID == 2:
        cv2.imshow("Image", img)

    cv2.waitKey(1)
