import math

def is_within_office_geofence(user_lat: float, user_lon: float, office_lat: float, office_lon: float, max_radius_meters: float = 150.0) -> dict:
    R = 6371000  # Radius of earth in meters
    phi1 = math.radians(user_lat)
    phi2 = math.radians(office_lat)
    delta_phi = math.radians(office_lat - user_lat)
    delta_lambda = math.radians(office_lon - user_lon)
    
    a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = round(R * c, 2)
    
    allowed = distance <= max_radius_meters
    return {"allowed": allowed, "distance_meters": distance, "max_radius_meters": max_radius_meters}
