#Outputing parsed information from Kaufman_Parser to Database

#VERY IMPORTANT FOR THE IMPORT TO WORK YOU NEED TO INSTALL PANDAS
#FROM THE COMMAND LINE JUST TYPE IN "pip install pandas" and press enter 
import pandas as pd

#if you change this rename your excel file too
excel_file = "Output.xlsx"

database = pd.read_excel(excel_file)

abbreviations = {
    'pChl' : "proto Ch'ol",
    'LL+GQ': "Lowland + Greater Q'anjob'alan",
    'eGK' : "eastern Greater K'iche'an",
    'GK' : "Greater K'iche'an",
    'GQ': "Greater Q'anjob'alan",
    'GLL?' : "Greater Lowland?",
    'Was+LL' : "Wasteko + Lowland",
    'WAS+LL' : "Wasteko + Lowland",
    'WM+GM' : "Western Mayan + Greater Mamean",
    'EM+' : "Eastern Mayan+",
    'GLL+WM' : "Greater Lowland + Western Mayan",
    'GLL+' : "Greater Lowland+",
    'Yu+' : "Yukatekan+",
    'LL+Was' : "Lowland + Wasteko",
    'WASw': 'Western (Tancanhuitz)',
    'WASc': 'Central (Tantoyuca)',
    'WASe': 'Eastern (Chontla, Chinampa)',
    'MAMt': 'Tacana*',
    'MAMo': 'Ostuncalco',
    'MAMc': 'Cajola*',
    'MAMi': 'San Idlefonso Ixtahuaca*n',
    'IXLne': 'Nebaj',
    'IXLco': 'Cotzal',
    'IXLch': 'Chajul',
    'KCHn': 'Nahuala*',
    'KCHq': 'Quiche*',
    'KCHc': 'Chichicastenango',
    'KCHk': 'Chicaj',
    'KAQp': 'Patzu*n',
    'KAQc': 'Comalapa',
    'KAQt': 'Tecpa*n',
    'PQMp': 'Pali*n',
    'PQMj': 'San Lui*s Jilotepeque',
    'QEQw': 'Western (Coba*n, Chamelco)',
    'QEQe': 'Eastern (Lanqui*n and Cahabo*n)',
    'QEQl&c': 'Lanqui*n and Cahabo*n',
    'pM': 'proto-Mayan',
    'pWa': 'proto-Wastekan',
    'WAS': 'Wasteko /teenek/',
    'KAB': 'Kabil ("Chicomuselteco")',
    'pYu': 'proto-Yukatekan',
    'YUK': 'Yukateko /maHya/',
    'LAK': 'Lakantun',
    'ITZ': 'Itzaj',
    'MOP': 'Mopan',
    'pCM': 'proto Central Mayan',
    'pWM': 'proto Western Mayan',
    'pGTz': 'proto Greater Tzeltalan',
    'EpM': 'Epigraphic Mayan',
    'pCh': "proto-Ch'olan",
    'CHR': "Ch'orti7",
    'CHT': "Ch'olti7 [col]",
    'CHL': "Ch'ol",
    'YOK': "Yokot'an (Chontal of Tabasco)",
    'pTzp': 'proto-Tzeltalan Proper',
    'TZO': "Tzotzil /b'atz'i k'op/",
    'TZE': "Tzeltal /b'atz'il k'op/",
    'pGQ': "proto Greater Q'anjob'alan",
    'pChT': "proto-Chujean (proto-Chuj-Tojol 7ab'al)",
    'TOJ': "Tojol 7ab'al",
    'CHJ': 'Chuj',
    'pQp': "proto-Q'anjob'al Proper",
    'QAN': "Q'anjob'al",
    'AKA': 'Akateko',
    'POP': 'Popti7',
    'pKo': "proto-Kotoke /qato7k'/",
    'MCH': 'Mocho* /mo:cho7/ ("Motozintleco")',
    'TUZ': '"Tuzanteco" /mu:chu7/',
    'pEM': 'proto Eastern Mayan',
    'pGM': 'proto Greater Mamean',
    'pMp': 'proto-Mamean Proper',
    'TEK': 'Teko (Cuilquen*o)',
    'MAM': 'Mam /qyool/',
    'pIx': 'proto-Ixilan',
    'AWA': 'Awakateko',
    'IXL': 'Ixil',
    'pGK': "proto Greater K'iche'an",
    'pUK': "proto Uspanteko-K'iche'an",
    'USP': 'Uspanteko (Musre*)',
    'pKp': "proto-K'iche'an Proper",
    'KCH': "K'iche7 /k'iche7 ch'aab'al/",
    'SIP': 'Sipakapense',
    'SAK': 'Sakapulteko',
    'TZU': "Tz'utujiil",
    'KAQ': 'Kaqchikeel',
    'PQM': 'Poqomam',
    'WM+LL': 'Western Mayan + Lowland',
    'PCH': 'Poqomchii7',
    'QEQ': "Q'eqchi7",
    'CM' : "Central Mayan: WM + EM",
    'WM' : "Western Mayan: GTz + GQ",
    'EM' : "Eastern Mayan: GM + GK",
    'GTz' : "Ch + Tz",
    'GQ' : "Chujean + Qanjobal + Kotoke",
    'GM' : "Ix + Mp",
    'GK' : "UK + PQ",
    'GK+' : "Greater K'iche'an+",
    'LL' : "Lowland",
    'GLL' : "Greater Lowland",
    'Hue' : "Huehuetenango",
    'LL+WM': "Lowland + Western Mayan",
    'LL+WM+': "Lowland + Western Mayan+",
    'LL+': "Lowland+"
}

parts_speech = {
    'adv' : "adverbo",
    'vt' : 'verbo transativo',
    'vi' : 'verbo intransitivo',
    's' : "sustantivos" ,
    'v' : "verbo",
    's/aj' : "sustantivo/adjetivos",
    'aj' : "adjetivo",
    'sv' : "sustantivo verbo",
    'agt' : "argumento",
    'p' : "pronombre",
    'ajs' : "adjetivos",
    'aj/s': "adjetivos/sustantivo",
    'pt' : "pronombre transativo",
    'caus' : "causante",
    'cn' : "conjuction",
    'num' : "numero",
    'sds' : "sds",
    'instr' : "instr",
    'temp' : "temp"
    }


def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        parsed_data = []
        i = 0
        current_row = 1
        for line in lines:
            #just to reset the line we are on 
            if i == 4:
                i = 0
                current_row += 1
            #this handles the first line of the text file (categories)    
            if i == 0:
                #category stuff
                category = line.split(':')[0]
                sub_category = line.split(':')[1]
                database.at[current_row,"Category"] = category.strip()
                database.at[current_row, "Sub Category"] = sub_category.strip()
            #this handles the second line of the text file (parent word)    
            if i == 1:
                #parent entry stuff
                splited_line = line.strip().split(' ')
                #gets the lang id and langauge 
                langID = ""
                langauge = ""
                if abbreviations.get(splited_line[0]) is not None:
                    langID = splited_line[0]
                    langauge = abbreviations.get(langID)
                else:
                    for entry in splited_line:
                        if entry.__contains__('?') or entry.__contains__('cf.'):
                            langauge = entry
                database.at[current_row, 'Langauge Abbrv'] = langID
                database.at[current_row, 'Language'] = langauge
                

                index = line.find(langID)
                substring = line[index + len(langID):]                
                database.at[current_row, "Entry"] = substring.strip()
            #this handles the third line of the text file (child word)       
            if i == 2:
                #langauge entry DONT REALLY WANT TO MESS WITH THIS BUT I WILL
                #EVENTUALLY TO MAKE IT EASIER TO READ
                splited_line = line.strip().split(None, 3)
                if splited_line[0].strip() == "cf.":
                    database.at[current_row,"Confer"] = "yes"
                    splited_line.pop(0)
                else:
                    database.at[current_row, "Confer"] = "no"
                if splited_line[0].strip() == '?   ':
                    database.at[current_row, "? In Entry"] = "yes"
                    splited_line.pop(0)
                else:
                    database.at[current_row, "? In Entry"] = "no"

                #gets the lang id and langauge 
                langID = splited_line[0]
                langauge = abbreviations.get(langID)
                database.at[current_row, 'Lang Abbrv'] = langID
                database.at[current_row, 'Language.1'] = langauge
                
                word = ""
                parts_of_speech = ""
                def_ = ""
                source = ""
                if len(splited_line) > 1:
                    temp = (line.split(None))
                    temp.pop(0)
                    next_word_src = False
                    
                    #this checks for the source
                    for entry in temp:
                        if entry.__contains__('//'):
                            continue
                        if next_word_src is True:
                            source += ' ' + entry + ' '
                            next_word_src = False
                        if entry.__contains__('[') and entry.__contains__(']'):
                            source += entry.strip() + ' '
                        elif entry.__contains__('['):
                            next_word_src = True
                            source += entry                                 
                                        
                    j = 0
                    #this grabs the actual word
                    for entry in temp:                        
                        cur = parts_speech.get(entry)
                        if entry.__contains__('<') and entry.__contains__('>'):
                            word += ' ' + entry
                            break
                        if entry.__contains__('//'):
                            continue
                        if j == 1 and cur == None and not entry.__contains__('['):
                            word += ' ' + entry
                            
                        elif j == 0:   
                            word += ' ' + entry
                        j += 1
                        
                    word = word.strip() 
                #print(word)
                index_of_word = line.find(word)
                substring_of_word = line[index_of_word + len(word):]
                substring_of_word = substring_of_word.split(None)
                
                if len(substring_of_word) > 1 and parts_speech.get(substring_of_word[0]) != None :
                    parts_of_speech = substring_of_word[0]
                    substring_of_word.pop(0)
                if len(substring_of_word) > 1:
                    for entry in substring_of_word:
                       if entry != "//" and not entry.startswith('['):
                           def_ += entry + ' '
                  
                database.at[current_row,"Source"] = source 
                database.at[current_row, "Word"] = word
                database.at[current_row, "Parts of Speech"] = parts_of_speech.strip()
                database.at[current_row, "Definition"] = def_.strip()
            #this handles the fourth line of the text file (page number)
            if i == 3:
                #page number
                database.at[current_row,"Page in Kaufman's file"] = line.strip()
            i += 1
        #the line below saves the changes to your excel file   
        database.to_excel(excel_file,"Sheet1",index=False)
    return parsed_data


#if you change filename rename your text file too  
filename = 'OutputFromKaufmanParser.txt'
parsed_data = parse_input(filename)


