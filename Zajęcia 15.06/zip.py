"""
Get city form zip code
"""

digit_to_area = {
    0: 'Warszawa',
    1: 'Olszyn',
    2: 'Wrocław',
    3: 'Szczecin',
    4: 'Łódź',
    5: 'Białystok',
    6: 'Opole',
    7: 'Gdańsk',
    8: 'Poznań',
    9: 'Sopot',
}

def get_city(zip_code):
    """
    Validate input and return city
    :param zip_code:
    :return:
    """
    if len(zip_code) !=6:
        return None
    if zip_code[2] != '-':
        return None
    if not (zip_code[:2] + zip_code[3:]).isdigit():
        return None

    city_code = int(zip_code[0])
    return digit_to_area[city_code]



if __name__=='__main__':
    code = input('Please provide zip code: ')
    city = get_city(code)
    if city:
        print(f'Elo gosciu z {city}')
    else:
        print('Wrong zip code')
