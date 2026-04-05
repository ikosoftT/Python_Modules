#!/usr/bin/env python3

import sys
import importlib
from types import ModuleType
from typing import Dict, List, Tuple, Optional

REQUIRED_PACKAGES = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computations",
    "matplotlib": "Visualization",
    "requests": "Network access (optional)"
}


def check_dependencies() -> Tuple[Dict[str, ModuleType], List[str]]:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    installed: Dict[str, ModuleType] = {}
    missing: List[str] = []

    for pkg, desc in REQUIRED_PACKAGES.items():
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {pkg} ({version}) - {desc} ready")
            installed[pkg] = module
        except Exception:
            print(f"[MISSING] {pkg} - {desc}")
            missing.append(pkg)

    if missing:
        print("\nDependency installation options:")
        print("-> Using pip:")
        print("   pip install -r requirements.txt")
        print("-> Using Poetry:")
        print("   poetry install")

    return installed, missing


def fetch_data(req: ModuleType) -> Optional[List[float]]:
    print("Fetching real data using requests...")

    try:
        res = req.get(
            "https://fakerapi.it/api/v1/persons?_quantity=5", timeout=5)
        data = res.json()

        persons = data.get("data", [])
        emails = [p.get("email", "") for p in persons]

        values: List[float] = [float(len(email)) for email in emails if email]

        if not values:
            return None

        print(f"Fetched {len(values)} data points from API")
        return values

    except Exception:
        print("API fetch failed")
        return None


def generate_fallback_data(np: ModuleType) -> List[float]:
    print("Generating Matrix data...")
    return np.random.randn(1000).tolist()


def analyze_data(
    pd: ModuleType,
    np: ModuleType,
    plt: ModuleType,
    data: List[float]
) -> None:
    print("Analyzing Matrix data...")
    print(f"Processing {len(data)} data points...")

    df = pd.DataFrame({
        "signal": data,
        "time": range(len(data))
    })

    window_size: int = min(10, len(data))
    df["smoothed"] = df["signal"].rolling(window=window_size).mean()

    print("Generating visualization...")

    plt.figure()
    plt.plot(df["time"], df["signal"], label="Raw Signal")
    plt.plot(df["time"], df["smoothed"], label="Smoothed Signal")
    plt.legend()
    plt.title("Matrix Signal Analysis")
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved")


def show_environment() -> None:
    import os

    if os.environ.get("POETRY_ACTIVATE"):
        print("Environment: poetry")
    else:
        print("Environment : pip/system")


def main() -> None:
    installed, missing = check_dependencies()

    core_missing = [
        pkg for pkg in ["pandas", "numpy", "matplotlib"] if pkg in missing
    ]

    if core_missing:
        sys.exit(1)

    pd = installed["pandas"]
    np = installed["numpy"]
    plt = importlib.import_module("matplotlib.pyplot")

    data = None

    if "requests" in installed:
        data = fetch_data(installed["requests"])

    if data is None:
        data = generate_fallback_data(np)

    analyze_data(pd, np, plt, data)
    show_environment()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
