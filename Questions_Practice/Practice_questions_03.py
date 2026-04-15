# The Grade Analyzer

def analyze_scores(scores):
    if not scores:
        return {
            "average": 0,
            "highest": None,
            "lowest": None,
            "passed": 0,
            "failed": 0,
            "grades": {"A": 0, "B": 0, "C": 0, "D": 0}
        }
    
    total = 0
    min_score = float('inf')
    max_score = float('-inf')

    passed = 0
    failed = 0

    grades = {"A": 0, "B": 0, "C": 0, "D": 0}

    for score in scores:
        total += score

        if score < min_score:
            min_score = score
        if score > max_score:
            max_score = score

        if score >= 60:
            passed += 1
        else:
            failed += 1
        
        if score >= 90:
            grades["A"] += 1
        elif score >= 75:
            grades["B"] += 1
        elif score >= 60:
            grades["C"] += 1
        else:
            grades["D"] += 1

    average = round(total / len(scores), 2)

    return {
        "average": average,
        "highest": max_score,
        "lowest": min_score,
        "passed": passed,
        "failed": failed,
        "grades": grades
    }

scores = [95, 82, 67, 45, 74, 88, 91]
print(analyze_scores(scores))       