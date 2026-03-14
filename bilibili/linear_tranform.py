from manimlib import *
from os import system
if __name__ == "__main__":
    system('manimgl {}  -c BLACK'.format(__file__))

class trans(Scene):
    def construct(self) -> None:
       T=TexText("$Linear Transformation$")
       npl=NumberPlane()
       mat1 = np.array([
            [1,6],
            [2,-1]
            ])
       mat2 = np.array([
            [-3,6],
            [1,4]
            ])
       VG=VGroup(npl,T)

     #   self.play(ShowCreation(npl),ShowCreation(T))
       self.play(ApplyMatrix(mat1,npl),ApplyMatrix(mat1,T))
     #   self.play(ApplyMatrix(mat2,npl),ApplyMatrix(mat2,T))
       self.play(VG.animate.apply_complex_function(lambda x: x**2),run_time=6)

