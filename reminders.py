def show_reminders(data, user_id):
    """Placeholder: display schedules; later add timed notifications."""
    for med in data['users'][user_id]['medications']:
        if med['active']:
            print(f'{med["name"]}: {", ".join(med["times"]) or "No times set"}')