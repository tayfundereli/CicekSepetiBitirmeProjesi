from behave import step


@step('Login sayfasina gidilir')
def step_impl(context):
    context.home_page.navigate("https://www.mizu.com/en-mx/login")


@step('Email ve password alani doldurulur')
def step_impl(context):
    context.login_page.fill_email("ranome8393@reamtv.com")
    context.login_page.fill_password("ranome8393")


@step('Sign in butonuna tiklanir')
def step_impl(context):
    context.login_page.click_submit()


@step('Pop-up kapatilir')
def step_impl(context):
    context.home_page.close_popup()


@step('Giris yapildigi kontrol edilir')
def step_impl(context):
    context.home_page.control_login()
