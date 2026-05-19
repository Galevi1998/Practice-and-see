

def is_valid_shallow_json(s: str) -> bool:
    lst = s.split(',')
    for i in range (len(lst)):
        helper=  lst[i].split(":")
        if(len(helper)!=2):
            return False
        for j in helper : 
        
    return True


def main():
    test_cases = [
        ('{}', True),
        ('{"a": "b"}', True),
        ('{"a": "b", "c": "d"}', True),
        ('{"a": 123, "b": null}', True),
        ('{"a": "1", "b": 2, "c": null}', True),
        ('{"a": "b",}', False),                    # trailing comma
        ('{"a":}', False),                         # missing value
        ('{"a": "b", "c"}', False),                # missing value
        ('{"a" "b"}', False),                      # missing colon
        ('{a: "b"}', False),                       # key not quoted
        ('{"a": b}', False),                       # value not quoted or a number or null
        ('{"a": "b", "c": 1.5}', False),           # invalid number format (float not supported here)
        ('{"a": "b" "c": "d"}', False),            # missing comma between pairs
        ('{"a": "b", "c": "d", "e": "f"}', True),
        ('{"key": null}', True),
        ('{"a": "b", "c": null, "d": 0}', True),
        ('{"x": 10, "y": 20, "z": "text"}', True),
        ('{"x": 10, "y": 20, "z": "text"', False), # missing closing brace
        ('"not even json"', False),                # no braces at all
        ('{ }', True),                             # empty with space
    ]

    print("🔍 Running Tests for is_valid_shallow_json:")
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = is_valid_shallow_json(input_str)
        status = "✅" if result == expected else "❌"
        print(f"Test {i:>2}: {status} | Input: {input_str} | Expected: {expected} | Got: {result}")


if __name__ == "__main__":
    main()
