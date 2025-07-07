#Jackie-Merritt_Chp9-10-Lab2_7/7/2025

def main():
    print('File Processor\n')
    file_name = input('Enter the name of the file you wish to process: ')
    words = get_words(file_name)
    print(f'The total number of words were {len(words)}')
    print(words)

def get_words(file_name):
    try:
        with open(file_name) as file:
            contents = file.read()
            file.close()
        contents = contents.replace("\n", "")
        contents = contents.replace(",", "")
        contents = contents.replace(".", "")
        contents = contents.replace("â€“", "")
        contents = contents.lower()

        words = contents.split(" ")
        words.sort()
        return words

    except FileNotFoundError:
        print('File could not be found')
    
main()
