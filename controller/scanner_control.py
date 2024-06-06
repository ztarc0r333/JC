'''import cv2
import pyzbar
from pyzbar import pyzbar


def save_barcode(data):
    pass


def read_barcode():
    """
    Reads barcodes from the attached scanner and prints the data
    until 'q' is pressed.
    """
    # Initialize video capture device
    scanner = cv2.VideoCapture(1)

    while scanner.isOpened():
        # Read a frame from the device
        success, frame = scanner.read()

        # Convert the frame to grayscale
        detection = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Find barcodes in the image
        barcodes = pyzbar.decode(detection)

        # Print the data read from each barcode
        for barcode in barcodes:
            data = barcode.data.decode("utf-8")
            if data:
                return print(data)

        # Display the frame with detected barcodes
        cv2.imshow("Barcode Scanner", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):

            break

    # Release the device and close the windows
    scanner.release()
    cv2.destroyAllWindows()'''

import cv2
from pyzbar import pyzbar


def read_barcode():
    """
    Reads barcodes from the attached scanner and prints the data
    until 'q' is pressed.
    """
    # Initialize video capture device
    scanner = cv2.VideoCapture(1)

    # Set camera window size
    scanner.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    scanner.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

    while scanner.isOpened():
        # Read a frame from the device
        success, frame = scanner.read()

        if not success:
            break

        # Convert the frame to grayscale
        detection = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Find barcodes in the image
        barcodes = pyzbar.decode(detection)

        # Display the frame with detected barcodes
        cv2.imshow("Barcode Scanner", frame)

        # Wait for the space bar to capture the scanned code
        key = cv2.waitKey(1) & 0xFF
        if key == ord(" "):  # Space bar key
            for barcode in barcodes:
                data = barcode.data.decode("utf-8")
                if data:
                    print(data)

        # Break the loop on 'q' key press
        elif key == ord("q"):
            break

    # Release the device and close the windows
    scanner.release()
    cv2.destroyAllWindows()
