import pytest

#模块执行开始结束setup/teardown_module
def setup_module():
    print("setup:整个模块只执行一次开始")
def teardown_module():
    print("teardown:整个模块只执行一次结束")
#非类中执行开始结束setup/teardown_function
def setup_function():
    print("不在类中执行用例的开始")
def teardown_function():
    print("不在类中执行用例的结束")

def test_addthree():
    print("test_addthree")
def test_addfour():
    print("tesr_addfour")

class Test_pration():
   #类中执行开始结束setup/teardown_class
    def setup_class(self):
        print("setup:类中用例执行开始")
    def teardown_class(self):
        print("setup:类中用例执行结束")
    #类中方法执行开始结束setup/teardown_method
    def setup_method(self):
        print("setup:每个用例的开始")
    def teardown_method(self):
        print("teardown:每个用例的结束")
    def test_add_one(self):
        print("addOne")
    def test_add_two(self):
        print("addtwo")