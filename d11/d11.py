# .1
# def read_file(f):
#     file = open(f)
#     text = file.readlines()
#     file.close()
#
#     lines = len(text)
#     longest_line = ""
#     words = 0
#     for line in text:
#         if len(line) > len(longest_line):
#             longest_line = line
#         words += len(line.split())
#     """
#     tavidan ase davwere mushaobs magrm zedmetad
#     gartulebuli iyo mgoni
#
#     lines = 0
#     longest_line = ""
#     words = 0
#     current_line = ""
#
#     for c in text:
#         current_line += c
#
#         if c == " ":
#             words += 1
#
#         if c == "\n":
#             lines += 1
#             words += 1
#
#             if len(longest_line) < len(current_line):
#                 longest_line = current_line
#
#             current_line = ""
#
#     if current_line :
#         if len(longest_line) < len(current_line):
#             longest_line = current_line
#         lines += 1
#         words += 1
#     """
#     return lines, longest_line, words
#
# x = read_file("text.txt")
# print(f"xazebi: {x[0]},\nyveraze grdzeli xazi: {x[1]},\nsityvebis raodenoba: {x[2]}")

# .2
def word_count(f_name, word):
    w_count = 0
    word = word.lower()
    with open(f_name) as file:
        text = file.read()
    for w in text.lower().split():
        if word == w.strip(" .!?,"):
            w_count += 1

    return w_count

print(f"word count = {word_count('text.txt', 'akaki')}")
