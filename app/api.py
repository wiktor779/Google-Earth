from flask import Flask
from flask import request
from flask import send_file
import cv2

app = Flask(__name__)


@app.route('/process_image', methods=['POST'])
def process_image():
    if request.method == 'POST':
        file = request.files.get('image')
        image_name = 'image.png'
        file.save(image_name)

        draw_bounding_boxes(image_name)

        return send_file(image_name, mimetype='image/png')


def draw_bounding_boxes(image_name):
    print('Started processing image')
    #  TODO: process image using yolov3
    print('Finished processing image')


if __name__ == '__main__':
    app.run(debug=True)
