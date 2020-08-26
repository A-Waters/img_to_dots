#higher scale = larger files/images and better quality
img_scale = 4

fileName = 'test2.JPG'

gen_type = 'single'

from PIL import Image, ImageDraw

# get pixel data
im = Image.open(fileName, 'r')
width, height = im.size
pixel_values = list(im.getdata())

# create new image to draw on
blank = Image.new('P', (width*img_scale, height*img_scale), 255)
draw = ImageDraw.Draw(blank)

# draw a circle
def create_circle(x, y, r): #center coordinates, radius
    draw.ellipse((x-r, y-r, x+r, y+r), fill=(0,0,0,255))

# types of generation
types = ['single','quad']

# generate the image
def generate():
    if gen_type not in types:
        raise Exception("Please chose a valid type") 
        print (types)


    print ("start")
    perc = 0


    if gen_type == 'single':
        # for every pixel get the index and rgb value
        for index, values in enumerate(pixel_values):
            # skip every other line
            if (index%width) % 2 == 0 or int(index/width) % 2 == 0:
                continue

            # calculacte gray value (inverted)
            gray_value = (values[0] * 0.3) + (values[1] * 0.59) + (0.11 * values[2]) + 1# (max(values) + min(values)) / 2 #
            
            # get x and y pos
            y, x = (index/width), (index%width)


            
            # draw circle at correct positions and add invert gray scale (to non inverted)
            # print(gray_value)
            create_circle(x * img_scale, y * img_scale, (1 - float((gray_value)/255))*img_scale)

            #loading ani
            if (int(index/len(pixel_values) * 100) > perc):
                perc = (int(index/len(pixel_values) * 100))
                print(str(perc) + "%")





    elif gen_type == 'quad':
        # for every pixel get the index and rgb value
        for index, values in enumerate(pixel_values):
            # skip every other line
            '''if (index%width) % 2 == 0 or int(index/width) % 2 == 0:
                    continue
            '''
            # calculacte gray value (inverted)
            gray_value = (values[0] * 0.3) + (values[1] * 0.59) + (0.11 * values[2]) + 1# (max(values) + min(values)) / 2 #
            
            # get x and y pos
        
            y, x = (index/width) * img_scale, (index%width) * img_scale

            # draw circle at correct positions and add invert gray scale (to non inverted)
            # print(gray_value)
            
            for i in range(img_scale):
                for j in range(img_scale):
                    create_circle(
                                x + i, 
                                y + j, 
                                (1 - float((gray_value)/255))*img_scale/2)

            #loading ani
            if (int(index/len(pixel_values) * 100) > perc):
                perc = (int(index/len(pixel_values) * 100))
                print(str(perc) + "%")

            

    # show the img
    blank.show()

    #save the img
    blank.save(str(fileName.split('.')[-2]) + '.' + str(gen_type) + '.' + str(img_scale) + '.output.png')





if __name__ == '__main__':
    generate()

'''
    values = pixel_values[int(len(pixel_values)/2)]

    gray_value = (values[0] * 0.3) + (values[1] * 0.59) + (0.11 * values[2]) + 1
    

    y, x = (height/2), (width/2)

    create_circle(x, y, (1 - float((gray_value)/255)))

    print(gray_value)
    print(1 - float((gray_value)/255))



    blank.show()
    '''
