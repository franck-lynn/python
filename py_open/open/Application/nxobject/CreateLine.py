
import NXOpen
import NXOpen_UF


def cteateLine():
    try:
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        lw = theSession.ListingWindow
        lw.Open()
        lw.WriteLine("当前部件名称---> " + workPart.Name)

        line1 = workPart.Curves.CreateLine(
            NXOpen.Point3d(0.0, 0.0, 0.0),
            NXOpen.Point3d(1.5, 2.5, 7.0)
        )
    except Exception as ex:
        raise ex
