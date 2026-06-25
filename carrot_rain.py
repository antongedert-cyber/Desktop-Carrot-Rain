import random
import tkinter as tk


class CarrotRain:
    def __init__(self, root):
        self.root = root
        self.root.title("Carrot Rain")
        self.root.configure(bg="black")
        self.root.attributes("-topmost", True)
        self.root.attributes("-fullscreen", True)
        self.root.overrideredirect(True)
        self.root.config(cursor="none")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        try:
            self.root.wm_attributes("-transparentcolor", "black")
        except tk.TclError:
            pass

        self.canvas = tk.Canvas(
            root,
            width=self.width,
            height=self.height,
            bg="black",
            highlightthickness=0,
            bd=0,
        )
        self.canvas.pack()

        self.carrots = [self._spawn_carrot() for _ in range(90)]

        self.root.bind("<Escape>", lambda event: self.root.destroy())
        self.root.bind("<F11>", lambda event: self.root.attributes("-fullscreen", not self.root.attributes("-fullscreen")))
        self.animate()

    def _spawn_carrot(self):
        return {
            "x": random.randint(0, self.width),
            "y": random.randint(-220, -20),
            "speed": random.uniform(2.4, 5.8),
            "drift": random.uniform(-0.8, 0.8),
            "size": random.randint(18, 30),
            "rotation": random.uniform(-0.18, 0.18),
        }

    def animate(self):
        self.canvas.delete("all")

        for carrot in self.carrots:
            carrot["y"] += carrot["speed"]
            carrot["x"] += carrot["drift"]

            if carrot["y"] > self.height + 40:
                carrot.update(self._spawn_carrot())
                carrot["y"] = random.randint(-80, -20)

            if carrot["x"] < -40:
                carrot["x"] = self.width + 20
            elif carrot["x"] > self.width + 40:
                carrot["x"] = -20

            self.canvas.create_text(
                carrot["x"],
                carrot["y"],
                text="🥕",
                font=("Segoe UI Emoji", carrot["size"]),
                fill="#ff7f0f",
                anchor="center",
            )

        self.root.after(16, self.animate)


def main():
    root = tk.Tk()
    CarrotRain(root)
    root.mainloop()


if __name__ == "__main__":
    main()
