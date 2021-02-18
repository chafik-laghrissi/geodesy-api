from api.views import area, calculateMeridianArc, calculateParallelArc, curvatureRadius, latitudesCalculator, resolveDirecProblem, resolveEllipsoidParams, resolveInversProblem, tranformCartToGeo, transformGeoToCart
from django.http.response import JsonResponse
from django.urls import path
urlpatterns = [path("area", area),
               path("geo-to-cart", transformGeoToCart),
               path("cart-to-geo", tranformCartToGeo),
               path("inverse-problem", resolveInversProblem),
               path("direct-problem", resolveDirecProblem),
               path("latitudes", latitudesCalculator),
               path("ellipsoid-params", resolveEllipsoidParams),
               path("meridian-arc", calculateMeridianArc),
               path("parallel-arc", calculateParallelArc),
               path("curvature-radius", curvatureRadius)]
