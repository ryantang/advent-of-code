import re

translator = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
class Decoder:
    def decode(text_line):
        decoded = Decoder._first_digit(text_line) + Decoder._last_digit(text_line)
        return int(decoded)
    
    def decode_with_spelling(text_line):
        decoded = Decoder._first_number(text_line) + Decoder._last_number(text_line)
        return int(decoded)

    def _first_number(text_line):
        converted = Decoder._convert_first_digit(text_line)
        return Decoder._first_digit(converted)
    
    def _last_number(text_line):
        converted = Decoder._convert_last_digit(text_line)
        return Decoder._last_digit(converted)

    def _convert_first_digit(text):
        regex_pattern = '|'.join(re.escape(key) for key in translator.keys())
        return re.sub(regex_pattern, lambda m: translator[m.group(0)], text, count=1)
    
    def _convert_last_digit(text):
        text_reversed = Decoder._reverse_string(text)        
        translator_reversed = Decoder._reverse_dict(translator)
        
        regex_pattern = '|'.join(re.escape(key) for key in translator_reversed.keys())
        result_reversed = re.sub(regex_pattern, lambda m: translator_reversed[m.group(0)], text_reversed, count=1)
        result = Decoder._reverse_string(result_reversed)        
        return result

    def _reverse_string(s):
        return s[::-1]

    def _reverse_dict(d):
        return {k[::-1]: v for k, v in d.items()}

    def sum_decoded_from_file(file):
        f = open(file, 'r')
        lines = f.readlines()
        f.close()
        sum = 0
        for line in lines:
            sum += Decoder.decode(line)
        return sum

    def sum_decoded_with_spelling_from_file(file):
        f = open(file, 'r')
        lines = f.readlines()
        f.close()
        sum = 0
        for line in lines:
            sum += Decoder.decode_with_spelling(line)
        return sum

    def _first_digit(text_line):
        i = 0
        while i < len(text_line):
            if text_line[i].isdigit():
                return text_line[i]
            i += 1

    def _last_digit(text_line):
        i = len(text_line) - 1
        while i >= 0:
            if text_line[i].isdigit():
                return text_line[i]
            i -= 1

