from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'Home.html')

def ImageProcessing(request):
    myimage = request.FILES['image']
    fs=FileSystemStorage()
    filename=fs.save('test_img.jpeg',myimage)
    uploaded_file_url=fs.url(filename)
    print("File_ URL " + uploaded_file_url)
    uploaded_file_url = uploaded_file_url[1:]
    RecognizeFace(uploaded_file_url)
    return render(request,'Result.html',{'myurl':uploaded_file_url})


def RecognizeFace(file_url):
    import cv2
    images = []
    print("file url" + file_url)
    namelist = ['aamir khan', 'arnold', 'elon musk', 'kit harington', 'mark zukerberg', 'narendra modi',
                'priyanka chopra']
    face_recognizer = cv2.face_LBPHFaceRecognizer.create()
    face_recognizer.read('files/trained1.yml')
    test_img = cv2.imread(file_url,0)

    haar_face_cascade = cv2.CascadeClassifier('files/haarcascade_frontalface_alt.xml')
    faces = haar_face_cascade.detectMultiScale(test_img, scaleFactor=1.1, minNeighbors=5);
    #print("length: " + str(len(faces)))
    for (x, y, w, h) in faces:
        img = test_img[y:y+h, x:x+w]
        images.append(img)

    lable, con = face_recognizer.predict(images[0])
    name = namelist[lable]
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (x, y + h)
    fontScale = 1
    fontColor = (255, 255, 255)
    lineType = 2
    cv2.putText(test_img, name, bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
    cv2.imwrite(file_url,test_img)
    #cv2.imshow("  ", test_img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
