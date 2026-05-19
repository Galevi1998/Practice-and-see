import json

class Solution:
    def serialize_object(self, obj: dict) -> str:
        return json.dumps(obj,indent=2)


    def deserialize_json(self, json_str: str) -> dict:
        return(json.loads(json_str))
        # TODO: Implement
        pass

    def deep_equal(self, json1, json2) -> bool:
        return json1==json2
        # TODO: Implement
        pass

    # def flatten_json(self, nested_json: dict) -> dict:

    #     # TODO: Implement
    #     pass
    def merge_json_objects(self, json1: dict, json2: dict) -> dict:
        merged = dict(json1)  # Shallow copy
        stack = [(merged, json2)]  # Stack of (target_dict, source_dict) pairs

        while stack:
            target, source = stack.pop()

            for key in source:
                if key in target and isinstance(target[key], dict) and isinstance(source[key], dict):
                    # Dive deeper into both sub-dicts
                    stack.append((target[key], source[key]))
                else:
                    # Overwrite or insert
                    target[key] = source[key]

        return merged
    
    # def merge_json_objects(self, json1: dict, json2: dict) -> dict:
    #     for json in json1:
    #         if(json2.get(json)):
    #             json2
    #     # TODO: Implement

    #     pass


def main():
    sol = Solution()

    print("🔹 1. Serialize Object")
    obj = {"name": "Alice", "age": 30}
    result = sol.serialize_object(obj)
    print("Result:", result)

    print("\n🔹 2. Deserialize JSON")
    json_str = '{"name": "Alice", "age": 30}'
    result = sol.deserialize_json(json_str)
    print("Result:", result)

    print("\n🔹 3. Deep Equal JSON")
    a = {"a": [1, 2], "b": {"x": 5}}
    b = {"b": {"x": 5}, "a": [3, 2]}
    result = sol.deep_equal(a, b)
    print("Are deeply equal?", result)

    # print("\n🔹 4. Flatten JSON")
    # nested = {"a": {"b": 1, "c": {"d": 2}}, "e": 3}
    # result = sol.flatten_json(nested)
    # print("Flattened:", result)

    print("\n🔹 5. Merge JSON Objects")
    j1 = {"a": {"x": 1}, "b": 2}
    j2 = {"a": {"y": 3}, "c": 4}
    result = sol.merge_json_objects(j1, j2)
    print("Merged:", result)


if __name__ == "__main__":
    main()
