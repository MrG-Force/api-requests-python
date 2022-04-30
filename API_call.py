import requests
import argparse
import sys


def main():
    args = get_args()

    if args.sample:
        url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"
        pets_count = get_json_obj_count(url, args.verbose)
        print(f"The number of pets is: {pets_count[0]}")
    else:
        result = get_json_obj_count(args.URL, args.verbose)
        print(f"result: {result[1]} of size {result[0]} ")


def get_json_obj_count(url, verbose):
    try:
        response = requests.get(url)
        response.raise_for_status()

    except requests.exceptions.HTTPError as err:
        print("An HTTP error ocurred. Please check the url.")
        sys.exit()

    except requests.exceptions.ConnectionError as err:
        print("Couldn't reach the server. Please check your internet connection or try a different url.")
        sys.exit()
    else:
        if response.ok:
            length = len(response.json())
            object_type = "JSON object" if type(
                response.json()).__name__ == "dict" else "JSON array"
            if verbose:
                unit = "objects" if object_type == "JSON array" else "name/value pairs"
                print(
                    f"The API returned a {object_type} with {length} {unit}")
            return (length, object_type)


def get_args():
    parser = argparse.ArgumentParser(
        description="Call an API and display the number of returned results.")
    url_group = parser.add_mutually_exclusive_group(required=True)
    url_group.add_argument(
        "--URL", help="The URL representing the API endpoint")
    url_group.add_argument(
        "--sample", help="Call a sample API: https://petstore.swagger.io/v2/pet/findByStatus?status=available", action="store_true")
    parser.add_argument(
        "-v", "--verbose", help="Display extra information about the returned data", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    main()
