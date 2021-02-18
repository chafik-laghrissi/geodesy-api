import math
from scipy import integrate


def CalculateArea(**kwargs):
    """
    This function calculate the area limited by two parallels with latitude phi1 and phi2 and two meridians with 
    longitudes lambda1 & lambda2
    Arguments:
    phi1 and phi2: latitudes
    lambda1 and lambda2: longitudes
    ref or a&b: params of ellipsoid
    """
    a = 0
    b = 0
    try:
        if kwargs["ref"] == "local":
            a = 6378249.145
            b = 6356515
        elif kwargs["ref"] == "global":
            a = 6378137
            b = 6356752.314
        elif kwargs["a"] and kwargs["b"]:
            a = kwargs["a"]
            b = kwargs["b"]
    except KeyError:
        return {"error": "params a and b is required, you can use ref too which has two possible value: local and global"}
    try:
        e2 = 1-(b/a)**2

        def integral(x):
            return math.cos(x)*(1-e2*math.sin(x)**2)**-2
        y = integrate.romberg(integral, math.radians(
            kwargs["phi1"]), math.radians(kwargs["phi2"]))
        return {"S": (kwargs["lambda2"]-kwargs["lambda1"])*y*b**2}
    except KeyError:
        return {"error": "oops something went wrong, one of the basic arguments isn't found, this function take 5 arguments => phi1 and phi2: latitudes lambda1 and lambda2: longitudes,ref or a&b: params of ellipsoid"}
# print(CalculateArea(ref="global",phi1=15,phi2=30,lambda1=10,lambda2=50))
