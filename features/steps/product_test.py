from behave import given, when, then

@given("Open Amazon {product_id} produst page")
def open_amazon_prodcut_page(context, product_id):
    context.app.product_page.open_product()


@when('Hover over Add to Cart button')
def hover_add_to_cart(context):
    context.app.product_page.hover_add_to_cart()


@then('Verify size selection tooltip is shown')
def verify_size_tooltip(context):
    context.app.product_page.verify_size_tooltip()


@when('Hover over New Arrivals')
def hover_new_arrivals(context):
    context.app.product_page.hover_new_arrivals()


@then('New Arrivals option list is displayed')
def verify_new_arrival_options_appear(context):
    context.app.product_page.verify_new_arrival_options_appear()