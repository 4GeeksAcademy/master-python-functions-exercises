"""Validate every exercise in this LearnPack.

For each folder in exercises/ (except the welcome step) this script checks that:
  1. README.md and README.es.md exist.
  2. app.py, solution.hide.py and test.py exist.
  3. The tests PASS when app.py is replaced by solution.hide.py (positive case).
  4. The tests FAIL with the untouched starter app.py (negative case).

Usage:
    pip install pytest==6.2.5 pytest-testdox mock
    python scripts/validate_exercises.py [exercise-folder-name ...]
"""
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXERCISES = os.path.join(ROOT, "exercises")
REQUIRED = ["README.md", "README.es.md", "app.py", "solution.hide.py", "test.py"]


def run_tests(folder, use_solution):
    with tempfile.TemporaryDirectory() as tmp:
        target = os.path.join(tmp, "exercise")
        shutil.copytree(folder, target)
        if use_solution:
            shutil.copy(os.path.join(target, "solution.hide.py"), os.path.join(target, "app.py"))
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "test.py"],
            cwd=target,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.returncode == 0, result.stdout + result.stderr


def main(selected):
    problems = []
    names = sorted(n for n in os.listdir(EXERCISES) if os.path.isdir(os.path.join(EXERCISES, n)))
    for name in names:
        if selected and name not in selected:
            continue
        folder = os.path.join(EXERCISES, name)
        if name.startswith("000"):
            missing = [f for f in ["README.md", "README.es.md"] if not os.path.exists(os.path.join(folder, f))]
            if missing:
                problems.append(f"{name}: missing {', '.join(missing)}")
            continue
        missing = [f for f in REQUIRED if not os.path.exists(os.path.join(folder, f))]
        if missing:
            problems.append(f"{name}: missing {', '.join(missing)}")
            continue
        ok_solution, out_solution = run_tests(folder, use_solution=True)
        ok_starter, _ = run_tests(folder, use_solution=False)
        status = "ok"
        if not ok_solution:
            status = "SOLUTION FAILS"
            problems.append(f"{name}: solution.hide.py does not pass the tests\n{out_solution[-1500:]}")
        if ok_starter:
            status = "STARTER PASSES"
            problems.append(f"{name}: the starter app.py already passes the tests")
        print(f"{status:>15}  {name}")
    print()
    if problems:
        print("\n\n".join(problems))
        print(f"\n{len(problems)} problem(s) found.")
        return 1
    print("All exercises are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
