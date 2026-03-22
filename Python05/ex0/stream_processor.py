from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, res: str) -> str:
        return f"Output: {res}"


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, list) and all(isinstance(x, (int, float))
                                           for x in data)
        )

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric value!")
            print("Validation: Numeric data verified")
            total = sum(data)
            avg = total / len(data)
            res = f"Processed {len(data)} numeric values," \
                f"sum={total}, avg={avg:.1f}"
            return self.format_output(res)
        except Exception as e:
            print(f"ERROR: {e}")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        print(f"Processing data: \"{data}\"")
        try:
            if not self.validate(data):
                raise ValueError("Invalid text value!")
            print("Validation: Text data verified")
            lettres = len(data)
            count = len(data.split())
            res = f"Processed text: {lettres} characters, {count} words"
            return self.format_output(res)
        except Exception as e:
            print(f"ERROR: {e}")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return (isinstance(data, str) and data)

    def process(self, data: Any) -> str:
        print(f"Processing data: \"{data}\"")
        try:
            if not self.validate(data):
                raise ValueError("Invalid log data!")
            content = data.split(":")
            if content[0] == "ERROR":
                err = content[0]
                msg = content[1]
                res = f"[ALERT] {err} level detected:{msg}"
            elif "INFO" in content[0]:
                info = content[0]
                msg = content[1]
                res = f"[INFO] {info}:{msg}"
            else:
                raise ValueError(
                    "Please enter in valid format ERR:msg or INFO")
            print("Validation: Log entry verified")
            return self.format_output(res)
        except Exception as e:
            print(f"ERROR: {e}")


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ==\n")
    all_data: list[Any] = [[1, 2, 3, 4, 5],
                           "Hello Nexus World", "ERROR: Connection timeout"]
    test_data: list[Any] = [[1, 2, 3], "Hello 1337",
                            "INFO evel detected: System ready"]

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Initializing Numeric Processor...")

    Processed = numeric.process(all_data[0])

    print(Processed)

    print("\nInitializing Text Processor...")

    Processed = text.process(all_data[1])

    print(Processed)

    print("\nInitializing Log Processor...")

    Processed = log.process(all_data[2])

    print(Processed)

    print("\n=== Polymorphic Processing Demo ===")

    processors = [
        numeric,
        text,
        log
    ]
    for p, d in zip(processors, test_data):
        r = p.process(d)
        print(r, end="\n\n")


if __name__ == "__main__":
    main()
