#Jackie-Merritt_Chp9-10-Lab2_7/7/2025
import sys

def main():
    print('File Processor\n')
    file_name = input('Enter the name of the file you wish to process: ')
    contents = open_file(file_name)
    words = get_words(contents)
    total_cap = get_capitals(contents)
    print(f'The file {file_name} contains {len(words)} words of which {total_cap} of them are capitilized.')

def get_words(contents):
        words = contents.split()
        words.sort()
        return words

def get_capitals(contents):
    words = contents.split()
    capitilized = []
    for num in words:
        if num.islower() == False:
            capitilized.append(num)
    total_cap = len(capitilized)
    return total_cap
            

def open_file(file_name):
    try:
        with open(file_name) as file:
            contents = file.read()
            file.close()
            return contents
            
    except FileNotFoundError:
        print('File could not be found')
        sys.exit()
    
    
main()
