from behave import step


@step('Anasayfaya gidilir')
def step_impl(context):
    context.home_page.navigate("https://www.mizu.com/en-mx/")


@step('Menu altindaki tum linkler gezilir')
def step_impl(context):
    context.home_page.count_links()


@step('Kirik link olup olmadigi kontrol edilir')
def step_impl(context):
    context.home_page.control_links()
