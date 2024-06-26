class Decoder:
    def decode(text_line):
        decoded = Decoder.first_digit(text_line) + Decoder.last_digit(text_line)
        return int(decoded)

    def first_digit(text_line):
        i = 0
        while i < len(text_line):
            if text_line[i].isdigit():
                return text_line[i]
            i += 1

    def last_digit(text_line):
        i = len(text_line) - 1
        while i >= 0:
            if text_line[i].isdigit():
                return text_line[i]
            i -= 1

    def sum_decoded_from_file(file):
        f = open(file, 'r')
        lines = f.readlines()
        f.close()
        sum = 0
        for line in lines:
            sum += Decoder.decode(line)
        return sum
