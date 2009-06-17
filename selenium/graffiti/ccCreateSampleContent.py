#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../..')
import common.monotesting as mono
from selenium.graffiti.graffitiTestCase import graffitiTestCase

class graffiti_cc_CreateSampleContent(graffitiTestCase):
    graffitiTestCaseId = 662403
    def test(self):
        if not self.canRun:
            return
        try:
            sel = self.selenium
            sel.open("/")
            sel.click("link=Login")
            sel.wait_for_page_to_load("30000")
            sel.type("UserName", "mono user")
            sel.type("Password", "mono")
            sel.click("login")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Write")
            sel.wait_for_page_to_load("30000")
            sel.type("//*[@id=\"ctl00_MainRegion_txtTitle\"]", "Pellentesque tempus mollis pharetra. Etiam blandit risus augue, eget venenatis elit?")
            sel.select("ctl00_MainRegion_CategoryList", "label=Sample Content")
            sel.type("ctl00$MainRegion$txtContent", "Praesent at nisl eu dui imperdiet euismod a nec ligula. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Praesent molestie est sit amet odio ultricies sodales. Pellentesque pharetra, enim eget tristique tempus, massa neque hendrerit tortor; eu sollicitudin elit mi nec risus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac mi ante, in iaculis est. Etiam fringilla, libero consequat ullamcorper rutrum; ligula mauris lobortis erat, id rutrum ligula massa nec nisi. Maecenas semper; quam eu vulputate egestas, sapien nisi aliquet mauris; ac tincidunt turpis dui egestas nulla. Phasellus nibh sem, commodo a ullamcorper eget, pulvinar vitae dolor. Quisque scelerisque odio dapibus leo semper ullamcorper vulputate tellus malesuada. In at nibh mauris. Proin commodo tempor ante, eu adipiscing orci dapibus vel. Morbi massa risus, consequat eu interdum at; iaculis at diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In hac habitasse platea dictumst.  Cras imperdiet, tortor vel feugiat commodo, lacus nisi aliquam ante; nec rutrum nunc ante nec nulla. Aliquam fermentum purus varius lacus viverra at imperdiet enim tincidunt. Aenean mi elit, ullamcorper quis faucibus ac, dignissim quis erat. Aenean tempor facilisis quam, eu posuere ante egestas id. Morbi in ligula velit. Aliquam erat libero, iaculis bibendum volutpat eu; blandit at erat. Quisque neque elit, vestibulum eget vulputate eget, faucibus eget urna. Nunc malesuada purus id nulla egestas adipiscing. Nam hendrerit elementum commodo. Nullam tristique, mauris sed tincidunt molestie, orci nisl sollicitudin ligula, ac elementum erat magna in leo. Fusce in lectus a libero dapibus sodales at varius urna. Phasellus blandit mattis quam quis aliquet? Nulla vulputate iaculis turpis, a luctus justo ultricies quis. Sed aliquet purus non dolor interdum fermentum. Nullam pulvinar leo eu arcu consequat sollicitudin. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eleifend lorem nulla, et cursus enim? Duis non varius ipsum. Curabitur purus lorem, molestie et blandit id, tempor vitae ante.  Quisque facilisis vehicula ornare. Maecenas nec augue dolor. Proin nec condimentum enim. Donec dignissim congue blandit. Nulla porttitor adipiscing metus, vel placerat elit dictum eget. Pellentesque mattis lectus a velit sagittis aliquam accumsan enim adipiscing. Proin non erat diam, nec bibendum felis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Pellentesque in mollis mi. Integer congue; eros in convallis porttitor, augue nisl porta leo, ac accumsan sem dui vel eros. Phasellus tincidunt rhoncus cursus. Morbi magna lacus, vulputate interdum elementum sed, porttitor et urna. Aenean iaculis leo vel diam congue sit amet malesuada ligula viverra. Nulla tellus metus, pellentesque vitae hendrerit ut, cursus sed nisi.")
            sel.click("ctl00_MainRegion_Publish_Button")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("exact:Pellentesque tempus mollis pharetra. Etiam blandit risus augue, eget venenatis elit?"))
            self.failUnless(sel.is_text_present("By mono user on"))
            sel.click("link=Log Off")
        
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
