import foo.subpkg1


def f(x):
    print "subpkg2:", x
    foo.subpkg1.f("subpkg2")
