"""
前提条件：python版本和PF提供的API版本一致，路径已经添加到系统路径
"""
import sys
print(sys.path)
#加入PF python 搜索路径
sys.path.append("C:\\Program Files\\DIgSILENT\\PowerFactory 2023 SP5\\Python\\3.11")
print(sys.path)

if __name__=="__main__":    #必须加，否则进程不会自己结束，只能调用一次模块
    import powerfactory as pf
    print(pf.__file__)
    #返回一个PF对象
    app=pf.GetApplication()
    print(app)
    #激活工程
    project=app.ActivateProject('39 Bus New England System')
    #激活算例
    ldf=app.GetFromStudyCase("ComLdf")
    ldf.iopt_net=0
    #执行
    ldf.Execute()
    #搜索所有支路并打印
    terminals=app.GetCalcRelevantObjects("*.ElmTerm")
    for terminal in terminals:
        voltage=terminal.GetAttribute("m:u")
        print("Voltage at terminal %s is %f p.u."%(terminal,voltage))