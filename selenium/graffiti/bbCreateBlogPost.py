#!/usr/bin/env python

import sys, unittest, time, re

sys.path.append('../..')
import common.monotesting as mono
from selenium.graffiti.graffitiTestCase import graffitiTestCase

class graffiti_bb_CreateBlogPost(graffitiTestCase):
    graffitiTestCaseId = 662404
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
            sel.type("//*[@id=\"ctl00_MainRegion_txtTitle\"]", "Cras tristique, enim ac ornare facilisis, ante justo euismod urna; ac varius nisl libero sed velit?")
            sel.select("ctl00_MainRegion_CategoryList", "label=Blog")
            sel.type("ctl00$MainRegion$txtContent", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut massa ut augue bibendum tempor ut a mauris. Duis quam arcu, euismod eu viverra sit amet, sollicitudin vel est. Fusce ultricies, enim vitae porta hendrerit, magna nisi porta erat, eu volutpat purus enim in purus. Phasellus aliquam sodales interdum. Integer commodo purus in metus adipiscing sit amet commodo nisi convallis. Nam eleifend, ipsum id posuere malesuada; velit arcu lacinia leo, eu feugiat augue enim vel nulla. Integer mollis orci nec dui euismod in varius ante euismod. Ut at sem nibh. Sed tempor suscipit lorem id faucibus. Morbi faucibus tristique sem ac pulvinar! Fusce id erat diam; id molestie leo? Sed non nibh at neque venenatis vestibulum. Suspendisse iaculis nunc vel nisi dignissim feugiat! Fusce suscipit ligula id diam feugiat sit amet volutpat risus hendrerit. Nullam sapien neque, elementum et vehicula ac, sodales ac odio! Morbi quam diam, pretium eget porta id, sodales eu nulla.\n\nPhasellus blandit risus sed sem porta ultrices. Suspendisse at risus non nisl congue consequat. Praesent sollicitudin luctus tortor, sit amet pharetra justo malesuada non. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ut gravida diam. Curabitur eget lobortis quam. Aliquam quis auctor lacus. Phasellus malesuada aliquet nulla; sed molestie orci fringilla ac. Maecenas quis justo felis, sit amet blandit diam. Nunc diam erat, varius eu bibendum eget, ullamcorper id orci. Maecenas id nunc purus; eu euismod elit! Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec ultrices, lacus a placerat imperdiet, sem risus aliquam dui, non molestie leo nunc non ligula.\n\nCras ac consectetur leo. Nullam at dui felis. Phasellus et quam neque; a pretium quam! Cras pharetra est in odio tempus faucibus. Aenean luctus, urna euismod luctus luctus, ipsum massa tincidunt lectus, a congue dui justo at ligula. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam sed neque enim. Proin fringilla dapibus lorem vitae imperdiet. Ut quis interdum eros. Proin pellentesque, ligula in iaculis elementum, lorem risus convallis nisi, a tristique augue nisl vel dolor. Aenean ipsum lacus, tempor vel mattis a, mollis sit amet magna.")
            sel.click("ctl00_MainRegion_Publish_Button")
            sel.wait_for_page_to_load("30000")
            self.failUnless(sel.is_text_present("exact:Cras tristique, enim ac ornare facilisis, ante justo euismod urna; ac varius nisl libero sed velit?"))
            self.failUnless(sel.is_text_present("By mono user on"))
            sel.click("link=Log Off")
    
        except Exception,e:
            self.verificationErrors.append(str(e))


if __name__ == "__main__":
    mono.monotesting_main()
