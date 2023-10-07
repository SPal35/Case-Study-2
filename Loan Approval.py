import csv

def build_unique_profession_set(filename):
    unique_professions = set()
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            unique_professions.add(row['job'].strip().lower()) 
    return unique_professions

def get_loan_eligibility(unique_professions, profession):
    return profession.lower() in unique_professions

unique_professions = build_unique_profession_set('bank-data.csv')

min_age = 20
max_age = 65

while True:

    profession = input("Enter profession (type 'END' to exit): ").strip()


    if profession.lower() == 'end':
        break


    eligibility = get_loan_eligibility(unique_professions, profession)


    print(f"Client with profession '{profession}' is{' ' if eligibility else ' not '}eligible for the marketing campaign.")


    print(f"Maximum age for loan eligibility: {max_age}")
    print(f"Minimum age for loan eligibility: {min_age}")
