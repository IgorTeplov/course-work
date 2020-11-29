import os, signal, sys, time
from pathlib import Path
from utils.works import Work

BASE_DIR = Path(__file__).resolve().parent

COURSES_STORE = BASE_DIR / 'course_works'

_, courses_list, _ = next(os.walk(COURSES_STORE))

def handler(signum, frame):
    print('So long ...')
    sys.exit()

signal.signal(signal.SIGALRM, handler)

t_s = time.time()
print(f"START: {t_s}")

courses = Work(COURSES_STORE, courses_list, BASE_DIR/'course_works_settings.json')

# signal.alarm(24)
courses.create_all_works()
# signal.alarm(0)

t_e = time.time()
print(f"END: {t_e}")
print(f"DELTA: {t_e-t_s}")