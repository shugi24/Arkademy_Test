# Jawaban Untuk Soal Nomor 1 #


import json

def biodata():
    biodata = {
        'name':'Sutra Sugi Prabowo',
        'age' : 23,
        'Address' : 'Jalan Cijerah II Blok Sukamaju no.66, Kel. Melong Kec. Cimahi Selatan',
        'hobbies' : ['Coding', 'Basketball', 'Reading books'],
        'is_married' : False,
        'list_school' : [
            {'year_in': 2015, 'year_out':2019, 'major': 'Sundanese Literature'},
            ],
        'skills' : [
            {'skill_name': 'Manchine Learning', 'level': 'advance'},
            {'skill_name': 'Python Engineer', 'level': 'Begginer'},
            {'skill_name': 'Web Develover', 'level': 'Begginer'},
            {'skill_name': 'Linguistics', 'level': 'Expert'}
            
            ],
        'interest_in_coding': True,
    }

    return json.dumps(biodata)

print(biodata())