import pytest
from pythonCode.calculator import CalCuLator
#先导库，导包，添加setup公用变量，mark设定参数化。
class Test_CalCuLator():

    def setup_class(self):
        self.calc=CalCuLator()
        print("计算开始")
    def teardown_class(self):
        print("结束计算")
    @pytest.mark.parametrize("a,b,expect",[(1,2,3),(200,400,600),(-2,-3,-5)])
    def test_add(self,a,b,expect):
         assert expect==self.calc.add(a,b)

    @pytest.mark.parametrize("a,b,expect",[(6,3,3),(1000,500,500),(-3,-6,3)])
    def test_sub(self,a,b,expect):
        assert expect==self.calc.sub(a,b)
    @pytest.mark.parametrize("a,b,expect",[(1,2,2),(-2,-3,6),(0.2,0.6,0.12),(3.14,3,9.42)])
    def test_mul(self,a,b,expect):
        assert expect==self.calc.mul(a,b)
    @pytest.mark.parametrize("a,b,expect",[(6,3,2),(2000,200,10),(0.66,0.3,2.2),(-6,-2,3)])
    def test_div(self,a,b,expect):
        assert expect==self.calc.div(a,b)
