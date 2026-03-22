#!/usr/bin/env python3

import importlib


REQUIRED_PACKAGES = ["pandas", "numpy", "matplotlib", "requests"]


def check_package(name: str):
    """Check if a package is installed."""
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - Ready")
        return module
    except ImportError:
        print(f"[MISSING] {name} - not installed")
        return None


def run_analysis(pd, np, plt):
    """Run fake data analysis."""
    print("\nAnalyzing Matrix data...")

    data = np.random.normal(50, 10, 1000)
    df = pd.DataFrame({"signal": data})

    print(f"Processing {len(df)} data points...")

    plt.hist(df["signal"], bins=30)
    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal")
    plt.ylabel("Frequency")

    plt.savefig("matrix_analysis.png")

    print("Generating visualization...")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:\n")

    modules = {}

    for pkg in REQUIRED_PACKAGES:
        modules[pkg] = check_package(pkg)

    if None in modules.values():
        print("\nSome dependencies are missing.")
        print("Install them using:")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        return

    import matplotlib.pyplot as plt

    run_analysis(
        modules["pandas"],
        modules["numpy"],
        plt
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")