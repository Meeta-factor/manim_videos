from manimlib.imports import *

class Shapes(Scene):
#A few simple shapes
  def construct(self):
    circle = Circle()
    square = Square()
    line=Line(np.array([3,0,0]),np.array([5,0,0]))
    triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

    self.add(line)
    self.play(ShowCreation(circle))
    self.play(FadeOut(circle))
    self.play(GrowFromCenter(square))
    self.play(Transform(square,triangle))

class MoreShapes(Scene):
      def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse=Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))

class latex(Scene):
      def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()  


class FirstLinearTransformation(LinearTransformationScene):
    def construct(self):
        mob = Circle(color=PURPLE)
        mob.move_to(RIGHT+UP*2)
        vector_array1 = np.array([[1], [2]])
        vector_array2 = np.array([[2], [1]])
        matrix = [[2, 0], [1, 1]]
        
        self.add_transformable_mobject(mob)
        self.add_vector(vector_array1,color=YELLOW)
        self.add_vector(vector_array2,color=BLUE)
        self.apply_matrix(matrix)
        self.wait(3)       