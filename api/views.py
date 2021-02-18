
from methods.rayonDeCourbur import rayonDeCourbur
from methods.calculateArc import parallelArcLength
from methods.ellipsoidParams import ellipsoidParams
from methods.latitudes import latitudes
from methods.problem import directProblem, inversProblem
from methods.transformation import cartToGeo, geoToCart
from methods.areaCalculator import CalculateArea
from django.http.response import JsonResponse
import math
# Create your views here.


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
            phi = math.radians(kwargs["phi"])
            e2 = 1-(b/a)**2
            w = math.sqrt(1-e2*math.sin(phi)**2)
            M = a*(1-e2)/w**3
            N = a/w
            if "alpha" in kwargs.keys():
                alpha = math.radians(kwargs["alpha"])
                rAlpha = (M*N)/(M*math.sin(alpha)**2+N*math.cos(alpha)**2)
                return{"M": M, "N": N, "rAlpha": rAlpha, "1/R": 1/rAlpha}
            elif kwargs["radius"] == "M":
                return {"M": M}
            elif kwargs["radius"] == "N":
                return {"N": N}
        except KeyError as err:
            return {"erreur": f"{format(err)} is required!"}


def merdianArcLength(**kwargs):
    """
    this function take 3 params
    phi1:latitude 1
    phi2: latitude 2
    ref or a&b : ellipsoid params
    this function calculate the meridian arc width
    """
    a = 0
    b = 0
    kwargs["radius"] = "M"
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
        kwargs["phi"] = kwargs["phi1"]
        M1 = rayonDeCourbur(**kwargs)["M"]
        kwargs["phi"] = kwargs["phi2"]
        M2 = rayonDeCourbur(**kwargs)["M"]
        deltaPhi = abs(kwargs["phi2"]-kwargs["phi1"])
        if 2 <= deltaPhi < 5:
            e2 = 1-(b/a)**2
            Mm = (M1+M2)/2
            phiM = (kwargs["phi1"]+kwargs["phi2"])/2
            S = ((M1+M2+4*Mm)*deltaPhi +
                 ((math.cos(math.radians(2*phiM))*deltaPhi**5)*(a*e2)/240))/6
            return {"S": S}
        elif deltaPhi < 2:
            e2 = 1-(b/a)**2
            Mm = (M1+M2)/2
            phiM = (kwargs["phi1"]+kwargs["phi2"])/2
            S = Mm*deltaPhi+(a*e2*math.cos(2*phiM)*deltaPhi**3)/3
            return {"S": S}
    except KeyError:
        return {"error": "the function required 3 basics params phi1,phi2 and ref or a&b"}


def area(req):
    try:
        data = dict(req.GET)
        for index, a in enumerate(data.keys()):
            if a == "ref":
                data[str(a)] = str(list(data.values())[index][0])
            else:
                data[str(a)] = float(list(data.values())[index][0])
        res = CalculateArea(**data)
        if "error" in res.keys():
            res.update(
                {"success": False, "message": "something wrong has happend"})
            return JsonResponse(res, status=400)
        else:
            res.update(
                {"success": True, "message": "the surface has been calculated successfully"})
            return JsonResponse(res, status=200)
    except KeyError as err:
        return JsonResponse({"error": format(err), "message": "something wrong has happend", "success": False}, status=400)
    except TypeError as err:
        return JsonResponse({"error": format(err), "message": "something wrong has happend", "success": False}, status=500)
    except ValueError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)


def transformGeoToCart(req):
    try:
        data = dict(req.GET)
        for index, a in enumerate(data.keys()):
            if a == "ref":
                data[str(a)] = str(list(data.values())[index][0])
            else:
                data[str(a)] = float(list(data.values())[index][0])
        res = geoToCart(**data)
        if "error" in res.keys():
            res.update(
                {"success": False, "message": "something wrong has happend"})
            return JsonResponse(res, status=400)
        else:
            res.update(
                {"success": True, "message": "the transformation appliqued successfully"})
            return JsonResponse(res, status=200)
    except KeyError as err:
        return JsonResponse({"error": format(err), "message": "something wrong has happend", "success": False}, status=400)
    except TypeError as err:
        return JsonResponse({"error": format(err), "message": "something wrong has happend", "success": False}, status=500)
    except ValueError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)


def tranformCartToGeo(req):
    try:
        data = dict(req.GET)
        for index, a in enumerate(data.keys()):
            if a == "ref":
                data[str(a)] = str(list(data.values())[index][0])
            else:
                data[str(a)] = float(list(data.values())[index][0])
        res = cartToGeo(**data)
        if "error" in res.keys():
            res.update(
                {"success": False, "message": "something wrong has happend"})
            return JsonResponse(res, status=400)
        else:
            res.update(
                {"success": True, "message": "the transformation appliqued successfully"})
            return JsonResponse(res, status=200)
    except KeyError as err:
        return JsonResponse({"error": format(err), "message": "something wrong has happend", "success": False}, status=500)
    except TypeError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)
    except ZeroDivisionError as err:
        return JsonResponse({"error": format(err), "message": "unexpected  0 value for z for the entry given ", "success": False}, status=500)
    except ValueError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)


def resolveDirecProblem(req):
    try:
        data = dict(req.GET)
        for index, a in enumerate(data.keys()):
            data[str(a)] = float(list(data.values())[index][0])
        res = directProblem(**data)
        if "error" in res.keys():
            res.update(
                {"success": False, "message": "something wrong has happend"})
            return JsonResponse(res, status=400)
        else:
            res.update(
                {"success": True, "message": "the direct problem was resolved successfully"})
            return JsonResponse(res, status=200)
    except KeyError as err:
        return JsonResponse({"error": format(err), "message": "something wrong has happend", "success": False}, status=500)
    except TypeError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)
    except ZeroDivisionError as err:
        return JsonResponse({"error": format(err), "message": "unexpected  0 value for the entry given ", "success": False}, status=500)
    except ValueError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)


def resolveInversProblem(req):
    try:
        data = dict(req.GET)
        for index, a in enumerate(data.keys()):
            data[str(a)] = float(list(data.values())[index][0])
        res = inversProblem(**data)
        if "error" in res.keys():
            res.update(
                {"success": False, "message": "something wrong has happend"})
            return JsonResponse(res, status=400)
        else:
            res.update(
                {"success": True, "message": "the invers problem was resolved successfully"})
            return JsonResponse(res, status=200)
    except KeyError as err:
        return JsonResponse({"error": format(err), "message": "something wrong has happend", "success": False}, status=500)
    except TypeError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)
    except ZeroDivisionError as err:
        return JsonResponse({"error": format(err), "message": "unexpected  0 value for the entry given ", "success": False}, status=500)
    except ValueError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)


def latitudesCalculator(req):
    try:
        data = dict(req.GET)
        for index, a in enumerate(data.keys()):
            if a == "ref":
                data[str(a)] = str(list(data.values())[index][0])
            else:
                data[str(a)] = float(list(data.values())[index][0])
        res = latitudes(**data)
        if "error" in res.keys():
            res.update(
                {"success": False, "message": "something wrong has happend"})
            return JsonResponse(res, status=400)
        else:
            res.update(
                {"success": True, "message": "the latitudes has been calculated successfully"})
            return JsonResponse(res, status=200)
    except KeyError as err:
        return JsonResponse({"error": format(err), "message": "something wrong has happend", "success": False}, status=500)
    except TypeError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)
    except ZeroDivisionError as err:
        return JsonResponse({"error": format(err), "message": "unexpected  0 value for z for the entry given ", "success": False}, status=500)
    except ValueError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)


def resolveEllipsoidParams(req):
    try:
        data = dict(req.GET)
        for index, a in enumerate(data.keys()):
            data[str(a)] = float(list(data.values())[index][0])
        res = ellipsoidParams(**data)
        if "error" in res.keys():
            res.update(
                {"success": False, "message": "something wrong has happend"})
            return JsonResponse(res, status=400)
        else:
            res.update(
                {"success": True, "message": "the ellipsoid prams has been calculated successfully"})
            return JsonResponse(res, status=200)
    except KeyError as err:
        return JsonResponse({"error": format(err), "message": "something wrong has happend", "success": False}, status=500)
    except TypeError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)
    except ZeroDivisionError as err:
        return JsonResponse({"error": format(err), "message": "unexpected  0 value for z for the entry given ", "success": False}, status=500)
    except ValueError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)


def calculateMeridianArc(req):
    try:
        
        data = dict(req.GET)
        for index, a in enumerate(data.keys()):
            if a == "ref":
                data[str(a)] = str(list(data.values())[index][0])
            else:
                data[str(a)] = float(list(data.values())[index][0])
        print(data)
        res = merdianArcLength(
            phi1=data["phi1"], ref=data["ref"], phi2=data["phi2"])
        print(res)
        if "error" in res.keys():
            res.update(
                {"success": False, "message": "something wrong has happend"})
            return JsonResponse(res, status=400)
        else:
            res.update(
                {"success": True, "message": "the arc length of meridian has been calculated successfully"})
            return JsonResponse(res, status=200)
    except KeyError as err:
        return JsonResponse({"error": format(err), "message": "something wrong has happend", "success": False}, status=500)
    except TypeError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)
    except ZeroDivisionError as err:
        return JsonResponse({"error": format(err), "message": "unexpected  0 value for z for the entry given ", "success": False}, status=500)
    except ValueError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)


def calculateParallelArc(req):
    try:
        data = dict(req.GET)
        for index, a in enumerate(data.keys()):
            if a == "ref":
                data[str(a)] = str(list(data.values())[index][0])
            else:
                data[str(a)] = float(list(data.values())[index][0])
        res = parallelArcLength(**data)
        if "error" in res.keys():
            res.update(
                {"success": False, "message": "something wrong has happend"})
            return JsonResponse(res, status=500)
        else:
            res.update(
                {"success": True, "message": "the arc length of parallel has been calculated successfully"})
            return JsonResponse(res, status=200)
    except KeyError as err:
        return JsonResponse({"error": format(err), "message": "something wrong has happend", "success": False}, status=500)
    except TypeError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)
    except ZeroDivisionError as err:
        return JsonResponse({"error": format(err), "message": "unexpected  0 value for z for the entry given ", "success": False}, status=500)
    except ValueError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)


def curvatureRadius(req):
    try:
        data = dict(req.GET)
        for index, a in enumerate(data.keys()):
            if a == "ref" or a == "radius":
                data[str(a)] = str(list(data.values())[index][0])
            else:
                data[str(a)] = float(list(data.values())[index][0])
        res = rayonDeCourbur(**data)
        if "error" in res.keys():
            res.update(
                {"success": False, "message": "something wrong has happend"})
            return JsonResponse(res, status=500)
        else:
            res.update(
                {"success": True, "message": "the curvature radius has been calculated successfully"})
            return JsonResponse(res, status=200)
    except KeyError as err:
        return JsonResponse({"error": format(err), "message": "something wrong has happend", "success": False}, status=500)
    except TypeError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)
    except ZeroDivisionError as err:
        return JsonResponse({"error": format(err), "message": "unexpected  0 value for z for the entry given ", "success": False}, status=500)
    except ValueError as err:
        return JsonResponse({"error": format(err), "message": "missed required params for this method", "success": False}, status=400)
