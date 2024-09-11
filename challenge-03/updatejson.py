import json
import csv
import argparse

def update_json_from_csv(env, json_file, csv_file):
    # Load the JSON file
    with open(json_file, 'r') as jf:
        config_data = json.load(jf)

    # Check if the environment exists in the JSON file
    if env not in config_data:
        print(f"Environment {env} not found in {json_file}")
        return

    # Read the CSV file and update the JSON data
    with open(csv_file, mode='r') as cf:
        csv_reader = csv.reader(cf)
        for row in csv_reader:
            if len(row) == 2:
                key, value = row
                if key in config_data[env]:
                    print(f"Updating {env} config: {key} = {value}")
                    config_data[env][key] = value
                else:
                    print(f"Key {key} not found in {env} environment")

    # Write the updated JSON back to the file
    with open(json_file, 'w') as jf:
        json.dump(config_data, jf, indent=4)

    print(f"{env} environment in {json_file} updated successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update JSON config based on environment and CSV input.")
    parser.add_argument("--env", required=True, help="The environment to update (e.g., DEV or PROD)")
    parser.add_argument("--json", required=True, help="Path to the JSON config file")
    parser.add_argument("--csv", required=True, help="Path to the CSV input file")

    args = parser.parse_args()

    update_json_from_csv(args.env, args.json, args.csv)
