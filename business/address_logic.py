from db.models import Address
from geopy.distance import geodesic
from core.logging_config import logger

def add_address(db, address_data):
    try:
        data = Address(
            address=address_data.address,
            lat=address_data.lat,
            lon=address_data.lon
        )

        db.add(data)
        db.commit()
        db.refresh(data)

        logger.info(f"Address created successfully | id={data.id}")

        return data

    except Exception as e:
        logger.error(f"Error creating address | {str(e)}")
        db.rollback()
        raise


def update_address(db, address_id, address_data):
    try:
        address = db.query(Address).filter(Address.id == address_id).first()

        if not address:
            logger.warning(f"Update failed | Address {address_id} not found")
            return None

        address.address = address_data.address
        address.lat = address_data.lat
        address.lon = address_data.lon

        db.commit()
        db.refresh(address)

        logger.info(f"Address updated | id={address_id}")

        return address

    except Exception as e:
        logger.error(f"Error updating address {address_id} | {str(e)}")
        db.rollback()
        raise


def get_addresses(db):
    try:
        details = db.query(Address).all()
        logger.info(f"Fetched all addresses | count={len(details)}")
        return details

    except Exception as e:
        logger.error(f"Error fetching addresses | {str(e)}")
        raise


def delete_address(db, address_id):
    try:
        details = db.query(Address).filter(Address.id == address_id).first()

        if not details:
            logger.warning(f"Delete failed | Address {address_id} not found")
            return None

        db.delete(details)
        db.commit()

        logger.info(f"Address deleted | id={address_id}")

        return True

    except Exception as e:
        logger.error(f"Error deleting address {address_id} | {str(e)}")
        db.rollback()
        raise


def get_nearby_addresses(db, lat, lon, distance_km):
    try:
        logger.info(f"Nearby search started | lat={lat} lon={lon} radius={distance_km}km")

        addresses = db.query(Address).all()

        result = []

        for addr in addresses:
            dist = geodesic((lat, lon), (addr.lat, addr.lon)).km

            if dist <= distance_km:
                result.append(addr)

        logger.info(f"Nearby search completed | results={len(result)}")

        return result

    except Exception as e:
        logger.error(f"Error in nearby search | {str(e)}")
        raise