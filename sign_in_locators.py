"""Create a function that will take a string as an input and return the 1st non-unique letter of a string.
“Google” => “l”
“Amazon” => “m”
If there are no unique letters, return an empty string: “xoxoxo” => “”.
How would you test it? How would you handle edge cases?
"""
str_1 = 'Google'


def unique_char(string):
    string = string.lower()
    for item in string:
        if string.count(item) == 1:
            return item
            break
    return ''


print(unique_char(str_1))




"""
The most optimal locators for Create Account (Registration) page elements:

1. Amazon logo :

By.CSS_SELECTOR = ".a-icon-log"

2. Create account :

By.CSS_SELECTOR  = ".a-box-inner h1"

3. Your name :

By.ID = "ap_customer_name"

4. Email :

By.ID = "ap_email"

5. Password :

By.ID = "ap_password"

6. Re-enter password :

By.ID = "ap_password_check"

7. Create your Amazon account :

By.ID = "continue"

8. Conditions of use :

By.XPATH = "//a[contains(@href,'condition_of_use')]"

9. Privacy Notice :

By.XPATH = "//a[contains(@href,'privacy_notice')]"

10. Sign-In :

By.CSS_SELECTOR = ".a-link-emphasis"
"""
# Locators for Amazon Sign In page

# Amazon logo:

#By.XPATH : "//i[@class='a-icon a-icon-logo']"
#By.XPATH : "//i[@aria-label='Amazon']"
#By.XPATH : "//*[@role='img']"

# Email field :

#By.ID : "ap_email"
#By.NAME : "email"
#By.XPATH : "//*[@type='email']"

# Continue button:

#By.ID : "continue"
#By.XPATH : "//*[@class='a-button-input']"
#By.XPATH : "//*[@type='submit']"

# Conditions of use:

#By.XPATH : "//a[text()='Conditions of Use']"
#By.XPATH : "//a[contains(@href, 'condition of use')]"

# Privacy Notice:

#By.XPATH : "//a[text()='Privacy Notice']"
#By.XPATH : "//a[contains(@href, 'privacy_notice')]"

# Need Help?

#By.XPATH : "//span[@class='a-expander-prompt']"
#By.LINK_TEXT : 'Need help?'

# Forgot your password?

#By.ID : "auth-fpp-link-bottom"
#By.LINK_TEXT : 'Forgot your password?'

# Other issues:

#By.ID : "ap-other-signin-issues-link"
#By.LINK_TEXT : "Other issues with Sign-In"

# Create Amazon account:

#By.ID : "createAccountSubmit"
#By.LINK_TEXT : "Create your Amazon account"
#By.XPATH : "//span[@class='a-button-inner']/a"










