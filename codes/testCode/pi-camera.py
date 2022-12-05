import picamera as piC
import createFolder as cF
import time as tm


def main():
	shoot_auto()
	shoot_custom()


def shoot_auto():
	path = "../../pictures/"
	time = tm.strftime("%Y-%m-%d_%H-%M-%S", tm.localtime())

	cF.mkdir(path)

	camera = piC.PiCamera()
	camera.capture(path + "pic_" + time + ".jpg")

	camera.close()


def shoot_custom():
	path = "../../pictures/"
	cF.mkdir(path)

	pic_name = input("pictrue's name: ")
	pic_type = input("Picture's format: ")


	camera = piC.PiCamera()
	camera.capture(path + pic_name + "." + pic_type)

	camera.close()

if __name__ == "__main__":
	main()
