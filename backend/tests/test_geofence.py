from app.modules.attendance.geofence import is_within_office_geofence

def test_attendance_geofence_validation():
    # Office HQ at (12.9716, 77.5946)
    res_in = is_within_office_geofence(12.9717, 77.5947, 12.9716, 77.5946, max_radius_meters=100.0)
    assert res_in["allowed"] is True
    
    res_out = is_within_office_geofence(12.9800, 77.6000, 12.9716, 77.5946, max_radius_meters=100.0)
    assert res_out["allowed"] is False
