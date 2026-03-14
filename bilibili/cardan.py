from manimlib import *
from os import system
if __name__ == "__main__":
    system("manimgl {}  -c BLACK ".format(__file__))

class Title(Scene):
    def construct(self):
        text0 = Text("听说你的朋友很厉害。\n", font="Microsoft YaHei",color=PURPLE)
        text1=Text('那就让Ta来看看这个吧。',font="Microsoft YaHei",color=ORANGE)
        text1.next_to(text0,DOWN)
        self.play(Write(text0))
        self.play(Write(text1))
        self.wait(2)
        self.play(FadeOut(text0),FadeOut(text1))
       

class scene1(Scene):
    def construct(self):
        text0 = Text("我们都知道一元二次方程的求根公式是", font="KaiTi").to_edge(UP+LEFT).scale(1)
        tex0=Tex(r"x_{1,2}=\frac{-b\pm \sqrt{b^{2}-4ac}}{2a} ",font="Arial").next_to(text0,DOWN)
        text1=Text("那么，我们如何求一元三次方程的求根公式呢？",font="KaiTi",color=GOLD_A).next_to(tex0,DOWN).scale(0.7)
        self.play(Write(text0))
        self.play(Write(tex0))
        self.play(Write(text1))
        self.wait(3)

class scene2(Scene):
    def construct(self):
        text0 = Text("首先，我们给出一元三次方程的一般形式：", font="KaiTi").to_corner(UP+LEFT).scale(0.8)
        tex0=Tex(r"y^{3}+a_{1}y^{2}+a_{2}y+a_{3}=0",font="Arial").next_to(text0,DOWN)
        text=Text("令",font="KaiTi").next_to(tex0,DOWN).to_edge(LEFT).scale(0.8)
        tex=Tex(r"y-\alpha \longrightarrow x\Rightarrow y=x+\alpha ",color=BLUE).next_to(text,RIGHT)
        tex1=VGroup(text,tex)
        
        T0=Text("那么，我们将其代入可以推出：", font="KaiTi").next_to(tex1,DOWN).scale(0.8).to_edge(LEFT)
        tex2_1=Tex(r"(x+\alpha )^{3}+a_{1}(x+\alpha)^{2}+a_{2}(x+\alpha)+a_{3}=0",font="Arial").scale(0.8)
        tex2_2=Tex(r"x^{3}+3\alpha x^{2}+3\alpha^{2}x+\alpha+a_{1}(x^{2}+2\alpha x+\alpha^{2})+a_{2}(x+\alpha)+a_{3}=0",font="Arial").next_to(tex2_1,DOWN).scale(0.8)
        tex2_3=Tex(r"x^{3}+(3\alpha+a_{1}) x^{2}+(3\alpha^{2}+2a_{1}\alpha +a_{2})x+(\alpha+a_{1}\alpha^{2}+a_{2}\alpha+a_{3})=0",font="Arial",color=GOLD).next_to(tex2_2,DOWN).scale(0.8)
        tex2=VGroup(tex2_1,tex2_2,tex2_3)
        tex3=Tex(r"x^{3}+px+q=0",font="Arial",color=PURPLE).to_edge(LEFT).next_to(tex2,DOWN)
        T=Text("对比一下，可以得到", font="KaiTi").scale(0.8).move_to([-3.8,2,0])
        dedao=Tex(r"\begin{cases} 0=3\alpha +a_{1}\\p=3\alpha^{2}+2a_{1}\alpha +a_{2}=a_{2}-\frac{1}{3}a_{1}^{2} \\q=\alpha +a_{1}\alpha ^{2}+a_{2}\alpha+a_{3}=a_{3}-\frac{1}{3}a_{1}a_{2}+\frac{2}{27}a_{1}^{3}\\  \end{cases}")
        dedao.align_to(T)
        de_dao=Tex(r"\begin{cases}\alpha= -\frac{a_{1}}{3} \\ p=a_{2}-\frac{1}{3}a_{1}^{2} \\ q=a_{3}-\frac{1}{3}a_{1}a_{2}+\frac{2}{27}a_{1}^{3}\\ \end{cases}",color=RED_A)
        T1=VGroup(tex2_3,tex3)
        fade1=VGroup(text0,tex0,tex1,T0,tex2_1,tex2_2)
        self.play(Write(text0))
        self.play(Write(tex0))
        self.play(Write(tex1))
        self.play(Write(T0))
        self.play(*[Write(tex2_i)for tex2_i in tex2])
        self.play(TransformFromCopy(tex2_3,tex3))
        self.play(AnimationOnSurroundingRectangle(T1))
        self.play(FadeOut(fade1),T1.animate.shift(5*UP).scale(0.85))
        self.play(Write(T))
        self.play(Write(dedao))
        self.play(Transform(dedao,de_dao))
        self.wait(4)

        #self.embed()

class scene3(Scene):
    def construct(self):
        tex0=Tex(r"x^{3}+px+q=0",font="Arial").to_corner(LEFT+UP)
        text=Text("令",font="KaiTi").next_to(tex0,DOWN).to_edge(LEFT).scale(0.8)
        tex=Tex(r"x=u+v",color=BLUE).next_to(text,RIGHT)
        text0=VGroup(text,tex)
        text1=Text("根据二项式定理：",font="KaiTi").next_to(text0,DOWN).to_edge(LEFT).scale(0.8)
        tex1=Tex(r"x^3 = u^3+v^3+3u^2v+3uv^2").next_to(text1,DOWN).to_edge(LEFT)
        tex2=Tex(r"x^3 = u^3+v^3+3uv(u+v)").next_to(text1,DOWN).to_edge(LEFT)
        tex3=Tex(r"x^3 = u^3+v^3+3uvx").next_to(text1,DOWN).to_edge(LEFT)
        tex4=Tex(r"x^3 -3uvx-(u^3+v^3)=0").next_to(tex3,DOWN).to_edge(LEFT)

        text2=Text("由于韦达定理：",font="KaiTi").next_to(tex4,DOWN).to_edge(LEFT).scale(0.8)
        tex01=Tex(r"\begin{cases}-p=3uv\\u^3+v^3=-q\end{cases}").next_to(text2,DOWN).to_edge(LEFT)
        tex02=Tex(r"\begin{cases}u^3v^3=(uv)^3=(-\frac{p}{3})^3\\u^3+v^3=-q\end{cases}").next_to(text2,DOWN).to_edge(LEFT)
        
        l = DashedLine(
            start=UP * 4,
            end=DOWN * 4,
            dash_length=0.05,
            dash_spacing=0.3,
            positive_space_ratio=0.5,
            color=GREEN_C)
        

        text3_0=Tex(r"z^2+qz-(\frac {p}{3} )^3=0").next_to(l,RIGHT).to_edge(UP).scale(0.8)
        text3_1=TexText("显然$u^3,v^3$是方程的根",font="KaiTi").next_to(l,RIGHT).next_to(text3_0,DOWN).scale(0.8)
        text3=VGroup(text3_0,text3_1)
        text4=Tex(r"\Delta =q^2+4(\frac{p}{3})^3").next_to(l,RIGHT).next_to(text3,DOWN).scale(0.8)
        tex41=Tex(r"\begin{cases}u^3=\frac{-q+\sqrt{\Delta}}{2}\\v^3=\frac{-q-\sqrt{\Delta}}{2}\end{cases}").next_to(l,RIGHT).next_to(text4,DOWN).scale(0.8)
        tex42=Tex(r"\begin{cases}u^3=\frac{-q}{2}+\sqrt{\frac{q^2}{4}+\frac{p^3}{27}}=R_1\\v^3=\frac{-q}{2}-\sqrt{\frac{q^2}{4}+\frac{p^3}{27}}=R_2\end{cases}").next_to(l,RIGHT)
        tex5=Tex(r"x=\sqrt[3]{R_1}+\sqrt[3]{R_2}").next_to(l,RIGHT).next_to(text3,DOWN).scale(0.8).next_to(l,RIGHT).next_to(tex41,DOWN).scale(1.1)
        text6=Text("卡丹公式",font="KaiTi").next_to(tex5,DOWN).scale(0.8)



        self.play(Write(tex0))
        self.play(Write(text0))
        self.play(Write(text1))
        self.play(Write(tex1))
        self.play(ReplacementTransform(tex1,tex2))
        self.play(ReplacementTransform(tex2,tex3))
        self.play(Write(tex4))
        self.play(Write(text2))
        self.play(Write(tex01))
        self.play(ReplacementTransform(tex01,tex02))
        self.wait(3)
        self.play(ShowCreation(l))
        self.wait()
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(tex41))
        self.play(ReplacementTransform(tex41,tex42))
        self.play(Write(tex5))
        self.play(ShowCreation(SurroundingRectangle(tex5)))
        self.play(Write(text6))
        self.wait(5)

class End(Scene):
    def construct(self):
        text0 = Text("怎么样？", font="Microsoft YaHei")
        text1=Text('很简单吧！',font="Microsoft YaHei")
        text1.next_to(text0,DOWN)
        self.play(Write(text0))
        self.play(Write(text1))
        self.play(FadeOut(text0),FadeOut(text1))
        self.wait()




        


             


