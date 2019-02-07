from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from quot import quot
from maker import make_const, make_pwr, make_pwr_expr, make_plus, make_prod, make_quot, make_e_expr, make_ln, make_absv
from tof import tof
from deriv import deriv
import unittest
import math

class Assign01UnitTests(unittest.TestCase):

    # def test_01(self):
    #     #e^(5x) drv = ((2.71828182846^(5.0*(x^1.0)))*(5.0*(1.0*(x^0.0))))
    #     print('*******Test 01 ********')
    #     fex = make_e_expr(make_prod(make_const(5.0), make_pwr('x', 1.0)))
    #     print(fex)
    #     drv = deriv(fex)
    #     assert not drv is None
    #     print(drv)
    #     drvf = tof(drv)
    #     assert not drvf is None
    #     gt = lambda x: 5.0*(math.e**(5.0*x))
    #     for i in range(10):
    #         print(drvf(i), gt(i))
    #         assert abs(gt(i) - drvf(i)) <= 0.001
    #     print('Test 01: pass')
    #
    # def test_02(self):
    #     #e^((x^2)-1) drv = ((2.71828182846^((x^2.0)+-1.0))*((2.0*(x^1.0))+0.0))
    #     print('*******Test 02 ********')
    #     fex = make_e_expr(make_plus(make_pwr('x', 2.0),make_const(-1.0)))
    #     print(fex)
    #     drv = deriv(fex)
    #     assert not drv is None
    #     print(drv)
    #     drvf = tof(drv)
    #     assert not drvf is None
    #     gt = lambda x: 2*x*(math.e**2(x**2 - 1.0))
    #     for i in range(10):
    #         print(drvf(i), gt(i))
    #         assert abs(gt(i) - drvf(i)) <= 0.001
    #     print('Test 02: pass')
    #
    # def test_03(self):
    #     '''e^(x-(1/x)) = ((2.71828182846^((x^1.0)+(-1.0/(x^1.0))))*((1.0*(x^0.0))+((((x^1.0)*0.0) +
    #                                                                                     (-1.0*(-1.0*(1.0*(x^0.0)))))/((x^1.0)^2.0))))
    #     '''
    #     print('*******Test 03 ********')
    #     fex1 = make_quot(make_const(-1.0), make_pwr('x', 1.0))
    #     fex2 = make_e_expr(make_plus(make_pwr('x', 1.0), fex1))
    #     print(fex2)
    #     drv = deriv(fex2)
    #     assert not drv is None
    #     print(drv)
    #     drvf = tof(drv)
    #     assert not drvf is None
    #     def gt_drvf(x):
    #         d = (x -1.0/x)
    #         return (math.e**d)*(1.0 + 1.0/(x**2))
    #     err = 0.0001
    #     for i in range(1, 10):
    #         print(drvf(i), gt_drvf(i))
    #         assert abs(gt_drvf(i) - drvf(i)) <= err
    #     print('Test 03: pass')
    #
    # def test_04(self):
    #     '''
    #      (3e^(2x))/((1+x^2)) drv = ((((1.0+(x^2.0))*(3.0*((2.71828182846^(2.0*(x^1.0)))*(2.0*(1.0*(x^0.0))))))
    #                                 +(-1.0*((3.0*(2.71828182846^(2.0*(x^1.0))))*(0.0+(2.0*(x^1.0)))))) / ((1.0+(x^2.0))^2.0))
    #
    #     '''
    #     print('*******Test 04 ********')
    #     n = make_prod(make_const(3.0), make_e_expr(make_prod(make_const(2.0), make_pwr('x', 1.0))))
    #     d = make_plus(make_const(1.0), make_pwr('x', 2.0))
    #     fex = make_quot(n, d)
    #     print(fex)
    #     drv = deriv(fex)
    #     assert not drv is None
    #     print(drv)
    #     drvf = tof(drv)
    #     assert not drvf is None
    #     def gt_drvf(x):
    #         n = 6.0*(math.e**(2.0*x))*(x**2 - x + 1.0)
    #         d = (1 + x**2)**2
    #         return n/d
    #     for i in range(-10, 10):
    #         print(drvf(i), gt_drvf(i))
    #         assert abs(gt_drvf(i) - drvf(i)) <= 0.001
    #     print('Test 04: pass')

    # def test_05(self):
    #     '''
    #     (ln 5x)drv = ((5.0*(ln(x^1.0)^4.0))*((1.0/(x^1.0))*(1.0*(x^0.0))))
    #     '''
    #     print('*******Test 05********')
    #     fex = make_ln(make_prod(const(5.0), make_pwr('x', 1.0)))
    #     #fex = make_pwr_expr(make_ln(make_pwr('x', 1.0)), 5.0)
    #     print(fex)
    #     drv = deriv(fex)
    #     assert not drv is None
    #     print(drv)

    # def test_05(self):
    #     '''
    #     (ln x)^5 drv = ((5.0*(ln(x^1.0)^4.0))*((1.0/(x^1.0))*(1.0*(x^0.0))))
    #     '''
    #     print('*******Test 05********')
    #     fex = make_pwr_expr(make_ln(make_pwr('x', 1.0)), 5.0)
    #     print(fex)
    #     drv = deriv(fex)
    #     assert not drv is None
    #     print(drv)
    #     drvf = tof(drv)
    #     assert not drvf is None
    #     gt = lambda x: (5.0*(math.log(x, math.e)**4))/x
    #     err = 0.0001
    #     for i in range(1, 5):
    #         print(drvf(i), gt(i))
    #         assert abs(gt(i) - drvf(i)) <= err
    #     print('Test 05: pass')

    # def test_06(self):
    #     '''
    #     x ln(x) drv =  (((x^1.0)*((1.0/(x^1.0))*(1.0*(x^0.0))))+(ln(x^1.0)*(1.0*(x^0.0)))
    #     '''
    #     print('*******Test 06********')
    #     fex = make_prod(make_pwr('x', 1.0), make_ln(make_pwr('x', 1.0)))
    #     print(fex)
    #     drv = deriv(fex)
    #     assert not drv is None
    #     print(drv)
    #     drvf = tof(drv)
    #     assert not drvf is None
    #     gt = lambda x: 1.0 + math.log(x, math.e)
    #     err = 0.0001
    #     for i in range(1, 10):
    #         print(drvf(i), gt(i))
    #         assert abs(gt(i) - drvf(i)) <= err
    #     print('Test 06: pass')

    def test_07(self):
        '''
        ln(x e^x) drv =  (((1.0/(x^1.0))*(1.0*(x^0.0)))+((1.0/(2.71828182846^(x^1.0)))* x‘((2.71828182846^(x^1.0))*(1.0*(x^0.0)))))
        '''
        print('*******Test 07********')
        fex0 = make_prod(make_pwr('x', 1.0), make_e_expr(make_pwr('x', 1.0)))
        fex = make_ln(fex0)
        print(fex)
        drv = deriv(fex)
        assert not drv is None
        print("drv: ",drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: (x + 1.0)/x
        err = 0.0001
        for i in range(1, 10):
            print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        for i in range(-10, -1):
            print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        print('Test 07: pass')

    # def test_08(self):
    #     #ln|x| drv = ((x^1.0)^-1.0)
    #     print('*******Test 08********')
    #     fex = make_ln(make_absv(make_pwr('x', 1.0)))
    #     print(fex)
    #     drv = deriv(fex)
    #     assert not drv is None
    #     print(drv)
    #     drvf = tof(drv)
    #     assert not drvf is None
    #     gt = lambda x: 1.0/x
    #     err = 0.0001
    #     for i in range(1, 10):
    #         print(drvf(i), gt(i))
    #         assert abs(gt(i) - drvf(i)) <= err
    #     print('Test 08: pass')

    # def test_09(self):
    #     '''x(x+1)(x+2) drv = (((x^1.0)*(((x^1.0)+1.0)*((x^1.0)+2.0)))*(((1.0/(x^1.0))*(1.0*(x^0.0)))+
    #                             (((1.0/((x^1.0)+1.0))*((1.0*(x^0.0))+0.0))+((1.0/((x^1.0)+2.0))* ((1.0*(x^0.0))+0.0)))))
    #     '''
    #     print('*******Test 09********')
    #     fex = make_prod(make_pwr('x', 1.0),
    #                     make_prod(make_plus(make_prod('x', 1.0),
    #                                         make_const(1.0)),
    #                               make_plus(make_pwr('x', 1.0),
    #                                         make_const(2.0))))
    #     drv = logdiff(fex)
    #     assert not drv is None
    #     print(drv)
    #     drvf = tof(drv)
    #     assert not drvf is None
    #     def gt_drvf(x):
    #         x = x*(x+1.0)*(x+2.0)
    #         z2 = (1.0/x + 1.0/(x + 1.0) + 1.0/(x + 2.0))
    #         return x * z2
    #     err = 0.0001
    #     for i in range(1, 10):
    #         print(drvf(i), gt_drvf(i))
    #         assert abs(gt_drvf(i) - drvf(i)) <= err
    #     for i in range(-10, -1):
    #         if i == -1 or i == -2:
    #             continue
    #         print(drvf(i), gt_drvf(i))
    #         assert abs(gt_drvf(i) - drvf(i)) <= err
    #     print('Test 09: pass')

    # def test_10(self):
    #     '''
    #     (x^2 +1)(x^3 -3)(2x + 5) drv =
    #     '''
    #     print('*******Test 10********')
    #     fex1 = make_plus(make_pwr('x', 2.0), make_const(1.0))
    #     fex2 = make_plus(make_pwr('x', 3.0), make_const(-3.0))
    #     fex3 = make_plus(make_prod(make_const(2.0),
    #                                make_pwr('x', 1.0)),
    #                      make_const(5.0))
    #     fex = make_prod(fex1, make_prod(fex2, fex3))
    #     print(fex)
    #     drv = logdiff(fex)
    #     assert not drv is None
    #     print(drv)
    #     drvf = tof(drv)
    #     assert not drvf is None
    #     def gt_drvf(x):
    #         z = (x**2 + 1.0)*(x**3 - 3.0)*(2*x + 5.0)
    #         z2 = ((2.0*x)/(x**2 + 1) + (3.0*(x**2))/(x**3 - 3.0)+ 2.0/(2*x + 5.0))
    #         return z * z2
    #     err = 0.0001
    #     for i in range(1, 10):
    #         print(drvf(i), gt_drvf(i))
    #         assert abs(gt_drvf(i) - drvf(i)) <= err
    #     print('Test 10: pass')
    #
    # def test_11(self):
    #     '''
    #     (x+1)^4 *(4x-1)^2
    #     '''
    #     print('*******Test 10********')
    #     fex1 = make_pwr_expr(make_plus(make_pwr('x', 1.0), make_const(1.0)), 4.0)
    #     fex2 = make_pwr_expr(make_plus(make_prod(make_const(4.0),
    #                                              make_pwr('x', 1.0)),
    #                                    make_const(-1.0)), 2.0)
    #     fex = make_prod(fex1, fex2)
    #     print(fex)
    #     drv = logdiff(fex)
    #     assert not drv is None
    #     print(drv)
    #     drvf = tof(drv)
    #     assert not drvf is None
    #     def gt_drvf(x):
    #         z1 = ((x + 1.0) **4.0) * ((4*x - 1.0)** 2.0)
    #         z2 = (4.0/(x + 1.0)) + (8.0/ (4*x - 1.0))
    #         return z1 * z2
    #
    #     err = 0.0001
    #     for i in range(1, 10):
    #         print(drvf(i), gt_drvf(i))
    #         assert abs(gt_drvf(i) - drvf(i)) <= err
    #     print('Test 11: pass')

    if __name__ == "__main__":
        unittest.main()