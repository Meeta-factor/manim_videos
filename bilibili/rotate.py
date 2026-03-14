from manimlib import *
from os import system
if __name__ == "__main__":
    system('manimgl {}'.format(__file__))
def FadeIO(self):
    def __init__(self,text,*args,**kwargs):
       self.play(FadeIn(text))
       self.play(FadeOut(text))
class base(Scene):
    biaoti="PangMenZhengDao"
    putong="Alimama DaoLiTi"
    zimu="ZSDYLZWR"
    def construct(self):
        text0 = Text("听说你的朋友很聪明", font=self.biaoti,color=PURPLE)       
        text1=Text('那就让他看看这个吧',font=self.biaoti,color=ORANGE)
        # text1=Text('那就让他看看这个吧',font="biaoti",color=ORANGE)
        text1.next_to(text0,DOWN)
        self.play(WiggleOutThenIn(text0))
        self.play(Write(text1))
        self.play(FadeOut(text0),FadeOut(text1))
class test(Scene):
    
    biaoti="PangMenZhengDao"
    putong="Alimama DaoLiTi"
    zimu="ZSDYLZWR"
    back='blackboard.jpg' 
    def construct(self):
        rotate=Tex(r'\begin{bmatrix}\cos\phi  &-\sin\phi  \\\sin\phi&\cos\phi \end{bmatrix}',color=GOLD_A).to_edge(UP)
        rota1=Tex(r'\begin{bmatrix}\cos\phi  &-\sin\phi  \\\sin\phi&\cos\phi \end{bmatrix}^{n}',color=GOLD_A).to_edge(LEFT)
        rota2=Tex(r'=\begin{bmatrix}\cos n\phi  &-\sin n\phi  \\\sin n\phi&\cos n\phi \end{bmatrix}',color=GOLD_A).next_to(rota1,RIGHT)
        zimu1=Text('我们让坐标系旋转三次',font=self.zimu).to_edge(DOWN)
        zimu2=Text('每次十坤度,也就是二十五度',font=self.zimu).to_edge(DOWN)
        zimu3=Text('每做一次变换,角度就会加倍',font=self.zimu).to_edge(DOWN)
        zimu4=Text('我们就会得到这个公式',font=self.zimu).to_edge(DOWN)
        self.add(ImageMobject(self.back).scale(2))
        npl=NumberPlane().scale(5)
        self.play(ShowCreation(npl))
        self.play(FadeIO(zimu1)) 
        self.play(ShowCreation(rotate)) 
       
        self.play(FadeIO(zimu2))
       
        for i in range(1,4):  
           label=Tex(r'\phi=',color=GOLD_A).to_corner(UP+LEFT)
           j=DecimalNumber(i*25).next_to(label,RIGHT)
           j.add_updater(lambda x:x.next_to(label,RIGHT))
           j.add_updater(lambda x:x.set_value(i*25))
           theta=25*DEGREES
           mat = np.array([
            [math.cos(theta),-math.sin(theta)],
            [math.sin(theta),math.cos(theta)]
            ])
           
           self.add(j,label)
           self.play(ApplyMatrix(mat,npl))
           
        # self.embed()
        self.play(FadeOut(npl))  
        self.play(ReplacementTransform(rotate,rota1))
        self.play(FadeIO(zimu3))
        
        self.play(Write(rota2),FadeIn(zimu4))