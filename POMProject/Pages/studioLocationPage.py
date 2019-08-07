class StudioLocationPage():

    def __init__(self, driver):
        self.driver = driver
        self.todays_studio_sched_id = "hours-list-item-wrapper.hours-list--currentday"

    def print_todays_studio_schedule(self):
        print(self.driver.find_element_by_class_name(self.todays_studio_sched_id).text)