# IMAGE-EXTRACTION-FROM-TEXT
# LOGIC THAT I HAVE APPLIED :
1.Convert image to grayscale and Gaussian blur image
<br />2.Perform canny edge detection and form a contour
<br />3.Iterate through contours and find bounding boxes
<br />4.Extract ROI, check for their unique pixel values then select top values(which will be the images) and save image
<br />

# Some Description of Code
### First using cv2.GuassianBlur and cv2.Canny we will make image to grayscale and then by canny edge detection and cv2.findContours() we will find the contours.

### Then you have to enter that how many images you can see by your eyes in that document, the application will provide you that many images at end.

### After this I have used two similar looking loops, the first one to find out the top ranking contours in terms of pixel values and the second loop for separating out those top images and then saving it to the Results folder.
