import cv2, numpy as np
from zero_hid import Mouse
incriment = {
    "x" : 24,
    "y" : 42
}
border = {
    "x" : 11,
    "y" : 22
}
constant = {
    "x" : 17.063,
    "y" : 30.328
}
# Load image
im = cv2.imread('still_image.png')

# Define the blue colour we want to find - remember OpenCV uses BGR ordering
u = np.array([25,25,25])
l = np.array([0,0,0])
# Get X and Y coordinates of all blue pixels
Y, X = np.where(np.all(u-l-2*abs(im-l/2-u/2)>=[0,0,0],axis=2))
print(len(X),len(Y))
with Mouse(absolute=True) as m:
    # for i in range(1):
    #     m.move(1000,46+int(ky*1081))
    #     m.move(26,76)
    #     m.move(51,1000)
    # m.move(int(17*2),2767)
    for i in range(len(X)):
        m.move(border["x"]+int(constant["x"]*X[i]),border["y"]+int(constant["y"]*Y[i]))