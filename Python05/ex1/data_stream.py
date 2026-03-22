from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.id = stream_id
        self.stream_type = stream_type
        self.process_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int]]:
        return {
            "stream_id": self.id,
            "processed_count": self.process_count
        }


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[str]) -> str:
        try:
            temps = [
                float(item.split(":")[1])
                for item in data_batch
                if item.startswith("temp")
            ]
            self.process_count += len(data_batch)

            avg = sum(temps) / len(temps) if temps else 0

            return f"Sensor analysis: {len(data_batch)}"\
                f" readings processed, avg temp: {avg}°C"
        except Exception as e:
            return f"SensorStream Err: {e}"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            buys = [
                int(item.split(":")[1])
                for item in data_batch
                if isinstance(item, str) and item.startswith("buy")
            ]

            sells = [
                int(item.split(":")[1])
                for item in data_batch
                if isinstance(item, str) and item.startswith("sell")
            ]
            self.process_count += len(data_batch)
            net_flow = sum(buys) - sum(sells)
            return f"Transaction analysis: {len(data_batch)} operations,"\
                f" net flow: +{net_flow} units"
        except Exception as e:
            return f"TransactionStream Err: {e}"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        errs = [e for e in data_batch if isinstance(
            e, str) and "error" in e.lower()]

        self.process_count += len(data_batch)

        return f"Event analysis: {len(data_batch)} events," \
            f" {len(errs)} error detected"


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if not (isinstance(stream, DataStream) and not None):
            raise TypeError("StreamProcessor: Cannot Add None!")
        self.streams.append(stream)

    def process_streams(self, batches: List[List[Any]]) -> None:
        print(
            "Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")
        for stream, batch in zip(self.streams, batches):
            try:
                stream.process_batch(batch)
            except Exception:
                print("ERR: Processing Failed")
            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {len(batch)} readings processed")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {len(batch)} operations processed")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {len(batch)} events processed")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    trans_batch = ["buy:100", "sell:150", "buy:75"]
    event_batch = ["login", "error", "logout"]

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.id}, Type: {sensor.stream_type}")
    print(f"Processing sensor batch: {sensor_batch}")
    print(sensor.process_batch(sensor_batch))

    print("\nInitializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.id}, Type: {trans.stream_type}")
    print(f"Processing transaction batch: {trans_batch}")
    print(trans.process_batch(trans_batch))

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.id}, Type: {event.stream_type}")
    print(f"Processing event batch: {event_batch}")
    print(event.process_batch(event_batch))

    print("\n=== Polymorphic Stream Processing ===")

    streams_obs = [sensor, trans, event]

    processor = StreamProcessor()
    for s in streams_obs:
        processor.add_stream(s)

    processor.process_streams([
        ["temp:21.5", "temp:23.1"],
        ["buy:50", "sell:70", "sell:40", "buy:20"],
        ["login", "error", "logout"]])

    print("\nStream filtering active: High-priority data only")
    f_sens = sensor.filter_data(
        ["alert:temp_high", "temp:22", "alert:humidity"], "alert")
    f_tran = trans.filter_data(["buy:200", "sell:50", "buy:500"], "500")

    print(
        f"Filtered results: {len(f_sens)}",
        f" critical sensor alerts, {len(f_tran)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Outer Error: {e}")
