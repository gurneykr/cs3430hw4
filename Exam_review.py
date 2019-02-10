from prod import prod
from plus import plus
from quot import quot
from const import const
from maker import make_const, make_pwr, make_pwr_expr, make_plus, make_prod, make_quot, make_e_expr, make_ln, make_absv
from tof import tof
from deriv import logdiff
from deriv import deriv
from deriv import ln_deriv
import unittest
from poly12 import find_poly_2_zeros
import numpy as np
import matplotlib.pyplot as plt
import math

def problem_0():
    fex1 = make_pwr( make_plus(make_prod(const(4.0),
                                         make_pwr('x', 1.0)),
                               const(1.0)),
                     2.0)


def problem_01():
    # f(x) =(x+1)(2x+1)(3x+1) /(4x+1)^.5
    fex1 = make_plus(make_pwr('x', 1.0), const(1.0))
    fex2 = make_plus(make_prod(const(2.0), make_pwr('x', 1.0)), const(1.0))
    fex3 = make_plus(make_prod(const(3.0), make_pwr('x', 1.0)), const(1.0))
    fex4 = make_prod(fex1, fex2)

    fex5 = make_prod(fex4, fex3)

    fex6 = make_pwr_expr( make_plus(make_prod(const(4.0),
                                         make_pwr('x', 1.0)),
                               const(1.0)),
                     0.5)
    fex = make_quot(fex5, fex6)
    print(fex)
    drv = deriv(fex)
    print('drv: ',drv)
    drvf = tof(drv)
    def gt_drvf(x):
        n = (60.0*x**3)+ (84*x**2)+ 34*x + 4
        d = (4*x+1)**(3/2)
        return n/d
    for i in range(1, 10):
        print(drvf(i), gt_drvf(i))
        assert abs(gt_drvf(i) - drvf(i)) <= 0.001

    assert drv is not None
    print(drv)

    # zeros = find_poly_2_zeros(drv)
    # print(zeros)

    f1 = tof(fex)
    f2 = tof(deriv(fex))

    xvals = np.linspace(1, 5, 10000)
    yvals1 = np.array([f1(x) for x in xvals])
    yvals2 = np.array([f2(x) for x in xvals])
    fig1 = plt.figure(1)
    fig1.suptitle('Graph')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim()
    plt.xlim()
    plt.grid()
    plt.plot(xvals, yvals1, label=fex.__str__(), c='r')
    plt.plot(xvals, yvals2, label=deriv(fex).__str__(), c='g')
    plt.legend(loc='best')
    plt.show()

def problem_02():
    fex1 = make_pwr('x', 2.0)
    fex2 = make_ln(make_pwr('x', 1.0))
    fex = make_prod(fex1, fex2)
    print('f(x)= ', fex)
    d = deriv(fex)
    print('first drv = ', d)
    drv = deriv(d)
    print("second drv = ", drv)
    drvf = tof(drv)
    gt = lambda x: 2*math.log(x) + 3
    for i in range(1, 10):
        print(drvf(i), gt(i))
        assert abs(gt(i) - drvf(i)) <= 0.001



if __name__ == "__main__":
    problem_02()