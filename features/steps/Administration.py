from AdminUITests.Config.Config import Config as cf
from AdminUITests.Common.Browser import Browser as browser
from behave import Given,When,Then
import pdb
from time import sleep
class Administration:

    @Given('I have language set as English')
    def step(context):
        browser.visit(browser)
        browser.click_by_class(browser, "lang_en")
        browser.assert_by_cssselector(browser, "div.login-button", "LOG IN")

    @When('I type correct "user"')
    def step(context):
        browser.type_in_text_id(browser, "tbUsername", "smahajan935")

    @When('I type correct "password"')
    def step(context):
        browser.type_in_text_name(browser, "tbPassword", "password")

    @When('I click on login')
    def step(context):
        browser.click_by_css(browser, "div.login-button")

    @Then('I can see my "role"')
    def step(context):
        browser.assert_by_cssselector(browser,"span.dispatcher-userType.ng-binding", "Administrator")

    @Given('I am on homepage')
    def step(context):
        browser.assert_by_cssselector(browser,"span.dispatcher-userType.ng-binding", "Administrator")

    @When('I click on Admin Tab')
    def step(context):
        browser.click_on_link_text(browser,"ADMINISTRATION")

    @Then("I can see Admin Overview")
    def steps(context):
        browser.assert_by_cssselector(browser,".leftDiv.ng-binding","Overview")

    @Given("I am on admin tab")
    def step(context):
        browser.click_on_link_text(browser,"FLEET VIEW")
        browser.click_on_link_text(browser,"ADMINISTRATION")

    @When("I search for Invalid User")
    def step(context):
        browser.type_in_text_css(browser,"input.search-text","abcdef")
        browser.enter_return_key(browser,"input.search-text")

    @Then("I should be able to scroll and see Hardware")
    def step(context):
        browser.assert_view_state(browser,"li[ui-sref='admin.hardware.list']")

    @When("I search for a user by username and click on it")
    def step(context):
        browser.type_in_text_css(browser,"input.search-text","ttest_lastname578")
        browser.enter_return_key(browser,"input.search-text")
        sleep(2)
        browser.click_by_css(browser,"tr.table-tr")

    @When("I suspend the user")
    def step(context):
        browser.click_by_css(browser,"div.options")
        browser.click_on_link_text(browser, "Suspend User")
        browser.click_by_css(browser, "div.orange-gradient-button")

    @When("I unsuspend the user")
    def step(context):
        browser.click_by_css(browser,"div.options")
        browser.click_on_link_text(browser, "Unsuspend User")
        browser.click_by_css(browser, "div.blue-gradient-button")

    @Then("I can see user active")
    def step(context):
        browser.assert_by_cssselector(browser,"span.text.ng-binding","active")

    @Given("I am on active Emergency Center")
    def step(context):
        browser.click_on_link_text(browser, "EMERGENCY CENTER")
        browser.click_on_link_text(browser, "ACTIVE")



