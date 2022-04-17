from selenium import webdriver

from successful_login import *
from new_patient import *
from pages.base_element import BaseElement
from pages.med_page import LoginPage
from pages.med_page import MedPage


# Test Setup
currentURL = None

# Test
med_page = MedPage(driver=browser)
med_page.go()
med_page.new_request_button.click()
med_page.patient_field.find()
med_page.patient_field.input_text('Dima Kutovyi')
med_page.medication_field.click()
med_page.medication_field.input_text('Hydroxyzine - m00056')
med_page.prescription_field.input_text('Donec tincidunt pellentesque velit. Nunc semper lorem eu elit luctus mattis. '
                                       'Morbi volutpat eros dolor, sit amet ultrices neque commodo et.')
med_page.quantity_field.input_text(3)
med_page.refils_field.input_text(5)
med_page.add_button.click()
med_page.pop_up_button.click()