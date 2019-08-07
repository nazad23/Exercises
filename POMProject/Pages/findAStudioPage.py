class FindAStudioPage():

    def __init__(self, driver):
        self.driver = driver
        self.find_a_studio_button_id = "ela-menu-visitor-desktop-supplementa_find-a-studio"
        self.zip_code_id = "meetingSearch"
        self.submit_button_id = "btn.spice-translated"
        self.firstResult_location_id = "location__name"

    def click_find_a_studio(self):
        self.driver.find_element_by_id(self.find_a_studio_button_id).click()

    def enter_zip_code(self, zip_code):
        self.driver.find_element_by_id(self.zip_code_id).send_keys(zip_code)

    def click_submit(self):
        self.driver.find_element_by_class_name(self.submit_button_id).click()

    def click_first_selection(self):
        self.driver.find_element_by_class_name(self.firstResult_location_id).click()

