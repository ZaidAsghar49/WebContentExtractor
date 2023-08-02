import requests
from bs4 import BeautifulSoup

def heading_extractor(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        return headings
    else:
        print("Error: Unable to fetch the web page.")
        return []


def paragraph_extractor(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        return paragraphs
    else:
        print("Error: Unable to fetch the web page.")
        return []

def image_extractor(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')
        return images
    else:
        print("Error: Unable to fetch the web page.")
        return []

def link_extractor(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')
        return links
    else:
        print("Error: Unable to fetch the web page.")
        return []

def main():
    url = input("Enter the URL to extract information: ")

    print("Choose the type of Information:")
    print("1: Heading\n2: Paragraphs\n3: Links\n4: Images\n5: Exit\n")

    option = input("Option: ")

    if option == '1':
        headings = heading_extractor(url)
        if headings:
            print("Extracted Headings:")
            for index, heading in enumerate(headings, 1):
                print("{}. {}".format(index, heading.text))
        else:
            print("No headings found on the web page.")
    elif option == '2':
        paragraphs = paragraph_extractor(url)
        if paragraphs:
            print("Extracted Paragraphs:")
            for index, paragraph in enumerate(paragraphs, 1):
                print("{}. {}".format(index, paragraph.text))
        else:
            print("No paragraphs found on the web page.")

    elif option == '3':
        links = link_extractor(url)
        if links:
            print("Extracted links:")
            for index, link in enumerate(links, 1):
                print("{}. {}".format(index, link.get('href')))
        else:
            print("No links found on the web page.")

    elif option == '4':
        images = image_extractor(url)
        if images:
            print("Extracted images:")
            for index, image in enumerate(images, 1):
                img_url = image.get('src')
                print("{}. {}".format(index, img_url))
        else:
            print("No images found on the web page.")

    elif option == '5':
        print("Exiting...")
        exit()
    else:
        print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
