trida = {
    'student1': {'jmeno': 'Jarda', 'vek': 18},
    'student2': {'jmeno': 'Filip', 'vek': 19},
    'student3': {'jmeno': 'Saša', 'vek': 20},
    'student4': {'jmeno': 'Zuzka', 'vek': 18},
    'student5': {'jmeno': 'LUKY', 'vek': 19}
}

for student, info in trida.items():
    print("Jméno:", info['jmeno'])
    print("Věk:", info['vek'])
