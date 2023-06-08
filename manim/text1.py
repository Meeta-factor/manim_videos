from manimlib import *
from os import system



class demo(Scene):
    def construct(self):
        tex = Title(
            r"this is first title",
            r"this is second title ",
            r"this is third title",
            arg_separator=r"\\"
        )
        self.add(tex)


class geometry(Scene):
    def construct(self):
        temp_p = None
        radius = 3
        colors = [RED, BLUE, GREEN, PINK]
        for i, num in enumerate([4, 5, 6, 10, 20, 50]):
            if temp_p is None:
                temp_p = self.get_circle_polygon(radius, num)
                temp_p.set_fill(color=colors[i % len(colors)], opacity=0.75)
                self.play(Write(temp_p))
            else:
                cur_p = self.get_circle_polygon(radius, num)
                cur_p.set_fill(color=colors[i % len(colors)], opacity=0.75)
                self.play(ReplacementTransform(temp_p, cur_p))
                temp_p = cur_p
    
    def get_circle_polygon(self, radius, n : int):
        return Polygon(
            *[np.array([np.cos(i * 2 * PI / n), np.sin(i * 2 * PI / n), 0]) * radius for i in range(n)]
        )
class text(Scene):
    def construct(self):
        word = Text(
            text="I am a Text object",
            color=BLUE_B
        )
        self.add(word)


class InteractiveDemo(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(YELLOW, opacity=0.5)
        circle.set_stroke(BLUE)
        square = Square()
        square.set_fill(BLUE, opacity=0.7)
        square.set_stroke(RED)

        self.play(FadeIn(circle))

        # 进入交互模式
        self.embed()        



from os import system

if __name__ == "__main__":
    system("manimgl .\manim\text1.py")         
    
