import sys
import math
import time

class GPU:
    def __init__(self, filename, width, height):
        self.width = width
        self.height = height
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

    def draw_triangle(self):
        pass

    # def interpreter(self):
    #     mode = str(sys.argv[1])
    #     if (mode == 'r'):
    #         #draw rectangle
    #     else if(mode == 'c'):
    #         #draw circle
    #     else if(mode == 's'):
        
    #     else:
    #     pass

if __name__ == "__main__":
    # time1 = time.time()
    GPU_file = GPU("screen", 640, 480)
    GPU_file.draw_square(240, 240, 50)
    # print(time.time() - time1)
    print("Done")
    input()