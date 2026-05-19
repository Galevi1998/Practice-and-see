


def is_json_curly_balanced(s: str) -> bool:
    count=0
    for i in s :
        if i=='{':
            count+=1
        elif i == '}':
            count-=1
    return count==0


def main():
    test_cases = [
        ('{"name": "Gal", "age": 30}', True),
        ('{"data": {"a": 1, "b": 2}}', True),
        ('{"a": 1, "b": {"c": 2, "d": {"e": 3}}', False),  # missing closing brace
        ('{}}', False),  # extra closing
        ('{{}}', True),
        ('{}{}{}', True),
        ('{', False),
        ('}', False),
        ('"{"', False),  # braces inside a string
        ('Just a normal sentence with no JSON at all.', True)
    ]

    print("🔍 Running Tests for is_json_curly_balanced:")
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = is_json_curly_balanced(input_str)
        print(f"Test {i}: {'✅' if result == expected else '❌'} | Input: {input_str} | Expected: {expected} | Got: {result}")


if __name__ == "__main__":
    main()
