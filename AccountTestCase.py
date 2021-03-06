# -*- coding: UTF-8 -*-
import logging

import config
from StoreBase import StoreBase
from selenium.webdriver.common.by import By
from LoginFlowTestCase import LoginFlowNavigationLocators

# configuration
logger = logging.getLogger(__name__)
cfg = config.get_common_configs()

user_profile_info = cfg['name'] + " " + cfg['last_name']


class AccountLocators:
    PAGE_HEADER = (By.XPATH, "//*[contains(@class, 'page-heading')]")
    ACCOUNT_INFO = (By.CSS_SELECTOR, ".info-account")
    BREADCRUMB = (By.XPATH, "//*[contains(@class, 'navigation_page')]")
    ACCOUNT_USER_INFO = (By.CSS_SELECTOR, "nav .header_user_info .account")
    SIGNOUT = (By.CSS_SELECTOR, ".logout")
    ACCOUNT_MENU = (By.CSS_SELECTOR, ".myaccount-link-list span")


class AccountLexemes:
    ACCOUNT_HEADER = 'MY ACCOUNT'
    ACCOUNT_INFO = 'Welcome to your account. Here you can manage all of your personal information and orders.'


class AccountHelper(StoreBase):

    def __init__(self, driver):
        super().__init__(driver)

    def verify_my_account_page(self, case):
        self.wait_for_page_load(LoginFlowNavigationLocators.LOGIN_ACCOUNT_BOX)
        self.wait_for_page_load(LoginFlowNavigationLocators.ACCOUNT_CREATION_FORM)
        assert AccountLexemes.ACCOUNT_HEADER == self.find_element(AccountLocators.PAGE_HEADER).text
        assert AccountLexemes.ACCOUNT_INFO == self.find_element(AccountLocators.ACCOUNT_INFO).text
        if case == 'creation':
            assert user_profile_info == self.find_element(AccountLocators.ACCOUNT_USER_INFO).text
        if case == 'signin':
            assert cfg['user_info'] == self.find_element(AccountLocators.ACCOUNT_USER_INFO).text
        assert len(self.find_elements(AccountLocators.ACCOUNT_MENU)) == 5
        logger.info('my_account page %s is loaded' % self.get_current_url())

    def sign_out(self):
        self.find_element(AccountLocators.SIGNOUT)
        self.click_element(AccountLocators.SIGNOUT)
        assert self.base_url in self.get_current_url()
        logger.info('sign_in page %s is loaded' % self.get_current_url())
