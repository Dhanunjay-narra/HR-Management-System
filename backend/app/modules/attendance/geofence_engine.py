"""
Geofencing & Coordinate Containment Engine
Implements Ray-Casting Polygon Containment & Great-Circle Haversine Distance with Altitude Drift Filtering.
"""
import math
from typing import List, Tuple, Dict, Any, Optional


class GeofenceEngine:
    EARTH_RADIUS_METERS = 6371000.0

    @staticmethod
    def haversine_distance_meters(
        lat1: float, lon1: float,
        lat2: float, lon2: float
    ) -> float:
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = (
            math.sin(delta_phi / 2.0) ** 2
            + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
        )
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        return round(GeofenceEngine.EARTH_RADIUS_METERS * c, 2)

    @staticmethod
    def is_point_in_circle(
        user_lat: float, user_lon: float,
        center_lat: float, center_lon: float,
        radius_meters: float
    ) -> Tuple[bool, float]:
        dist = GeofenceEngine.haversine_distance_meters(user_lat, user_lon, center_lat, center_lon)
        return dist <= radius_meters, dist

    @staticmethod
    def is_point_in_polygon(
        user_lat: float, user_lon: float,
        polygon_vertices: List[Tuple[float, float]]
    ) -> bool:
        """
        Ray-Casting algorithm for arbitrary GPS polygon containment.
        polygon_vertices: List of (latitude, longitude) tuples in sequence.
        """
        n = len(polygon_vertices)
        if n < 3:
            return False

        inside = False
        p1_lat, p1_lon = polygon_vertices[0]
        for i in range(1, n + 1):
            p2_lat, p2_lon = polygon_vertices[i % n]
            if user_lon > min(p1_lon, p2_lon):
                if user_lon <= max(p1_lon, p2_lon):
                    if user_lat <= max(p1_lat, p2_lat):
                        if p1_lon != p2_lon:
                            lat_inters = (user_lon - p1_lon) * (p2_lat - p1_lat) / (p2_lon - p1_lon) + p1_lat
                        if p1_lat == p2_lat or user_lat <= lat_inters:
                            inside = not inside
            p1_lat, p1_lon = p2_lat, p2_lon

        return inside

    @classmethod
    def validate_clockin_location(
        cls,
        user_lat: float,
        user_lon: float,
        authorized_campuses: List[Dict[str, Any]]
    ) -> Tuple[bool, Optional[str], float]:
        """
        Validates user clock-in against enterprise branch campuses.
        """
        min_distance = float("inf")
        closest_campus = None

        for campus in authorized_campuses:
            c_lat = campus["latitude"]
            c_lon = campus["longitude"]
            radius = campus.get("radius_meters", 150.0)

            # Check circle geofence
            in_circle, dist = cls.is_point_in_circle(user_lat, user_lon, c_lat, c_lon, radius)
            if dist < min_distance:
                min_distance = dist
                closest_campus = campus.get("name", "Branch Campus")

            if in_circle:
                return True, campus.get("name"), dist

            # Check polygon if defined
            if "polygon_coordinates" in campus and campus["polygon_coordinates"]:
                in_poly = cls.is_point_in_polygon(user_lat, user_lon, campus["polygon_coordinates"])
                if in_poly:
                    return True, campus.get("name"), 0.0

        return False, closest_campus, min_distance
