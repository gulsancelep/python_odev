# UTM settings on Newsletter design page
# on Maven design page, when you rename variation cross and check buttons
# input warning message, for example, on Journey SMS page when we try to save empty title input
# on Journey do list filter input
# tags list when we select template in created journey campaign and didn’t click Use this Template button
# on Journey do list how to click exactly needed campaign’s Statistics button if there is more than 1 campaigns in the list
# on Message box design page remove variation cross icon
#  Remove/ Change element buttons on Journey canvas page
#  Alert toaster on any page of panel
#  on Api and js (access area) free js body input
from selenium.webdriver.common.by import By

# 1- UTM settings on Newsletter design page
# $('[class="checkboxDefault checkboxDefault"]').click()
# $('.checkboxDefault').click()
Utm_settings = (By.CLASS_NAME, 'checkboxDefault')

# 2- on Maven design page, when you rename variation cross and check buttons
# $('.icon-checked').click()
icon_checked = (By.CLASS_NAME, 'icon-checked')

# $('.variationNameUpdateCancel')[0].click()
icon_closed = (By.CLASS_NAME, 'variationNameUpdateCancel')

# 3- input warning message, for example, on Journey SMS page when we try to save empty title input
warning_message = (By.LINK_TEXT, 'The Your Message field is required.')

# 4-  on Journey do list filter input
journey_filter_input = (By.CLASS_NAME, 'icon-search')

# 5- tags list when we select template in created journey campaign and didn’t click Use this Template button
tags_list = (By.CLASS_NAME, 'class="btn btnBlue btnSelectTemplate animationHalf"')

# 6- on Journey do list how to click exactly needed campaign’s
# Statistics button if there is more than 1 campaigns in the list
statistics = (By.XPATH, '//*[@id="personalizationList"]/tbody/tr[1]/td[7]')

# 7- on Message box design page remove variation cross icon
remove_variation = (By.CLASS_NAME, 'variationDelete')

# 8- Remove/ Change element buttons on Journey canvas page
change_element = (By.XPATH, '//*[@id="wait-for-some-time-2"]/svg/image[1]')
# //*[@id="wait-for-some-time-2"]/svg/image[1]
remove_element = (By.XPATH, '//*[@id="wait-for-some-time-2"]/svg/image[2]')
# //*[@id="wait-for-some-time-2"]/svg/image[2]

# 9- Alert toaster on any page of panel
alert_panel = (By.LINK_TEXT, 'Please fill all necessary fields')

# 10- on Api and js (access area) free js body input
alert_api = (By.LINK_TEXT, 'You are not authorized to access this page!')