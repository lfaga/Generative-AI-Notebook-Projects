import sys, torch, json
from safetensors import safe_open

def inspect_safetensors_metadata(file_path):
    clean_dict = {}
    try:
        with safe_open(file_path, framework="pt", device="cpu") as f:
            metadata = f.metadata()
            for key, value in metadata.items():
                if isinstance(value, str):
                    try:
                        clean_dict[key] = json.loads(value)
                    except json.JSONDecodeError:
                        clean_dict[key] = value
                else:
                    clean_dict[key] = value

    except Exception as e:
        print(f"Error processing file '{file_path}': {e}")
    return clean_dict

def print_safetensors_metadata(file_path):
    
    final_json_string = json.dumps(inspect_safetensors_metadata(file_path))
    output_filepath = file_path + ".json"

    try:
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(final_json_string)
        print(f"Successfully saved JSON to: {output_filepath}")

    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python inspect_safetensors.py <path_to_safetensors_file>")
        sys.exit(1)

    safetensors_path = sys.argv[1]
    
    print_safetensors_metadata(safetensors_path)