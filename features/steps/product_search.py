from behave import given, when, then

# RESULTS_INFO = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")

@given('Open Amazon page')
def open_amazon(context):
    context.app.page.open_page()


@when('Search for {search_word}')
def input_search(context, search_word):
    context.app.top_nav_menu.search_word(search_word)


@when('When click on orders')
def click_orders_button(context):
    context.app.top_nav_menu.click_orders()


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    context.app.search_result_page.verify_found_result_text(search_word)


@when('Select {alias} department')
def select_department(context, alias):
    context.app.top_nav_menu.select_department(alias)

@then('{selected_dep} department in selected')
def verify_selected_department(context, selected_dep):
    context.app.top_nav_menu.verify_selected_department(selected_dep)