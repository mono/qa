#!/usr/bin/env python

import sys, unittest, time, re, random

sys.path.append('../../..')
import common.monotesting as mono
from selenium.xsp1.xsp1TestCase import xsp1TestCase

class WebControls_WebDataGridCommand(xsp1TestCase):
    xsp1TestCaseId = 839926
    xsp2TestCaseId = 861806
    xsp4TestCaseId = None

    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=web_datagrid_command")
            sel.wait_for_page_to_load("30000")
            self._setCountries()
            self._checkCountryList()

            self._removeCountriesAlwaysFromFirstSpotTest()
            self._resetWebPage()
            self._removeCountriesAtRandomTest()
            self._resetWebPage()
            self._removeCountriesAlwaysFromLastSpotTest()

        except Exception,e:
            self.verificationErrors.append(str(e))

    def _setCountries(self):
        self.countries = { "Spain":2, "Japan":3, "Austria":4, "France":5, "Great Britain":6, "Italia":7, "India":8, "Brazil":9, "Germany":10, "Mexico":11 }

    def _removeCountriesAtRandomTest(self):
        for ix in range(len(self.countries)):
            country = self.countries.keys()[random.randint(0,len(self.countries) - 1)]
            self._removeCountry(country)
            self._checkCountryList()

    def _removeCountriesAlwaysFromFirstSpotTest(self):
        for ix in range(len(self.countries)):
            countryIdx = 2
            country = self.selenium.get_text("//table[@id='dg']/tbody/tr[" + str(countryIdx) + "]/td[2]")
            self._removeCountry(country)
            self._checkCountryList()

    def _removeCountriesAlwaysFromLastSpotTest(self):
        for ix in range(len(self.countries)):
            countryIdx = len(self.countries) + 1
            country = self.selenium.get_text("//table[@id='dg']/tbody/tr[" + str(countryIdx) + "]/td[2]")
            self._removeCountry(country)
            self._checkCountryList()

    def _resetWebPage(self):
        self.selenium.open("/")
        self.selenium.wait_for_page_to_load("30000")
        self.selenium.click("link=web_datagrid_command")
        self.selenium.wait_for_page_to_load("30000")
        self._setCountries()
        self._checkCountryList()

    def _checkCountryList(self):
        for country in self.countries:
            if self.countries[country] != -1:
                #print country + ":" + str(self.countries[country]) + ":" + self.selenium.get_text("//table[@id='dg']/tbody/tr[" + str(self.countries[country]) + "]/td[2]")
                self.assertEqual(country, self.selenium.get_text("//table[@id='dg']/tbody/tr[" + str(self.countries[country]) + "]/td[2]"))
        #print

    def _removeCountry(self, country):
        self.selenium.click("//html/body/form/table/tbody/tr[" + str(self.countries[country]) + "]/td/a")
        self.selenium.wait_for_page_to_load("30000")
        for curCountry in self.countries:
            if self.countries[curCountry] > self.countries[country]:
                self.countries[curCountry] -= 1
        del self.countries[country]

if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
