import json
import os
from docx import Document
from importlib import import_module as im

class Work:

    def __init__(self, basepath, works, settings_for_works):
        self.basepath = basepath
        self.works = works
        self.settings_for_works = settings_for_works
        self.settings = {}
        self.global_settings = {}
        if os.path.isfile(settings_for_works):
            with open(settings_for_works, 'r') as file:
                self.global_settings = json.load(file)

    def create_work(self, work):
        if work in self.works:
            self._create_work(work)

    def create_all_works(self):
        for work in self.works:
            self._create_work(work)

    def _create_work(self, work):
        self.settings = self.global_settings.get(work, {})
        _, _, files = next(os.walk(self.basepath/work))
        
        file_name = self.basepath/f"{work}.docx"
        course_work = Document()

        processing = None
        for task in self.settings["structure"]:
            processing = im(".".join([str(self.basepath).split("/")[-1], 
                work, task.split('.')[0]]))

            course_work, self.settings = processing.Task(
                course_work, self.settings).run()

            course_work.save(file_name)