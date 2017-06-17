from generator import Generator

fields = [
    {
        'MiastoWydania': 'Warszawa',
        'NrZRejestru': 'KW001/213/2017',
        'TerminOd': '16.08.2017',
        'ImieNazwisko': 'Jan Kowalski',
        'NrZgody': 'ASDASDASDdf.dfsdfsdf',
        'DataUr': '16.08.1990',
        'DataZgody': '01.01.2017',
        'TerminDo': '18.08.2017',
        'DataWydania': '18.08.2017',
        'WydajacyZgode': 'Mazowiecki KO'
    },
    {
        'MiastoWydania': 'Warszawa',
        'NrZRejestru': 'KW001/213/2017',
        'TerminOd': '16.08.2017',
        'ImieNazwisko': 'Marek Kowalski',
        'NrZgody': 'ASDASDASDdf.dfsdfsdf',
        'DataUr': '16.08.1990',
        'DataZgody': '01.01.2017',
        'TerminDo': '18.08.2017',
        'DataWydania': '18.08.2017',
        'WydajacyZgode': 'Mazowiecki KO'
    },
    {
        'MiastoWydania': 'Warszawa',
        'NrZRejestru': 'KW001/213/2017',
        'TerminOd': '16.08.2017',
        'ImieNazwisko': 'John malkovic',
        'NrZgody': 'ASDASDASDdf.dfsdfsdf',
        'DataUr': '16.08.1990',
        'DataZgody': '01.01.2017',
        'TerminDo': '18.08.2017',
        'DataWydania': '18.08.2017',
        'WydajacyZgode': 'Mazowiecki KO'
    },
    {
        'MiastoWydania': 'Warszawa',
        'NrZRejestru': 'KW001/213/2017',
        'TerminOd': '16.08.2017',
        'ImieNazwisko': 'Marek Mostowiak',
        'NrZgody': 'ASDASDASDdf.dfsdfsdf',
        'DataUr': '16.08.1990',
        'DataZgody': '01.01.2017',
        'TerminDo': '18.08.2017',
        'DataWydania': '18.08.2017',
        'WydajacyZgode': 'Mazowiecki KO'
    },
    {
        'MiastoWydania': 'Warszawa',
        'NrZRejestru': 'KW001/213/2017',
        'TerminOd': '16.08.2017',
        'ImieNazwisko': 'Hanna Mostowiak',
        'NrZgody': 'ASDASDASDdf.dfsdfsdf',
        'DataUr': '16.08.1990',
        'DataZgody': '01.01.2017',
        'TerminDo': '18.08.2017',
        'DataWydania': '18.08.2017',
        'WydajacyZgode': 'Mazowiecki KO'
    }
]

cert = Generator("cert_kurs_template.docx")
cert.marge_pages_to_file(fields, "certyfikaty.docx")