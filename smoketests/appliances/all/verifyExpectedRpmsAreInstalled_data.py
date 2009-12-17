#!/usr/bin/env python

# These are the rpms that are expected to be there on the Mono appliance
monoExpectedRpms = [
                    "mono-addins",
                    "mono-zeroconf",
                    "mono-zeroconf-doc",
                    "mono-zeroconf-provider-avahi",
                    "mono-tools",
                    "mono-winfxcore",
       # --------------------------------------------
                    "Mono_ASP.NET_MonoForums",
                    "Mono_ASP.NET_ClubWebSite",
                    "Mono_ASP.NET_ClassifiedsStarterKit",
                    "Mono_ASP.NET_BlogStarterKit",
       # --------------------------------------------
                    "monodevelop",
                    "monodevelop-boo",
                    "monodevelop-database",
                    "monodevelop-debugger-gdb",
                    "monodevelop-debugger-mdb",
                    "monodevelop-java",
                    "monodevelop-vala",
       # --------------------------------------------
                    "mono-uia",
                    "uiaatkbridge",
                    "uiautomationwinforms",
       # --------------------------------------------
                    "vte016-sharp",
                    "gtkhtml314-sharp",
                    "gnome-sharp2-complete",
                    "gnome-print-sharp",
                    "gnome-desktop-sharp2",
                    "taglib-sharp",
                    "rsvg2-sharp",
                    "gtk-sharp2-complete",
                    "gtk-sharp2-gapi",
                    "gnome-keyring-sharp",
                    "gtksourceview-sharp2",
                    "nautilusburn-sharp",
                    "gtk-sharp2-doc",
                    "evolution-sharp",
                    "notify-sharp",
                    "wnck-sharp",
                    "gtksourceview2-sharp",
       # --------------------------------------------
                    "IPCE",
                    "boo",
                    "boo-devel",
                    "ikvm",
                    "nant",
                    "ndesk-dbus-glib-devel",
                   ]

# These are the rpms that are expected to be there on the MonoVS appliance
monoVSExpectedRpms = []

# These are the rpms that are expected to be there on all appliances
expectedRpms = [
                    "mono-core",
                    "mono-devel",
                    "mono-debugger",
                    "mono-nunit",
                    "mono-locale-extras",
                    "mono-complete",
                    "mono-extras",
                    "monodoc-core",
                    "mono-wcf",
                    "mono-jscript",
                    "mono-check",
                    "mono-basic",
                    "libgluezilla0",
                    "webkit-sharp",
                    "monovs-server",
                    "monovs-server-gui",
       # --------------------------------------------
                    "mono-winforms",
                    "libgdiplus0",
       # --------------------------------------------
                    "mono-web",
                    "apache2-mod_mono",
       # --------------------------------------------
                    "mono-data",
                    "mono-data-oracle",
                    "mono-data-sqlite",
                    "mono-data-postgresql",
                    "mono-data-sybase",
                    "mono-data-firebird",
                    "bytefx-data-mysql",
                    "ibm-data-db2",
       # --------------------------------------------
                    "gmime-sharp",
                    "gtk-sharp2",
                    "gnome-vfs-sharp2",
                    "glade-sharp2",
                    "gnome-sharp2",
                    "gnome-panel-sharp",
                    "glib-sharp2",
                    "art-sharp2",
                    "gconf-sharp2",
       # --------------------------------------------
                    "ndesk-dbus",
                    "ndesk-dbus-glib",
                    "xsp",
                    "samba",
                    ]


# vim:ts=4:expandtab:
