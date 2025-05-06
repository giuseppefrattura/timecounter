from datetime import datetime, timedelta

TIME_FORMAT = "%H:%M"

def calculate_exit_time(entry_time_str, lunch_start_str, lunch_end_str, work_hours=8):
    entry_time = datetime.strptime(entry_time_str, TIME_FORMAT)
    lunch_start = datetime.strptime(lunch_start_str, TIME_FORMAT)
    lunch_end = datetime.strptime(lunch_end_str, TIME_FORMAT)

    # Calcolo tempo lavorato prima della pausa
    before_lunch = lunch_start - entry_time

    # Calcolo durata pausa
    actual_lunch_duration = lunch_end - lunch_start

    # Se la pausa è inferiore a 1 ora, viene forzata a 1 ora
    min_lunch_duration = timedelta(hours=1)
    effective_lunch_duration = max(actual_lunch_duration, min_lunch_duration)

    # Calcolo orario di ripresa effettivo (pausa estesa se necessario)
    adjusted_lunch_end = lunch_start + effective_lunch_duration

    # Calcolo quante ore mancano
    total_work = timedelta(hours=work_hours)
    remaining_work = total_work - before_lunch

    # Calcolo orario di uscita
    exit_time = adjusted_lunch_end + remaining_work

    return exit_time.strftime(TIME_FORMAT)

if __name__ == "__main__":
#   E09:17-U13:45-E14:09

    entry = "09:17"
    lunch_start = "13:45"
    lunch_end = "14:09"
    work_hours = 8

    exit_time = calculate_exit_time(entry, lunch_start, lunch_end, work_hours)
    print(f"Devi uscire alle: {exit_time}")
