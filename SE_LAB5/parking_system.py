"""Manage campus parking permits and check vehicles against parking zones."""

import json
import secrets
from datetime import datetime, timedelta

permits = {}
ZONES = ["A", "B", "C"]


def register_permit(vehicle_plate, zone_id, zone_records=None):
    """Register a vehicle for a zone and return its permit number."""
    if zone_records is None:
        zone_records = []
    try:
        permit_no = "P" + str(secrets.randbelow(90000) + 10000)
        expiry = datetime.now() + timedelta(days=180)
        permits[vehicle_plate] = {
            "zone": zone_id,
            "permit": permit_no,
            "expiry": expiry.strftime("%Y-%m-%d"),
        }
        zone_records.append((vehicle_plate, zone_id))
        return permit_no
    except (TypeError, ValueError):
        return None


def revoke_permit(vehicle_plate):
    """Remove a vehicle's permit if one exists."""
    try:
        del permits[vehicle_plate]
    except KeyError:
        pass


def is_expired(vehicle_plate):
    """Return whether a vehicle's permit has expired."""
    try:
        expiry = datetime.strptime(
            permits[vehicle_plate]["expiry"], "%Y-%m-%d"
        )
        return expiry < datetime.now()
    except (KeyError, TypeError, ValueError):
        return False


def scan_zone(zone_id, plates_seen):
    """Return plates that are unauthorized or expired in the given zone."""
    flagged = []
    for p in plates_seen:
        if p not in permits or permits[p]["zone"] != zone_id or is_expired(p):
            flagged.append(p)
    return flagged


def load_permit_database(file="permits.json"):
    """Load permit data from a JSON file or start empty."""
    try:
        with open(file, "r", encoding="utf-8") as database_file:
            loaded_permits = json.load(database_file)
    except FileNotFoundError:
        permits.clear()
        return
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid permit database: {file}") from error

    if not isinstance(loaded_permits, dict):
        raise ValueError(
            f"Permit database must contain a JSON object: {file}"
        )
    permits.clear()
    permits.update(loaded_permits)


def save_permit_database(file="permits.json"):
    """Save all current permits to a JSON file."""
    with open(file, "w", encoding="utf-8") as database_file:
        json.dump(permits, database_file)


def set_expiry(vehicle_plate, date_text):
    """Set a vehicle's permit expiry date using YYYY-MM-DD format."""
    permits[vehicle_plate]["expiry"] = date_text


def main():
    """Run a short permit-management example."""
    load_permit_database()
    register_permit("KA01AB1234", "A")
    register_permit("KA05XY9999", "Z")
    register_permit("", "B")
    register_permit(None, "C")
    set_expiry("KA01AB1234", "2020-01-01")
    revoke_permit("MH12ZZ0000")
    print(
        "Flagged in zone A:",
        scan_zone("A", ["KA01AB1234", "KA05XY9999", "TN09QQ1111"]),
    )
    plate = input("Plate to revoke (Enter to skip): ")
    if plate:
        revoke_permit(plate)
    save_permit_database()
    print("Permits on file:", len(permits))


if __name__ == "__main__":
    main()
