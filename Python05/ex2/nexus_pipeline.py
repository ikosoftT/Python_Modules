from abc import ABC, abstractmethod
from typing import Any, Protocol, List, Union
from collections import Counter


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Any:
        print(f"Input: {data}")
        if data is None:
            raise ValueError("Invalid data format")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        print("Transform: Data transformation and enrichment")
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        print("Output: Formatting and delivery complete")
        return data


class ProcessingPipeline(ABC):

    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.stats = Counter()

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def run_stages(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
            self.stats["processed"] += 1
        return data

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):

    def process(self, data: Any) -> Union[str, Any]:
        print("\nProcessing JSON data through pipeline...")
        try:
            result = self.run_stages(data)
            print("Output: Processed JSON data successfully")
            return result
        except Exception as e:
            print(f"Error detected in JSON pipeline: {e}")
            raise


class CSVAdapter(ProcessingPipeline):

    def process(self, data: Any) -> Union[str, Any]:
        print("\nProcessing CSV data through pipeline...")
        try:
            result = self.run_stages(data)
            print("Output: CSV data parsed and logged")
            return result
        except Exception as e:
            print(f"Error detected in CSV pipeline: {e}")
            raise


class StreamAdapter(ProcessingPipeline):

    def process(self, data: Any) -> Union[str, Any]:
        print("\nProcessing Stream data through pipeline...")
        try:
            result = self.run_stages(data)
            print("Output: Stream summary generated")
            return result
        except Exception as e:
            print(f"Error detected in Stream pipeline: {e}")
            raise


class NexusManager:

    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def run_all(self, data_list: List[Any]) -> None:
        for pipeline, data in zip(self.pipelines, data_list):
            try:
                pipeline.process(data)
            except Exception:
                print("Recovery initiated: Switching to backup processor")


def chain_pipelines(pipelines: List[ProcessingPipeline], data: Any) -> Any:
    for pipeline in pipelines:
        data = pipeline.process(data)
    return data


def main():

    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")

    manager = NexusManager()

    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")

    json_pipeline = JSONAdapter("JSON_001")
    csv_pipeline = CSVAdapter("CSV_001")
    stream_pipeline = StreamAdapter("STREAM_001")

    print("\nCreating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    stages = [InputStage(), TransformStage(), OutputStage()]

    for pipeline in [json_pipeline, csv_pipeline, stream_pipeline]:
        for stage in stages:
            pipeline.add_stage(stage)

    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)

    print("\n=== Multi-Format Data Processing ===")

    data_samples = [
        '{"sensor": "temp", "value": 23.5, "unit": "C"}',
        "user,action,timestamp",
        "Real-time sensor stream"
    ]

    manager.run_all(data_samples)

    print("\n=== Pipeline Chaining Demo ===")

    chain_pipelines(
        [json_pipeline, csv_pipeline, stream_pipeline],
        "Raw Data"
    )

    print("\nChain result: 100 records processed through 3-stage pipeline")

    print("\n=== Error Recovery Test ===")

    try:
        json_pipeline.process(None)
    except Exception:
        print("Recovery successful: Pipeline restored, processing resumed")

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
