
import math




def parallelArcLength(**kwargs):
    """
    this function take 3 params
    phi:latitude of the parallel 
    lambda1: longitude of the first meridian 
    lambda2: longitude of the second meridian 
    ref or a&b : ellipsoid params
    this function calculate the meridian arc width
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
    try:
        phi = math.radians(kwargs["phi"])
        e2 = 1-(b/a)**2
        w = math.sqrt(1-e2*math.sin(phi)**2)
        L = a*math.cos(phi)*abs(kwargs["lambda2"]-kwargs["lambda1"])/w
        return {"L": L}
    except KeyError:
        return {"error": "the function required 3 basics params lambda1,lambda2(longitudes),phi(latitude) and ref or a&b"}

# print(merdianArcLength(phi1=10, phi2=9, ref="global"))
# print(parallelArcLength(ref="global",phi=15,lambda1=15,lambda2=20))
