from uuid import uuid4


def add_medication(data, user_id):
    name = input('Medication name: ').strip()
    if not name:
        print('Medication name cannot be empty.')
        return
    dose = input('Dose as written on prescription/label: ').strip()
    times_text = input('Reminder times (HH:MM, separated by commas): ')
    times = [part.strip() for part in times_text.split(',') if part.strip()]
    from datetime import datetime
    try:
        for scheduled_time in times:
            datetime.strptime(scheduled_time, '%H:%M')
    except ValueError:
        print('Invalid time. Use 24-hour HH:MM, e.g. 08:00, 20:00.')
        return
    medication = {'id': uuid4().hex[:8], 'name': name, 'dose': dose, 'times': times, 'active': True}
    data['users'][user_id]['medications'].append(medication)
    print('Medication added.')


def list_medications(data, user_id):
    medications = data['users'][user_id]['medications']
    if not medications:
        print('No medications saved for this user.')
        return
    for med in medications:
        print(f'{med["name"]} | Dose: {med["dose"]} | Times: {", ".join(med["times"]) or "none"}')
