import math


def ellipsoidParams(**kwargs):

    try:
        if {'a', 'b'}.issubset(kwargs.keys()):
            f = 1-kwargs["b"]/kwargs["a"]
            e1 = math.sqrt(2*f-f**2)
            e2 = math.sqrt((kwargs["a"]**2-kwargs["b"]**2)/kwargs["b"]**2)
            c = kwargs["a"]/(1-f)
            alpha = math.atan(e2)
            return {"f": f, "e1": e1, "e2": e2, "c": c, "alpha": math.degrees(alpha)}
        elif {"a", "f"}.issubset(kwargs.keys()):
            b = kwargs["a"]*(1-kwargs["f"])
            e1 = math.sqrt(2*kwargs["f"]-kwargs["f"]**2)
            e2 = math.sqrt((kwargs["a"]**2+b**2)/b**2)
            c = kwargs["a"]/(1-kwargs["f"])
            alpha = math.atan(e2)
            return {"b": b, "e1": e1, "e2": e2, "c": c, "alpha": math.degrees(alpha)}
        elif {"a", "c"}.issubset(kwargs.keys()):
            b = (kwargs["a"]**2)/kwargs["c"]
            f = 1-b/kwargs["a"]
            e1 = math.sqrt(2*f-f**2)
            e2 = math.sqrt((kwargs["a"]**2+b**2)/b)
            alpha = math.atan(e2)
            return {"b": b, "e1": e1, "e2": e2, "f": f, "alpha": math.degrees(alpha)}
        elif {"a", "e1"}.issubset(kwargs.keys()):
            b = kwargs["a"]*math.sqrt(1-kwargs["e1"])
            e2 = math.sqrt((kwargs["a"]**2+b**2)/b**2)
            f = 1-b/kwargs["a"]
            c = kwargs["a"]/(1-f)
            alpha = math.atan(e2)
            return {"b": b, "c": c, "e2": e2, "f": f, "alpha": math.degrees(alpha)}
        elif {"a", "e2"}.issubset(kwargs.keys()):
            b = kwargs["a"]/math.sqrt(1+kwargs["e2"]**2)
            f = 1-b/kwargs["a"]
            e1 = math.sqrt(2*f-f**2)
            c = kwargs["a"]/(1-f)
            alpha = math.atan(kwargs["e2"])
            return {"b": b, "c": c, "e1": e1, "f": f, "alpha": math.degrees(alpha)}
        elif {"a", "alpha"}.issubset(kwargs.keys()):
            b = kwargs["a"]*math.cos(math.degrees(kwargs["alpha"]))
            f = 1-b/kwargs["a"]
            e1 = math.sqrt(2*f-f**2)
            c = kwargs["a"]/(1-f)
            e2 = math.sqrt((kwargs["a"]**2-b**2)/b**2)
            return {"b": b, "c": c, "e1": e1, "f": f, "e2": e2}
        elif {"f", "b"}.issubset(kwargs.keys()):
            a = kwargs["b"]/(1-kwargs["f"])
            e1 = math.sqrt(2*kwargs["f"]-kwargs["f"]**2)
            e2 = math.sqrt((a**2-kwargs["b"]**2)/kwargs["b"]**2)
            c = a/(1-kwargs["f"])
            alpha = math.atan(e2)
            return {"a": a, "e1": e1, "e2": e2, "c": c, "alpha": math.degrees(alpha)}
        elif {"c", "b"}.issubset(kwargs.keys()):
            a = math.sqrt(kwargs["c"]*kwargs["b"])
            f = 1-kwargs["b"]/a
            e1 = math.sqrt(2*f-f**2)
            e2 = math.sqrt((kwargs["a"]**2-kwargs["b"]**2)/kwargs["b"]**2)
            alpha = math.atan(e2)
            return {"a": a, "e1": e1, "e2": e2, "f": f, "alpha": math.degrees(alpha)}
        elif {"e1", "b"}.issubset(kwargs.keys()):
            a = kwargs["b"]/math.sqrt(1-kwargs["e1"])
            e2 = math.sqrt((a**2-kwargs["b"]**2)/kwargs["b"]**2)
            f = 1-kwargs["b"]/a
            c = a/(1-f)
            alpha = math.atan(e2)
            return {"a": a, "c": c, "e2": e2, "f": f, "alpha": math.degrees(alpha)}
        elif {"e2", "b"}.issubset(kwargs.keys()):
            a = kwargs["b"]*math.sqrt(1+kwargs["e2"]**2)
            f = 1-kwargs["b"]/a
            e1 = math.sqrt(2*f-f**2)
            c = kwargs["b"]/(1-f)
            alpha = math.atan(kwargs["e2"])
            return {"a": a, "c": c, "e1": e1, "f": f, "alpha": math.degrees(alpha)}
        elif {"alpha", "b"}.issubset(kwargs.keys()):
            a = kwargs["b"]/math.cos(math.degrees(kwargs["alpha"]))
            f = 1-kwargs["b"]/a
            e1 = math.sqrt(2*f-f**2)
            c = a/(1-f)
            e2 = math.sqrt((a**2-kwargs["b"]**2)/kwargs["b"]**2)
            return {"a": a, "c": c, "e1": e1, "f": f, "e2": e2}
        elif {"e1", "c"}.issubset(kwargs.keys()):
            a = kwargs["c"]*math.sqrt(1-kwargs["c"]**2)
            b = (a**2)/kwargs["c"]
            f = 1-b/a
            e2 = math.sqrt((a**2-b**2)/b**2)
            alpha = math.atan(e2)
            return {"a": a, "b": b, "alpha": math.degrees(alpha), "f": f, "e2": e2}
        elif {"e2", "c"}.issubset(kwargs.keys()):
            a = kwargs["c"]*math.sqrt(1-kwargs["c"]**2)
            b = (a**2)/kwargs["c"]
            f = 1-b/a
            e1 = math.sqrt(2*f-f**2)
            alpha = math.atan(kwargs["e2"])
            return {"a": a, "b": b, "alpha": math.degrees(alpha), "f": f, "e1": e1}
        else:
            return {"error": "unsupported params, check the discreption of the function to understand why this error appear in your screen"}
    except ValueError as err:
        return {"error": format(err)}
    except ZeroDivisionError:
        return {"error": "You've passed a <0> value to a or b or both of them which isn't possible"}
# print(ellipsoidParams(a=300,b=100))