<h1> A guide to Kaufman_Destroyer. </h1>

In Kaufman_Parser.py you can modify the langauge you are trying to make a database of by changing the lang_abbrv variable on line 78 to whatever language abbreviation. For example
if I want to make a Ch'olti database I would set lang_abbrv = "CHT"

After running Kaufman_Parser.py it will output a file called "OutputFromKaufmanParser.txt" this text file is then use in the Parsed_to_Database.py to convert this text file to a
Excel database called Output.xlsx.  

If you change the name of your "OutputFromKaufmanParser.txt" file make sure to change line 269 to the new name you changed it to (filename). The same goes for the Excel file, make sure you to change line 8, excel_file.

Lastly, the output file needs to have the following column headers so it knows where to put the correct information in the right place. 
"Category"	"Sub Category"	"Langauge Abbrv"	"Language"	"Entry"		"Lang Abbrv"	"Language.1"	"Confer"	"? In Entry"	"Word"	"Parts of Speech"	"Definition"	"Source"	"Page in Kaufman's file"

![image](https://github.com/kevin14767/Kaufman_Destroyer/assets/95306723/eb2c1b40-0b6e-4944-ad21-53de6e4c96b2)

Also I believe I have made the code open to editing and pushing to this git repo but if for some reason you are unable to push to the git repo contact my email.

<a href = "mailto: kevinbarcenas2022@gmail.com">Send Email</a>

Created by Kevin Barcenas part of the Linguistics Research Center.
