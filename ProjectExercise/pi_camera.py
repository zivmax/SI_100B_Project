import picamera as piC
import createFolder as cF
import time


def setup():

	camera = piC.PiCamera()
	camera.video_stabilization = True
	camera.resolution = (2500, 800)
	camera.brightness = 30
	camera.image_effect = 'denoise'
	camera.meter_mode = 'matrix'
	camera.awb_mode = 'flash'
	camera.exposure_compensation = 12
	camera.exposure_mode = 'auto'

	return camera


def shoot(camera, folder_PATH) -> str:
	time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())  # get the local time

	cF.mkdir(folder_PATH)  # detect the folder path, if doesn't exist, it will be created

	pic_name = "pic_" + time + ".png"  # get the name of the picture, the name contains the time when it is taken,
					   # picture format is png

	pic_PATH = folder_PATH + pic_name  # combine the pic-name and folder-path to get the pic-path

	camera.capture(pic_PATH)  # take shoot and save pic in the pic-path
	camera.close()  # clear camera

	return pic_PATH


def shoot_auto():
	path = "/home/pi/projectPictures/"
	time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())

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


def main():
	shoot_auto()

	shoot_custom()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
