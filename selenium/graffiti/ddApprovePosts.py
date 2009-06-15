#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../..')
import common.monotesting as mono
from selenium.graffiti.graffitiTestCase import graffitiTestCase

class graffiti_dd_ApprovePosts(graffitiTestCase):

    graffitiTestCaseId = None
    def test(self):
        if not self.canRun:
            return
        try:

            sel = self.selenium
            sel.open("/")
            sel.click("link=Login")
            sel.wait_for_page_to_load("30000")
            sel.type("UserName", "admin")
            sel.type("Password", "mono")
            sel.click("login")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Posts")
            sel.wait_for_page_to_load("30000")
            sel.click("//html/body/div/form/div[3]/div/div/div/div/div[2]/a")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Pellentesque tempus mollis pharetra. Etiam blandit risus augue, eget venenatis elit?")
            sel.wait_for_page_to_load("30000")
            sel.click("//div[@id='ctl00_MainRegion_TabbedPanes1_TabSet']/div/table/tbody/tr/td[2]/div")
            sel.click("ctl00_MainRegion_HomeSortOverride")
            sel.click("ctl00_MainRegion_Publish_Button")
            sel.wait_for_page_to_load("30000")
            sel.click("//html/body/div/form/div[3]/div/div/div/div/div[2]/a")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Cras tristique, enim ac ornare facilisis, ante justo euismod urna; ac varius nisl libero sed velit?")
            sel.wait_for_page_to_load("30000")
            sel.click("//div[@id='ctl00_MainRegion_TabbedPanes1_TabSet']/div/table/tbody/tr/td[2]/div")
            sel.click("ctl00_MainRegion_HomeSortOverride")
            sel.click("ctl00_MainRegion_Publish_Button")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Go back to site")
            sel.wait_for_page_to_load("30000")
            sel.click("//div[@id='navigation']/ol/li[2]/a/span")
            sel.wait_for_page_to_load("30000")
            self.failUnless(re.search(r"^Pellentesque tempus mollis pharetra. Etiam blandit risus augue, eget venenatis elit[\s\S]$", sel.get_text("link=exact:Pellentesque tempus mollis pharetra. Etiam blandit risus augue, eget venenatis elit?")))
            sel.click("link=exact:Pellentesque tempus mollis pharetra. Etiam blandit risus augue, eget venenatis elit?")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("exact:Praesent at nisl eu dui imperdiet euismod a nec ligula. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Praesent molestie est sit amet odio ultricies sodales. Pellentesque pharetra, enim eget tristique tempus, massa neque hendrerit tortor; eu sollicitudin elit mi nec risus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac mi ante, in iaculis est. Etiam fringilla, libero consequat ullamcorper rutrum; ligula mauris lobortis erat, id rutrum ligula massa nec nisi. Maecenas semper; quam eu vulputate egestas, sapien nisi aliquet mauris; ac tincidunt turpis dui egestas nulla. Phasellus nibh sem, commodo a ullamcorper eget, pulvinar vitae dolor. Quisque scelerisque odio dapibus leo semper ullamcorper vulputate tellus malesuada. In at nibh mauris. Proin commodo tempor ante, eu adipiscing orci dapibus vel. Morbi massa risus, consequat eu interdum at; iaculis at diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In hac habitasse platea dictumst. Cras imperdiet, tortor vel feugiat commodo, lacus nisi aliquam ante; nec rutrum nunc ante nec nulla. Aliquam fermentum purus varius lacus viverra at imperdiet enim tincidunt. Aenean mi elit, ullamcorper quis faucibus ac, dignissim quis erat. Aenean tempor facilisis quam, eu posuere ante egestas id. Morbi in ligula velit. Aliquam erat libero, iaculis bibendum volutpat eu; blandit at erat. Quisque neque elit, vestibulum eget vulputate eget, faucibus eget urna. Nunc malesuada purus id nulla egestas adipiscing. Nam hendrerit elementum commodo. Nullam tristique, mauris sed tincidunt molestie, orci nisl sollicitudin ligula, ac elementum erat magna in leo. Fusce in lectus a libero dapibus sodales at varius urna. Phasellus blandit mattis quam quis aliquet? Nulla vulputate iaculis turpis, a luctus justo ultricies quis. Sed aliquet purus non dolor interdum fermentum. Nullam pulvinar leo eu arcu consequat sollicitudin. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse eleifend lorem nulla, et cursus enim? Duis non varius ipsum. Curabitur purus lorem, molestie et blandit id, tempor vitae ante. Quisque facilisis vehicula ornare. Maecenas nec augue dolor. Proin nec condimentum enim. Donec dignissim congue blandit. Nulla porttitor adipiscing metus, vel placerat elit dictum eget. Pellentesque mattis lectus a velit sagittis aliquam accumsan enim adipiscing. Proin non erat diam, nec bibendum felis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Pellentesque in mollis mi. Integer congue; eros in convallis porttitor, augue nisl porta leo, ac accumsan sem dui vel eros. Phasellus tincidunt rhoncus cursus. Morbi magna lacus, vulputate interdum elementum sed, porttitor et urna. Aenean iaculis leo vel diam congue sit amet malesuada ligula viverra. Nulla tellus metus, pellentesque vitae hendrerit ut, cursus sed nisi."))
            sel.click("//div[@id='navigation']/ol/li[3]/a/span")
            sel.wait_for_page_to_load("30000")
            self.failUnless(re.search(r"^Cras tristique, enim ac ornare facilisis, ante justo euismod urna; ac varius nisl libero sed velit[\s\S]$", sel.get_text("link=exact:Cras tristique, enim ac ornare facilisis, ante justo euismod urna; ac varius nisl libero sed velit?")))
            sel.click("link=exact:Cras tristique, enim ac ornare facilisis, ante justo euismod urna; ac varius nisl libero sed velit?")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("exact:Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut massa ut augue bibendum tempor ut a mauris. Duis quam arcu, euismod eu viverra sit amet, sollicitudin vel est. Fusce ultricies, enim vitae porta hendrerit, magna nisi porta erat, eu volutpat purus enim in purus. Phasellus aliquam sodales interdum. Integer commodo purus in metus adipiscing sit amet commodo nisi convallis. Nam eleifend, ipsum id posuere malesuada; velit arcu lacinia leo, eu feugiat augue enim vel nulla. Integer mollis orci nec dui euismod in varius ante euismod. Ut at sem nibh. Sed tempor suscipit lorem id faucibus. Morbi faucibus tristique sem ac pulvinar! Fusce id erat diam; id molestie leo? Sed non nibh at neque venenatis vestibulum. Suspendisse iaculis nunc vel nisi dignissim feugiat! Fusce suscipit ligula id diam feugiat sit amet volutpat risus hendrerit. Nullam sapien neque, elementum et vehicula ac, sodales ac odio! Morbi quam diam, pretium eget porta id, sodales eu nulla. Phasellus blandit risus sed sem porta ultrices. Suspendisse at risus non nisl congue consequat. Praesent sollicitudin luctus tortor, sit amet pharetra justo malesuada non. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ut gravida diam. Curabitur eget lobortis quam. Aliquam quis auctor lacus. Phasellus malesuada aliquet nulla; sed molestie orci fringilla ac. Maecenas quis justo felis, sit amet blandit diam. Nunc diam erat, varius eu bibendum eget, ullamcorper id orci. Maecenas id nunc purus; eu euismod elit! Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec ultrices, lacus a placerat imperdiet, sem risus aliquam dui, non molestie leo nunc non ligula. Cras ac consectetur leo. Nullam at dui felis. Phasellus et quam neque; a pretium quam! Cras pharetra est in odio tempus faucibus. Aenean luctus, urna euismod luctus luctus, ipsum massa tincidunt lectus, a congue dui justo at ligula. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam sed neque enim. Proin fringilla dapibus lorem vitae imperdiet. Ut quis interdum eros. Proin pellentesque, ligula in iaculis elementum, lorem risus convallis nisi, a tristique augue nisl vel dolor. Aenean ipsum lacus, tempor vel mattis a, mollis sit amet magna."))
            sel.click("link=Control Panel")
            sel.wait_for_page_to_load("30000")
            sel.click("link=Log Off")
            sel.wait_for_page_to_load("30000")

        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()


# vim:ts=4:expandtab:
