# This code exemplifies the data flow in Task 2 of lesson 603

# Refinements
def ask_for_and_store_badge_text(): # No parameters because no data in
    return "Hello Computing" # badge_text is passed out

def ask_for_and_store_number_of_badges():  # No parameters because no data in
    return 5 # number_of_badges is passed out

def display_the_badge_text(thisBadge_Text): # badge_text is passed in
    print(thisBadge_Text)
    # no data passed out

# Top-level Design
badge_text = ask_for_and_store_badge_text()
number_of_badges = ask_for_and_store_number_of_badges()
for index in range(number_of_badges):
    display_the_badge_text(badge_text)