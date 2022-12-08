import picamera as piC
import createFolder as cF
import time as tm


def main():
	shoot_auto()
	shoot_custom()

def setup(camera):

	camera = piC.PiCamera()
	camera.brightness = 100
	camera.contrast = 100

	return camera


def shoot_auto():
	path = "/home/pi/projectPictures/"
	time = tm.strftime("%Y-%m-%d_%H-%M-%S", tm.localtime())

	cF.mkdir(path)

	camera = piC.PiCamera()
	camera.capture(path + "pic_" + time + ".jpg")

	camera.close()


def shoot_custom():
	path = "/home/pi/projectPictures/"
	cF.mkdir(path)

	pic_name = input("pictrue's name: ")
	pic_type = input("Picture's format: ")


	camera = piC.PiCamera()
	camera.capture(path + pic_name + "." + pic_type)

	camera.close()


def shoot(PATH) -> str:
	time = tm.strftime("%Y-%m-%d_%H-%M-%S", tm.localtime())

	cF.mkdir(PATH)

	pic_name = "pic_" + time + ".jpg"

	camera = setup()

	camera.capture(PATH + pic_name)
	camera.close()

	path = PATH + pic_name
	return path


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
