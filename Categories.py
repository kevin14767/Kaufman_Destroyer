# code to pre process KaufmanEtymologies.txt

def parse_file(input_file, langauge_id):
    try:
        with open(input_file, 'r') as file, open("Categories.txt", 'w') as output:
            # page number variables
            page_num_line_contains = 'Kaufman: preliminary Mayan Etymological Dictionary'
            page_num = None

            # parent word variables
            parent_word = None
            # language word variabled
            language_id_line = None
            langauge = False
            lang_ID = langauge_id

            # category of language ID word
            category = None
            # sub category of langauge ID
            first_ID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
            second_ID = '========================='
            sub_category = None

            prefixes = ['   ', 'cf. ', '?   ']
            substrings = ['%', first_ID, second_ID]
            prefixes_child = ['    ' + lang_ID, 'cf. ' + lang_ID, '?   ' + lang_ID]
            # keeps track of previous line for identifying sub categories
            prev_line = ""

            first_category = "KINSHIP & SOCIAL ORGANIZATION"
            parent_ready_to_print = False


            for line in file:
                # check for category word
                if line.startswith("%% "):
                    category = line.replace('%', '').strip()
                    if first_category != category:
                        break

                # check for a sub category
                if prev_line.__contains__(first_ID) or prev_line.__contains__(second_ID):
                    if line.isupper() or line.strip().isdigit():
                        sub_category = line.strip()
                    else:
                        sub_category = ""

                # check if parent
                if not any(line.startswith(prefix) for prefix in prefixes) and not any(
                        substring in line for substring in substrings):
                    # check if it's a page number entry
                    if line.__contains__(page_num_line_contains):
                        page_num = line.split(' ')[0]

                    # has to be parent word, can't be dividers
                    else:
                        parent_word = line
                        parent_ready_to_print = True
                else:
                    if line.startswith("   "):
                        language_id_line = line.strip()
                        langauge = True

                # keep track of previous line
                prev_line = line

                if parent_ready_to_print:
                    output.write(f"{category}\n{parent_word}\n")
                    parent_ready_to_print = False
                else:
                    output.write(f"{language_id_line}, Page num: {page_num}\n")
                # print(category)
                # when the langauge word has been found
                # if langauge:
                #     langauge = False
                #     #output.write(
                #         #f"{category.strip()}: {sub_category}\n{parent_word.strip()}\n{language_id_line.strip()}\n{page_num}\n")


    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


lang_abbrv = "CHT"
# if you change the name of input file just rename the text file too
input_file = 'KaufmanEtymologies.txt'
parse_file(input_file, lang_abbrv)