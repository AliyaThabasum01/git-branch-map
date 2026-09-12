from branch_map import get_branches

print("🌿 Git Branch Map")
print("=" * 35)

try:
    branches = get_branches()

    for branch, current in branches:
        marker = "👉" if current else "  "
        print(f"{marker} {branch}")

except Exception as error:
    print(f"❌ Error: {error}")
