from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from enum import Enum
from typing import List


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMemeber(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMemeber] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not any(
            m.rank in (Rank.captain, Rank.commander)
            for m in self.crew
        ):
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            exp = sum(1 for m in self.crew if m.years_experience >= 5)
            tot = len(self.crew)
            if exp <= tot * 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need 50% "
                    "experienced crew (5+ years)")
            if not all(self.crew):
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("="*40)

    try:
        crew_mem = [
            {
                "member_id": "M202_MARS",
                "name": "Sarah Connor",
                "rank": Rank.commander,
                "age": 50,
                "specialization": "Mission Command",
                "years_experience": 6,
                "is_active": True
            },
            {
                "member_id": "M102_MARS",
                "name": "John Smith",
                "rank": Rank.lieutenant,
                "age": 22,
                "specialization": "Navigation",
                "years_experience": 12,
                "is_active": True,
            },
            {
                "member_id": "M202_MARS",
                "name": "Alice Johnson",
                "rank": Rank.officer,
                "age": 63,
                "specialization": "Engineering",
                "years_experience": 10,
                "is_active": True
            }
        ]
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-04-02 03:05:22",
            duration_days=900,
            crew=crew_mem,
            budget_millions=2500.0
        )
        print("valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew Members:")
        for m in mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")
        print()
    except Exception as e:
        print("Err:", e)
    print("="*40)
    try:
        crew_mem = [
            {
                "member_id": "M202_MARS",
                "name": "Sarah Connor",
                "rank": Rank.cadet,
                "age": 50,
                "specialization": "Mission Command",
                "years_experience": 6,
                "is_active": True
            },
            {
                "member_id": "M102_MARS",
                "name": "John Smith",
                "rank": Rank.cadet,
                "age": 22,
                "specialization": "Navigation",
                "years_experience": 12,
                "is_active": True,
            },
            {
                "member_id": "M202_MARS",
                "name": "Alice Johnson",
                "rank": Rank.cadet,
                "age": 63,
                "specialization": "Engineering",
                "years_experience": 10,
                "is_active": True
            }
        ]
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2026-04-02 03:05:22",
            duration_days=900,
            crew=crew_mem,
            budget_millions=2500.0
        )
    except Exception as e:
        print("Expected validation errors:")
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
