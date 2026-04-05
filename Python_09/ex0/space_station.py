from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.00, le=100.0)
    oxygen_level: float = Field(ge=0.00, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(min_length=1, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("="*40)
    try:
        print("valid station created:")
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=8,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-01-01T00:00:00",
            is_operational=True,
            notes="Nice Station By the way"
        )
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print("Status:", end='')
        if station.is_operational:
            print("Operational")
        else:
            print("Offline")

    except Exception as e:
        print("Error:", e)
    try:
        print("="*40)
        print("Expected validation error:")
        SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=80,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-01-01T00:00:00",
            is_operational=True,
            notes="Nice Station By the way"
        )
    except Exception as e:
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
