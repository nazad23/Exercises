# Steps:
# 1. Navigate to https://www.weightwatchers.com/us/
# 2. Verify loaded page title matches “WW (Weight Watchers): Weight Loss & Wellness Help”
# 3. On the right corner of the page, click on “Find a Studio”
# 4. Verify loaded page contains “Find WW Studios & Meetings Near You | WW USA”
# 5. In the search field, search for meetings for zip code: 10011
# 6. Print the title of the first result and the distance (located on the right of location tite/name)
# 7. Click on the first search result and then, verify displayed location name/title matches with the name of the first searched result that was clicked
# 8. From this location page, print TODAY’s hours of operation (located towards the bottom of the page)
# 9. Create a method to print the number of meeting the each person (under the scheduled time) has a particular day of the week  e.g. printMeetings(“Sun)  
# Output should be:
# Person A 3
# Person B 1

import time
import unittest
from POMProject.Tests.base import DriverManager
from POMProject.Pages.findAStudioPage import FindAStudioPage
from POMProject.Pages.studioLocationPage import StudioLocationPage

class WWTest(DriverManager):

    def test_one_scenario(self):
        driver = self.driver
        driver.get("https://www.weightwatchers.com/us/")

        findStudio = FindAStudioPage(driver)
        print("Homepage Title: " + driver.title)
        assert ('WW (Weight Watchers): Weight Loss & Wellness Help' == driver.title)

        findStudio.click_find_a_studio()
        time.sleep(2)

        #Assert title
        print("Current Page Title: " + driver.title)
        assert ('Find WW Studios & Meetings Near You | WW USA' == driver.title)

        #Enter zip
        findStudio.enter_zip_code("10011")
        findStudio.click_submit()

        firstResultLocation = self.driver.find_element_by_class_name("location__name").text
        firstResultDistance = self.driver.find_element_by_class_name("location__distance").text
        print("First Result: " + firstResultLocation, firstResultDistance)

        #click first result, store result, assert firstresult & currentResult
        findStudio.click_first_selection()
        currentResult = self.driver.find_element_by_class_name("location__name").text
        assert firstResultLocation == currentResult

        #Print hours of operation for Today
        studioLocation = StudioLocationPage(driver)
        studioLocation.print_todays_studio_schedule()

    def test_printMeetings(self, day_input):
        elements = self.driver.find_elements_by_class_name("schedule-detailed-day")

        week_dict = {"sun": 0, "mon": 1, "tue": 2, "wed": 3, "thu": 4, "fri": 5, "sat": 6}
        daily_schedule = elements[week_dict[day_input.lower()]].text.split("\n")
        daily_schedule.pop(0)

        print("\nSchedule for " + day_input + ": ")

        for instructors in range(len(daily_schedule) // 2):
            time = daily_schedule.pop(0)
            name = daily_schedule.pop(0)
            print(name, time)

if __name__ == "__main__":
    Example = WWTest()
    Example.test_one_scenario()
    Example.test_printMeetings("thu")
    Example.tearDownClass()




