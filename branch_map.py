import subprocess


def get_branches():
    result = subprocess.run(
        ["git", "branch", "--format=%(HEAD)|%(refname:short)"],
        capture_output=True,
        text=True,
        check=True
    )

    branches = []

    for line in result.stdout.splitlines():
        current, name = line.split("|", 1)
        branches.append((name, current == "*"))

    return branches
