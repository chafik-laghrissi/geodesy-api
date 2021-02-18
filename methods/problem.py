import math


def directProblem(**kwargs):
    """
    this function resolve the direct problem of a polar spheral triangle
    arguments:
    phi1:latitude of the first point
    a12:azimuth calculated from the first pint to the second point
    lambda1:longitude of the first point
    d: distance between the two points 
    """
    try:
        phi1 = math.radians(kwargs["phi1"])
        a12 = math.radians(kwargs["a12"])
        phi2 = math.degrees(math.asin(math.sin(
            phi1)*math.cos(kwargs["d"]+math.cos(phi1)*math.sin(kwargs["d"])*math.cos(a12))))
        lambda2 = kwargs["lambda1"] + math.degrees(math.atan(math.sin(kwargs["d"])*(-math.cos(
            math.pi/2-phi1)*math.cos(a12)+math.sin(math.pi/2-phi1)/math.tan(kwargs["d"]))))
        a21 = math.degrees(math.sin(
            a12)/(math.cos(kwargs["d"])*math.cos(a12)+math.tan(phi1)*math.sin(kwargs["d"])))
        return {"phi2": phi2, "a21": a21, "lambda2": lambda2}
    except KeyError:
        return {"error": "oops! something went wrong! an required arguments missed, required arguments=>  phi1:latitude of the first point, a12:azimuth calculated from the first point to the second point, lambda1:longitude of the first point and d: distance between the two points "}


def inversProblem(**kwargs):
    """
    this function resolve the invers problem of a polar spheral triangle
    arguments:
    phi1:latitude of the first point
    lambda1:longitude of the first point
    phi2:latitude of the second point
    lambda2:longitude of the second point
    """
    try:
        phi1 = math.radians(kwargs["phi1"])
        phi2 = math.radians(kwargs["phi2"])
        lambda1 = math.radians(kwargs["lambda1"])
        lambda2 = math.radians(kwargs["lambda2"])
        deltaLambda = lambda2-lambda1
        d = math.acos(math.sin(phi1)*math.sin(phi2)+math.cos(phi2)
                      * math.cos(phi1)*math.cos(deltaLambda))
        a12 = math.degrees(math.atan((math.sin(deltaLambda)*math.tan(deltaLambda))/(math.tan(
            deltaLambda)*math.tan(phi2)*math.cos(phi1)-math.sin(phi1)*math.sin(deltaLambda))))
        a21 = math.degrees(math.atan((math.sin(deltaLambda)*math.tan(deltaLambda))/(-math.tan(
            deltaLambda)*math.tan(phi1)*math.cos(phi2)+math.sin(phi2)*math.sin(deltaLambda))))
        return{"d": d, "a12": a12, "a21": a21}
    except KeyError:
        return{"error": "oops! something went wrong! an required arguments missed, required arguments=>  phi1:latitude of the first point,lambda1:longitude of the first point,phi2:latitude of the second point and lambda2:longitude of the second point"}


# print(directProblem(phi1=12, a12=20, lambda1=50, d=10))
# print(inversProblem(phi1=15,phi2=27,lambda1=50,lambda2=123))
