import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Rectangle Demo")

    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.pack(padx=20, pady=20)

    # Draw rectangle: (x1, y1, x2, y2)
    canvas.create_rectangle(50, 50, 250, 150, outline="blue", width=3, fill="lightgray")

    root.mainloop()

if __name__ == "__main__":
    main()