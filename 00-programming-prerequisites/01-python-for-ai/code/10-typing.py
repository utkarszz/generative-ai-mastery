
def analyze_scores(marks: list[int]) -> dict[str, float | int | bool]:
    average: float = sum(marks) / len(marks)
    highest: int = max(marks)
    passed: bool = average >= 40

    return {
        "average": average,
        "highest": highest,
        "passed": passed
    }


result = analyze_scores([80, 90, 70, 60])

print(result)
