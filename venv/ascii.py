import PIL.Image
import cv2

def ascii_picture():

    webcam = cv2.VideoCapture(0)

    if webcam.isOpened():
        validation, frame = (webcam.read())

        while validation:
            validation, frame = (webcam.read())
            key = cv2.waitKey(2)
            break

        cv2.imwrite("Your picture.png", frame)

        webcam.release()
        cv2.destroyAllWindows()

        ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]

        def resize_image(image, new_width=160):
            width, height = image.size
            ratio = height / width / 1.65
            new_height = int(new_width * ratio)
            resized_image = image.resize((new_width, new_height))

            return (resized_image)

        def grayscaler(image):
            grayscale_image = image.convert("L")

            return (grayscale_image)

        def pixels_to_ascii(image):
            pixels = image.getdata()
            characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])

            return (characters)

        def main(new_width=160):

            try:
                image = PIL.Image.open("Your picture.png")

            except:
                print("Not a valid image")

            new_image_data = pixels_to_ascii(grayscaler(resize_image(image)))

            pixel_count = len(new_image_data)
            ascii_image = "\n".join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))

            print(ascii_image)

            with open("ascii_image.txt", "w") as f:
                f.write(ascii_image)

            return ascii_image

        return main()

    else:
        print("\nsem câmera... não importa\n")