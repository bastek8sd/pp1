lang = ['Java', 'Python', 'JavaScript', 'C++',
         'C#', 'Ruby', 'Perl', 'PHP', 'C', 'Android']

val = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]

def rysujWykres(jezyki, wartosci):
    d = dict(zip(jezyki, wartosci))
    for key in d:
        print('{:>10}: {}'.format(key, '#'*d[key],))
        
rysujWykres(lang, val)