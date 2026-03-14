from manim import *
import numpy as np
import random

class FibonacciFancy(MovingCameraScene):
    def construct(self):
        # 一、标题与公式注释
        title = Text("Fibonacci 矩阵及其金色螺旋", font_size=48, color=GOLD_E)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        self.play(title.animate.to_edge(UP).scale(0.7))
        formula = MathTex(
            r"Q^n = \\begin{pmatrix} F_{n+1} & F_n \\\\ F_n & F_{n-1} \\end{pmatrix}",
            font_size=32
        )
        formula.next_to(title, DOWN)
        self.play(Write(formula), run_time=1)
        self.wait(0.5)

        # 二、定义 Q 矩阵并展示
        Q = np.array([[1, 1], [1, 0]])
        mat = Matrix(Q)
        mat.set_color_by_gradient(BLUE, PURPLE)
        mat_group = VGroup(Text("Q =", font_size=36), mat).arrange(RIGHT, buff=0.3)
        mat_group.next_to(formula, DOWN, buff=1)
        self.play(LaggedStart(*[Write(m) for m in mat_group], lag_ratio=0.2), run_time=1)
        self.wait(0.5)

        # 三、动态演示矩阵幂与黄金比收敛
        n = 7
        n_label = MathTex(r"n = %d" % n, font_size=36)
        n_label.next_to(mat_group, DOWN, buff=0.8)
        self.play(Write(n_label), run_time=0.8)
        self.wait(0.5)
        # 初始矩阵
        current_tex = Matrix(Q).scale(0.8).to_edge(LEFT, buff=1)
        self.play(Create(current_tex), run_time=0.7)
        # 初始黄金比标签
        ratio_val = Q[0,0] / Q[0,1]
        ratio_tex = MathTex(rf"\\frac{{F_{{2}}}}{{F_{{1}}}} = {ratio_val:.3f}", font_size=30)
        ratio_tex.next_to(current_tex, UP, buff=0.5)
        self.play(Write(ratio_tex), run_time=0.7)
        self.wait(0.3)
        # 幂运算循环
        for k in range(2, n+1):
            Qk = np.linalg.matrix_power(Q, k)
            next_tex = Matrix(Qk).scale(0.8).to_edge(LEFT, buff=1)
            next_tex.set_color_by_gradient(TEAL, GREEN)
            new_ratio = Qk[0,0] / Qk[0,1]
            new_ratio_tex = MathTex(rf"\\frac{{F_{{{k+1}}}}}{{F_{{{k}}}}} = {new_ratio:.3f}", font_size=30)
            new_ratio_tex.next_to(next_tex, UP, buff=0.5)
            self.play(
                ReplacementTransform(current_tex, next_tex),
                ReplacementTransform(ratio_tex, new_ratio_tex),
                run_time=0.7
            )
            current_tex = next_tex
            ratio_tex = new_ratio_tex
            self.wait(0.2)

        # 四、粒子/光效高亮 Fibonacci 数
        fib_n = np.linalg.matrix_power(Q, n)[0,1]
        fib_tex = MathTex(rf"F_{{{n}}} = {fib_n}", font_size=40, color=YELLOW)
        fib_tex.next_to(current_tex, RIGHT, buff=1)
        self.play(Write(fib_tex), run_time=0.8)
        glow = SurroundingRectangle(fib_tex, buff=0.2, stroke_color=YELLOW, stroke_width=4)
        self.play(Create(glow), run_time=0.5)
        # 粒子效果
        dots = VGroup(*[
            Dot(point=fib_tex.get_center(), radius=0.05, color=YELLOW)
            for _ in range(20)
        ])
        self.add(dots)
        dot_anims = []
        for dot in dots:
            dx, dy = random.uniform(-1,1), random.uniform(-1,1)
            dot_anims.append(
                dot.animate.shift([dx, dy, 0]).fade(1)
            )
        self.play(*dot_anims, run_time=1)
        self.play(FadeOut(dots), FadeOut(glow))
        self.wait(0.5)

        # 五、背景网格 & 相机缩放 & 金色螺旋
        plane = NumberPlane(
            x_range=[-6,6,1], y_range=[-4,4,1],
            background_line_style={"stroke_color":GRAY, "stroke_opacity":0.3}
        )
        plane.set_z_index(-1)
        self.add(plane)
        # 矩阵视图相机缩放
        self.play(
            self.camera.frame.animate.move_to(current_tex.get_center()).scale(1.2),
            run_time=1.5
        )
        self.wait(0.5)
        # 绘制螺旋
        spiral = ParametricFunction(
            lambda t: np.array([
                np.exp(t) * np.cos(t), np.exp(t) * np.sin(t), 0
            ]), t_range=[0, 4*PI], color=GOLD, stroke_width=4
        )
        spiral.move_to(3 * RIGHT + DOWN)
        self.play(Create(spiral), run_time=2.5)
        self.wait(0.5)
        # 相机平滑移动至螺旋
        self.play(
            self.camera.frame.animate.move_to(spiral.get_center()).scale(0.7),
            run_time=1.8
        )
        self.wait(0.5)

        # 六、放大展示螺旋细节
        box = SurroundingRectangle(spiral, buff=0.2)
        self.play(Create(box), run_time=0.5)
        zoomed = spiral.copy().scale(1.5).move_to(ORIGIN)
        self.play(
            Transform(box, SurroundingRectangle(zoomed, buff=0.3)),
            Transform(spiral, zoomed),
            run_time=1.5
        )
        self.wait(1)

        # 七、结束文字
        outro = Text("—— 演示完毕 ——", font_size=30, color=LIGHT_GRAY).to_edge(DOWN)
        self.play(FadeIn(outro, shift=UP), run_time=0.8)
        self.wait(1)
