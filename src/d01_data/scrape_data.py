import os
from src.d01_data.GoogleMapDownloader import GoogleMapDownloader


def main():
    start_x = 49.79034782845783
    start_y = 20.297437606648057
    zoom = 20

    gmd = GoogleMapDownloader(start_x, start_y, zoom)
    gmd.generate_multiple_images(tile_images_number=30)


if __name__ == '__main__':
    main()
