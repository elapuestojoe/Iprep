'''
Last night you partied a little too hard. 
Now there's a black and white photo of you that's about to go viral! 
You can't let this ruin your reputation, 
so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: 
Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, 
including x itself. All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.
'''
def boxBlur(image):
    newWidth = len(image[0]) - 2
    newHeight = len(image) - 2
    
    result = []
    for i in range(newHeight):
        result.append([0]*newWidth)
        
    for x in range(newWidth):
        for y in range(newHeight):
            val = 0
            for i in range(3):
                for j in range(3):
                    val += image[y+i][x+j]
            
            val = val // 9
            result[y][x] = val
    return result