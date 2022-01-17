from time import sleep
from behave import step


@step('Flowers kategorisine gidilir')
def step_impl(context):
    context.category_page.navigate("https://www.mizu.com/flowers")


@step('Ilk sayfada 60 urun oldugu kontrol edilir')
def step_impl(context):
    context.category_page.getProductCount(1)
    sleep(1)


@step('Sayfa 10 kez scroll edilerek her sayfada 60 urun oldugu kontrol edilir')
def step_impl(context):
    context.category_page.makeScrollBehaviourSmooth()
    context.category_page.scrollPageTenTimes()
