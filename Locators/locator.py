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
UTM_SETTINGS = (By.CLASS_NAME, 'checkboxDefault')

# 2- on Maven design page, when you rename variation cross and check buttons
# $('.icon-checked').click()
ICON_CHECKED = (By.CLASS_NAME, 'icon-checked')

# $('.variationNameUpdateCancel')[0].click()
ICON_CLOSED = (By.CLASS_NAME, 'variationNameUpdateCancel')

# 3- input warning message, for example, on Journey SMS page when we try to save empty title input
WARNING_MESSAGE = (By.LINK_TEXT, 'The Your Message field is required.')

# 4-  on Journey do list filter input
JOURNEY_FILTER_INPUT = (By.CLASS_NAME, 'icon-search')

# 5- tags list when we select template in created journey campaign and didn’t click Use this Template button
TAGS_LIST = (By.CLASS_NAME, 'class="btn btnBlue btnSelectTemplate animationHalf"')

# 6- on Journey do list how to click exactly needed campaign’s
# Statistics button if there is more than 1 campaigns in the list
STATISTICS = (By.PARTIAL_LINK_TEXT, "/journey-builder/75758/statistics")

# 7- on Message box design page remove variation cross icon
REMOVE_VARIATION = (By.CLASS_NAME, 'variationDelete')

# 8- Remove/ Change element buttons on Journey canvas page
CHANGE_ELEMENT = (By.PARTIAL_LINK_TEXT, "/assets/img/journey-builder/do-it-your-self/change-element-icon.svg")
# //*[@id="wait-for-some-time-2"]/svg/image[1]
REMOVE_ELEMENT = (By.PARTIAL_LINK_TEXT, "/assets/img/journey-builder/do-it-your-self/delete-element-icon.svg")
# //*[@id="wait-for-some-time-2"]/svg/image[2]

# 9- Alert toaster on any page of panel
ALERT_PANEL = (By.LINK_TEXT, 'Please fill all necessary fields')

# 10- on Api and js (access area) free js body input
ALERT_API = (By.LINK_TEXT, 'You are not authorized to access this page!')