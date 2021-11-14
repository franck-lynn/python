#nx: threaded
# 使用 numpy 第3方库时要加上上面这句, 不然会非常非常卡顿
import numpy as np
import NXOpen
# import NXOpen_UF

def main():
    try:
        theSession = NXOpen.Session.GetSession()
        # theUfSession = NXOpen_UF.UFSession.GetUFSession()
        # NXOpen.UI.GetUI()

        lw = theSession.ListingWindow
        lw.Open()
        
        workPart = theSession.Parts.Work
        # lw.WriteLine("当前工作部件名称---> " + workPart.Name )
        # lw.WriteLine("当前工作部件名称路径---> " + workPart.FullPath )
        # lw.WriteLine("当前工作部件单位---> " + str(workPart.PartUnits) )
        
        lw.WriteLine("输出工作部件的用户属性列表:" )
        
        bodies = workPart.Bodies 
        # lw.WriteLine(str(type(bodies))) # <class 'NXOpen.BodyCollection'>
        # lw.WriteLine(str(dir(bodies))) # <class 'NXOpen.BodyCollection'>
        # lw.WriteLine(str(iter(bodies))) # <NXOpen._CollectionIterator object at 0x000001BEADDE1AB0>
        
        for aBody in iter(bodies):
            # lw.WriteLine(str(type(aBody))) # <class 'NXOpen.Body'>
            attributes = aBody.GetUserAttributes()
            # lw.WriteLine("返回的类型: " + str(type(attributes)))  # 返回的是一个 list
            # lw.WriteLine(str(attributes))
            # ! 只能获取自定义的属性, 需要设置属性后才能获取
            lw.WriteLine("密度---> " + str(aBody.Density))
            for attr in attributes:
                lw.WriteLine(str(attr.Title)  + "= " + attr.StringValue)
        
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
    pass
