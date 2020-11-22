import os
from pathlib import Path
from utils.works import Work

BASE_DIR = Path(__file__).resolve().parent

LABORATORY_STORE = BASE_DIR / 'laboratory_works'

_, laboratories_list, _ = next(os.walk(LABORATORY_STORE))

courses = Work(COURSES_STORE, courses_list, BASE_DIR/'laboratory_works_settings.json')
courses.create_all_works()
