
import cv2
import os
        
def capture_image(file_path):
    # Open the default camera (usually the built-in webcam)
    cap = cv2.VideoCapture(0)
        
    try:
        # Read a single frame from the camera
        ret, frame = cap.read()
    
        # Save the captured frame to the specified file path
        cv2.imwrite(file_path, frame)
    
        print(f"Image captured and saved to {file_path}")
    
    finally:
        # Release the camera resources
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Get the user's home directory
    home_directory = os.path.expanduser("~")

    # Specify the file path on the desktop where you want to save the image
    file_name = "captured_image.jpg"
    desktop_path = os.path.join(home_directory, "Desktop", file_name)

    # Call the capture_image function with the file path on the desktop
    capture_image(desktop_path)



