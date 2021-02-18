import math


def rayonDeCourbur(**kwargs):
    """
    this function calculate radius of merdian and first vertical
    phi: latitude =>angle in degrees
    a and b : prams of ellipsoid
    optional: ref 
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
        return {"erreur": "params a and b is required, you can use ref too which has two possible value: local and global"}
    if a != 0 and b != 0:
        try:
            phi=math.radians(kwargs["phi"])
            e2 = 1-(b/a)**2
            w = math.sqrt(1-e2*math.sin(phi)**2)
            M = a*(1-e2)/w**3
            N = a/w
            if "alpha" in kwargs.keys():
                alpha = math.radians(kwargs["alpha"])
                rAlpha = (M*N)/(M*math.sin(alpha)**2+N*math.cos(alpha)**2)
                return{"M": M, "N": N, "rAlpha": rAlpha,"1/R":1/rAlpha}
            elif kwargs["radius"]=="M":
                return {"M": M}
            elif kwargs["radius"]=="N":
                return {"N":N}
        except KeyError as err:
            return {"erreur": f"{format(err)} is required!"}


# print(rayonDeCourbur(phi=10, ref="local", alpha=20))
