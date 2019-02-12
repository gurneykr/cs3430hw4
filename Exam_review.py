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
from hw03 import maximize_revenue
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

def problem_03():
    fex = make_e_expr(make_pwr('x', 1.0))
    print("f(x)= ",fex)
    drv = deriv(fex)
    print("f'(x)= ",drv)
    drvf = tof(drv)
    print("f'(-1)= ",drvf(-1))

def problem_04():
    #x^2 -4y^2 = 9 when x = 5, y = -2, dx/dt = 3
    x = 5.0
    y = -2.0
    dx_dt = 3.0

    fex1 = make_pwr('x', 2.0)
    fex2 = make_prod(const(-4.0), make_pwr('y', 2.0))
    fex3 = make_plus(fex1, fex2)
    print('f(x)=',fex3)
    drv = deriv(fex3)
    print("f'(x)=", drv)
    top = drv.get_elt1()

    bottom = make_prod(const(-1.0), drv.get_elt2())

    dy_dt = (tof(top)(x)* dx_dt)/ (tof(bottom)(y))
    print("dy_dt: ", dy_dt)

    '''
    d/dt(x^2) - d/dt(4y^2) =  d/dt 9
    2x dx/dt - 8y dy/dt = 0   , subtract 8y
    2x dx/dt  = 8y dy/dt , divide both sides by 8y to solve for dy/dt
    (2x)/(8y) dx/dt = dy/dt
    plug in x, y and dx/dt  to solve for dy/dt
    dy/dt = -1.875

    '''
def problem_06():

    demand_expr = make_plus(make_prod(const(-0.001), make_pwr('x', 1.0)), const(2.0))
    print(demand_expr)
    num_units, rev, price = maximize_revenue(demand_expr, constraint=lambda x: 0 <= x <= 1000)
    print('x = ', num_units.get_val())
    print("rev= ", rev.get_val())
    print('price = ', price.get_val())

def problem_07():
    pass

#problem 8 is the same as problem 4 in HW3

def problem_09():
    fex = make_e_expr(make_prod(const(-0.021), make_pwr('x', 1.0)))
    print(fex)
    P0 = const(8.0)
    expr, decay_const = fun1(fex, P0)

    print("f(x)= ",expr,"lambda=", decay_const)
    remaining = fun2(expr, 3.0)
    print("remaining= ", remaining)
    remaining_after_n_years = fun3(expr, 2.0, 3.0)


def fun1(expr, P0):#finds lambda= decay_const
    newExpr = make_prod(P0, expr)
    decay_const = expr.get_deg().get_mult1()
    return newExpr, decay_const


def fun2(expr, n):#computes remaining material after n years
    remaining = tof(expr)(n)
    return remaining

def fun3(expr, half_life, n):
    print("inside fun3")
    p0 = expr.get_mult1().get_val()
    lam_da = expr.get_mult2().get_deg().get_mult1().get_val()
    print("type p0", type(p0))
    print("type lambda ", type(lam_da))
    inside = half_life / p0
    t = math.e(inside) / lam_da
    print('t= ', t)

if __name__ == "__main__":
    problem_09()