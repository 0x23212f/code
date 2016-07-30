import sys, cv2, random, os

# get command-line arguments
imagePath = sys.argv[1]
cascadePath = sys.argv[2]

# create haar cascade
faceCascade = cv2.CascadeClassifier(cascadePath)

# read the image
image = cv2.imread(imagePath)

# convert image to grayscale. lot of opencv operations are done in grayscale.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# this is where the faces are being detected
# detectMultiScale detects objects. we're calling it on the faces cascade
# parameters:
# gray -> the grayscale of the input image object
# scaleFactor=1.1 -> compensates for different sized faces
# minNeighbors=5 -> how many objects are detected near current to declare face found
# minSize=(30,30) -> gives size of each window

faces = faceCascade.detectMultiScale(
	gray,
	scaleFactor=1.1,
	minNeighbors=5,
	minSize=(30,30),
	flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

# print faces -- you can try uncommenting this to see what faces is

print "Found %s faces!" % format(len(faces))

# draw rectangle around detected faces
for (x, y, w, h) in faces:
	cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)

# get extension and filename
def getExt(filename):
	file_ext = os.path.splitext(filename)
	return file_ext

output_file_name_split = getExt(imagePath)
output_file_name = output_file_name_split[0] + "_faces" + output_file_name_split[1]

# export photo to outputs directory
cv2.imwrite(output_file_name, image)

# wait for user to press key
cv2.imshow('Faces', image)
cv2.waitKey(0)