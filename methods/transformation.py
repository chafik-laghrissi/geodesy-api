import math


def cartToGeo(x, y, z, ref):

    a = 0
    f = 0
    if ref == "local":
        a = 6378249.145
        f = 1/293.4663
    elif ref == "global":
        a = 6378137
        f = 1/298.257223563
    if a != 0 and f != 0:
        e2 = 1-(1-f)**2
        lon = math.degrees(math.atan(y/x))
        lat0 = math.atan((z/(math.sqrt(x**2+y**2)))*(1+(e2)/(1-e2)))
        N0 = a/math.sqrt(1-e2*(math.sin(lat0)**2))
        lat1 = math.atan((z/(math.sqrt(x**2+y**2)))*(1+N0*e2*math.sin(lat0)/z))
        N1 = a/math.sqrt(1-e2*(math.sin(lat1)**2))
        while abs(N0-N1) > 1e-5:
            N0 = N1
            lat0 = lat1
            lat1 = math.atan((z/(math.sqrt(x**2+y**2)))
                             * (1+N0*e2*math.sin(lat0)/z))
            N1 = a/math.sqrt(1-e2*(math.sin(lat1)**2))

        alt = (z/math.sin(lat1))-N1*(1-e2)

        return{"lon": lon, "lat": math.degrees(lat1), "alt": alt}
    else:
        return {"error": "ref not defined as expected"}


def geoToCart(lon, lat, alt, ref):
    a = 0
    f = 0
    if ref == "local":
        a = 6378249.145
        f = 1/293.4663
    elif ref == "global":
        a = 6378137
        f = 1/298.257223563
    if a != 0 and f != 0:
        e2 = 1-(1-f)**2
        W = math.sqrt(1-e2*math.pow(math.sin(math.radians(lat)), 2))
        N = a/W
        x = (N+alt)*math.cos(math.radians(lat))*math.cos(math.radians(lon))
        y = (N+alt)*math.cos(math.radians(lat))*math.sin(math.radians(lon))
        z = (N*(1-e2)+alt)*math.sin(math.radians(lat))
        return{"x": x, "y": y, "z": z}
    else:
        return {"error": "ref not defined as expected"}


# test = geoToCart(-7.5575, 33.4463, 243.419, "local")
# print(cartToGeo(test["x"], test["y"], test["z"], "local"))
# print(test)
