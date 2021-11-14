from jedi import settings
settings.case_insensitive_completion = True


import NXOpen
session = NXOpen.Session.GetSession()
lw = session.ListingWindow
lw.Open()
lw.WriteLine('Hello Open Python! python nx 二次开发')     
