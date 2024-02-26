Difference Between Images
This Python script captures images from a camera at two different time points and computes the difference between them. It detects motion by comparing consecutive frames and highlights the areas where motion occurs.

Description
The script captures images from a camera feed at two different time intervals and calculates the difference between them. It then identifies areas of motion by detecting changes between the two frames and draws rectangles around these areas.

Dependencies
Python 3.x
OpenCV (cv2) library
Installation
Ensure you have Python 3.x installed on your system.
Install the OpenCV library:
Copy code
pip install opencv-python
Usage
Connect a camera to your system.
Run the script:
Copy code
python difference_between.py
The script will open two windows:
"Hareket Penceresi 1": Displays the first captured image.
"Hareket Penceresi 2": Displays the second captured image.
"Fark Penceresi 2": Displays the difference between the two images, highlighting areas of motion with rectangles.
Important Notes
Press the "ESC" key to exit the program.
Ensure that your camera is properly connected and accessible by the script.
Adjust the sleep time between capturing images (time.sleep(2)) as needed.
Fine-tune the motion detection parameters (cv2.threshold, cv2.GaussianBlur, cv2.dilate, etc.) based on your specific requirements.
License
This project is licensed under the MIT License.

Contribution
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

#Türkçe
OpenCv ile yapılan bu uygulamada kameradan aldığımız görüntüler arasında farklılıkları gösteriyoruz.