def main():
    response = input("What is your input? ")
    print(convert(response))

def convert(response):
    response = response.replace(":)", "🙂").replace(":(", "🙁")
    return response

main()
