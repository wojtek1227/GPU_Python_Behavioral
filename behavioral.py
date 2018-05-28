import sys
import math
import time
import datetime

class GPU:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        filename = self.set_filename()
        self.file = open(filename+'.pbm', "w")
        self.file.write("P1\n")
        self.file.write(str(width)+ " " + str(height)+"\n")
        print("File created")
        # self.clear_screen()
        pass

    def __del__(self):
        self.file.close()
        print(" File closed")
        pass
    
    def set_filename(self):
        if sys.argv[1]:
            try:
                return sys.argv[1] + "_" + sys.argv[2] + "_" + sys.argv[3] + "_" + sys.argv[4] + "_" + sys.argv[5]
            except IndexError:
                return sys.argv[1] + "_" + sys.argv[2] + "_" + sys.argv[3] + "_" + sys.argv[4]

        else:
            return datetime.date.today.strftime('%H:%M:%S_%d_%b_%y')

    def clear_screen(self):
        for x in range(self.height):
            for y in range(self.width):
                self.file.write("0")
            self.file.write("\n")
        pass

    def count_distance(self, x1, y1, x2, y2):
        return math.sqrt(pow(abs(x1-x2),2) + pow(abs(y1-y2), 2))

    def draw_rectangle(self, x1, y1, x2, y2):
        for x in range(self.height):
            for y in range(self.width):
                if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                    self.file.write("1")
                else:    
                    self.file.write("0")
            self.file.write("\n")
        pass

    def draw_square(self, x1, y1, width):
        for x in range(self.height):
            for y in range(self.width):
                if x >= x1 and x <= x1 + width and y >= y1 and y <= y1 + width:
                    self.file.write("1")
                else:    
                    self.file.write("0")
            self.file.write("\n")
        pass

    def draw_circle(self, x_centre, y_centre, radius):
        for x in range(self.height):
            for y in range(self.width):
                if x >= x_centre - radius + 1 and x <= x_centre + radius - 1 and y >= y_centre - radius + 1 and y <= y_centre + radius - 1:
                    if(abs(x - x_centre) + abs(y - y_centre) < radius):
                        self.file.write("1")
                    else:
                        distance = self.count_distance(x_centre, y_centre, x, y)
                    
                        if(math.ceil(distance) < radius):
                            self.file.write("1")
                        else: 
                            self.file.write("0")
                else:    
                    self.file.write("0")
            self.file.write("\n")
        pass

    def draw_triangle(self, x1, y1, width):
        for x in range(self.height):
            for y in range(self.width):
                if x >= x1 and x <= x1 + width and y >= y1 and y <= y1 + width:
                    if (x - x1) >= (y - y1): 
                        self.file.write("1")
                    else: 
                        self.file.write("0")
                else:    
                    self.file.write("0")
            self.file.write("\n")
        pass

    def interpreter(self):
        mode = str(sys.argv[1])
        if mode == '-r':
            # example: python behavioral.py r [x1] [y1] [x2] [y2]
            self.draw_rectangle(int(sys.argv[2]), int(sys.argv[3]),int(sys.argv[4]), int(sys.argv[5]))
        elif mode == '-c':
            # example: python behavioral.py r [x_centre] [y_centre] [radius]
            self.draw_circle(int(sys.argv[2]), int(sys.argv[3]),int(sys.argv[4]))
            #draw circle
        elif mode == '-s':
            # example: python behavioral.py s [x1] [y1] [width]
            self.draw_square(int(sys.argv[2]), int(sys.argv[3]),int(sys.argv[4]))
        elif mode == '-t':
            # example: python behavioral.py t [x1] [y1] [width]
            self.draw_triangle(int(sys.argv[2]), int(sys.argv[3]),int(sys.argv[4]))
        else:
            self.clear_screen()
        pass

if __name__ == "__main__":
    # time1 = time.time() 
    GPU_file = GPU(640, 480)
    GPU_file.interpreter()
    #GPU_file.draw_triangle(240, 240, 50)
    # print(time.time() - time1)
    print("Done")
    #input()