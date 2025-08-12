import cv2

image_path = r"C:\Users\ravya\Downloads\BMW M5 Competition.jpeg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image. Please check the file path.")
else:
  
    original_height, original_width = image.shape[:2]
   
    new_width = 1000
    aspect_ratio = new_width / original_width
    new_height = int(original_height * aspect_ratio)  

    resized_image = cv2.resize(image, (new_width, new_height))
 
    cv2.imshow("Resized Image", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()