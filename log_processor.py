logs = [
    "INFO User login",
    "ERROR Database failed",
    "INFO Request completed",
    "ERROR Timeout",
    "INFO Logout"
]

errors = []

for log in logs:
    if "ERROR" in log:
        errors.append(log)

print("Found errors:")

for error in errors:
    print(error)