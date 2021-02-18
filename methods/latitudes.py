import math


def latitudes(**kwargs):
    """
    this function calculate the 3 latitude 
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

    if a != 0 and b != 0:
        if "phi" in kwargs.keys():
            return {"beta": math.atan((b/a)*math.tan(kwargs["phi"])), "psi": math.atan(math.tan(kwargs["phi"])*(b/a)**2)}
        elif "beta" in kwargs.keys():
            return {"phi": math.atan((a/b)*math.tan(kwargs["beta"])), "psi": math.atan(math.tan(kwargs["beta"])*(b/a))}
        elif "psi" in kwargs.keys():
            return {"beta": math.atan((a/b)*math.tan(kwargs["psi"])), "phi": math.atan(math.tan(kwargs["psi"])*(a/b)**2)}
        else:
            return {"error": "unexpected parametre! supported params are phi,beta and psi"}

    else:
        return {"error": "the attribute ref it's necessary for this operation, and it take on of two values:local or global"}

# print(latitudes(alpha=2,ref="global"))
