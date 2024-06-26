from behave import given, when, then



@given('Open Help page for Technical Support')
def open_target_help_returns(context):
    context.app.help_page.open_help_technical_support()

#@given('Open Help page for Returns')
#def open_target_help_returns(context):
    #context.app.help_page.open_help_returns()


@when('Select Help topic {option}')
def select_topic(context, option):
    context.app.help_page.select_topic(option)


# @then('Verify Current promotions page opened')
# def verify_promotions_opened(context):
#     context.app.help_page.verify_promotions_header()
#
#
# @then('Verify Returns page opened')
# def verify_returns_opened(context):
#     context.app.help_page.verify_returns_header()


#@then('Verify help {header} page opened')
#def verify_help_page_header(context, header):
 #   context.app.help_page.verify_header(header)

@then('Verify help {header} page opened')
def verify_help_page_header(context, header):
    if header == 'Technical Support':
        context.app.help_page.verify_technical_support_header()
    elif header == 'Target GiftCard balance':
        context.app.help_page.verify_giftcards_header()
    else:
        raise ValueError(f"Header '{header}' not recognized.")
