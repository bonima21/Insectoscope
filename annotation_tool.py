from tkinter import *
from tkinter import simpledialog
from PIL import Image, ImageTk

class AnnotationTool:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Image Annotation Tool")

        try:
            self.image = Image.open(image_path)
            self.tk_image = ImageTk.PhotoImage(self.image)
        except Exception as e:
            print(f"Error loading image: {e}")
            return

        self.canvas = Canvas(root, width=self.image.width, height=self.image.height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=NW, image=self.tk_image)

        self.labels = []

        self.canvas.bind("<Button-1>", self.annotate)

    def annotate(self, event):
        label_name = simpledialog.askstring("Annotation", "Enter label:")
        if label_name:
            x, y = event.x, event.y
            label = self.canvas.create_text(x, y, text=label_name, fill="red")
            self.labels.append((label_name, (x, y)))

if __name__ == "__main__":
    root = Tk()

    # Replace 'your_image_path.jpg' with the path to your image
    app = AnnotationTool(root, 'C:\\Users\\vanla\\OneDrive\\Desktop\\ladybug.jpeg')

    root.mainloop()
