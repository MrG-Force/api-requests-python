import requests


def main():
    # url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"
    url = "https://api.github.com/emojis"
    pets_count = get_json_obj_count(url)
    if pets_count:
        print(f"The number of pets is: {pets_count}, {type(pets_count)}")


def get_json_obj_count(url):
    try:
        response = requests.get(url)

    except requests.ConnectionError as e:
        print("A connection error ocurred. Please check your internet connection or try a different url.")

    else:
        print(
            f"The API returned {len(response.json())} in a {type(response.json())}")
        return len(response.json())


if __name__ == "__main__":
    main()
