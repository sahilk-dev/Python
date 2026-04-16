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


# Smart Even-Odd Analyzer

def smart_analyzer(integers):
    
    even_count = 0
    odd_count = 0

    even_sum = 0
    odd_sum = 0

    for num in integers:

        if not isinstance(num, int):
            return {"error": "All elements must be integers"}

        if num % 2 == 0:
            even_count += 1
            even_sum += num
        else:
            odd_count += 1
            odd_sum += num

    return {
        "even": {"count": even_count, "sum": even_sum},
        "odd": {"count": odd_count, "sum": odd_sum}
    }

integers = [2, 4, 10, 7, 9, 50, 99 ]
print(smart_analyzer(integers))