import picamera as piC

camera = piC.PicCamera()

camera.capture("/home/pi/Project_pictures/test.jpg")

camera.close()