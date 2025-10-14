# test_camera.py
# maintainted as main
from util.geminiObjectDetect import describe_from_webcam

if __name__ == "__main__":
    print("Starting camera test...\n")
    result = describe_from_webcam()
    print("\n" + "="*50)
    print(result)
    print("="*50)