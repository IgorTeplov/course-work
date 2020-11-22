import os
from pathlib import Path
from utils.works import Work

BASE_DIR = Path(__file__).resolve().parent

COURSES_STORE = BASE_DIR / 'course_works'

_, courses_list, _ = next(os.walk(COURSES_STORE))

courses = Work(COURSES_STORE, courses_list, BASE_DIR/'course_works_settings.json')
courses.create_all_works()