from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(min_length=3, max_length=500)
    is_verified: bool = True

    @model_validator(mode='after')
    def validate(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact_id must start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical Contact must be verified.")
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should"
                "include received messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("="*40)
    try:
        print("Valid contact report:")
        al = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-04-02T03:05:00",
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=7.1,
            duration_minutes=30,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        print(f"ID: {al.contact_id}")
        print(f"Type: {al.contact_type.value}")
        print(f"Location: {al.location}")
        print(f"Signal: {al.signal_strength}/10")
        print(f"Duration: {al.duration_minutes} minutes")
        print(f"Witnesses: {al.witness_count}")
        print(f"Message: '{al.message_received}'\n")
    except Exception as e:
        print("Err:", e)

    print("="*40)
    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp="2026-04-02T03:05:00",
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=80,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
    except Exception as e:
        print("Expected validation error:")
        for err in e.errors():
            print(err['msg'])


if __name__ == "__main__":
    main()
