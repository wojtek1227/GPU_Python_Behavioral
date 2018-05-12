
class GPU:
    def __init__(self, filename, width, height):
        self.file = open(filename+'.pbm', "w")
        self.file.write("P1\n")
        self.file.write(str(width)+ " " + str(height)+"\n")
        print("File created")
        pass

    def __del__(self):
        self.file.close()
        print(" File closed")
        pass
    
    def clear_screen(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass

    def draw_triangle(self):
        pass


if __name__ == "__main__":
    GPU_file = GPU("screen", 640, 480)
    print("Done")
    input()