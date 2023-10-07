import re
from deep_translator import GoogleTranslator

# Define the regex pattern for matching text to translate
regex_pattern = r'"([^"\n]*[ЁёА-я][^"\n]*)"'

# Initialize the Google Translate translator
translator = GoogleTranslator(source='ru', target='en')

# Read the input text file
with open('Grace_Global.pwn', 'r', encoding='utf-8') as file:
    text = file.read()

def translate_stripped(match):
    print(match)
    translation = ''
    translation = translator.translate(text=match.group(1))
    if translation is None:
        return match.group(0)
    return match.string[:match.start(1)] + translation + match.string[match.end(1):]

def translate_match(match):
    print(match)
    translation = ''
    if match.group(0).isspace():
        return match.group(0)
    if re.fullmatch(r'[A-Za-z0-9.\s]+', match.group(0)) is not None:
        return match.group(0)
    mmtext = match.group(0)
    mmtext = re.sub(r'^\s*([0-9ЁёА-Яа-я?!\/\s,.-]+?)\s*$', translate_stripped, mmtext)
    return mmtext

# Use a function to preserve special characters during translation
def translate_whole_text_matches(match):
    print(match)
    #print(match.group(1))
    mmtext = match.group(1)
    mmtext = re.sub(r'[0-9ЁёА-Яа-я?!\/\s,.-]+', translate_match, mmtext)
    print(mmtext)
    return f'"{mmtext}"'

# Find all matches of the regex pattern in the text and translate them
text = re.sub(regex_pattern, translate_whole_text_matches, text)

# Write the translated text to a new file or overwrite the input file
with open('Grace_Global_translated.pwn', 'w', encoding='utf-8') as file:
    file.write(text)