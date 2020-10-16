# AI poem
An attempt to write an AI agent able to write terzine (a special kind of Italian poetry).

# How to download new poems:
1. Choose a poem on 'https://it.wikisource.org/wiki/Pagina_principale'
2. Select the id name of the poem from its url (e.g. url = https://it.wikisource.org/wiki/Atlantide => id name = Atlantide)
3. add the chosen name in the file ELT_params.yaml 
4. run main_ETL.py
5. Run parser_files.py in order to clean and reshape the text to be feed the algorithm.
