from behave import given, when, then


@then('{signin} logo is displayed')
def verify_found_results_text(context, signin):
    context.app.signin_page.sign_in_text(signin)


@then('Page title is correct')
def verify_page_title(context):
    context.app.signin_page.verify_title('Amazon Sign-In')
