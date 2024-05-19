def _ini():
    global _global_dict
    _global_dict = {}

def set_value(key,val):
    _global_dict[key] = val

def get_val(key):
    try:
        return _global_dict[key]
    except:
        print('读取'+key+'失败\r\n')

'''
    globalVAR.set_value('AxleSpeed_1',0)
    globalVAR.set_value('AxleSpeed_2', 0)
    globalVAR.set_value('AxleSpeed_3', 0)
    globalVAR.set_value('AxleSpeed_4', 0)

    globalVAR.set_value('D111', Ddata())
    globalVAR.set_value('D112', Ddata())
    globalVAR.set_value('D121', Ddata())
    globalVAR.set_value('D122', Ddata())
    globalVAR.set_value('D131', Ddata())
    globalVAR.set_value('D132', Ddata())
    globalVAR.set_value('D141', Ddata())
    globalVAR.set_value('D142', Ddata())

    globalVAR.set_value('D103', Ddata())
    globalVAR.set_value('D104', Ddata())
    globalVAR.set_value('D105', Ddata())
    globalVAR.set_value('D106', Ddata())
    globalVAR.set_value('D107', Ddata())
    globalVAR.set_value('D108', Ddata())
    globalVAR.set_value('D109', Ddata())
    globalVAR.set_value('D110', Ddata())

    globalVAR.set_value('D401', Ddata())
    globalVAR.set_value('D402', Ddata())
    globalVAR.set_value('D403', Ddata())

    globalVAR.set_value('BZ1EN', Ddata())
    globalVAR.set_value('BZ2EN', Ddata())
    globalVAR.set_value('BZ3EN', Ddata())
    globalVAR.set_value('BZ4EN', Ddata())

    AxleSpeed_1 = 0
    AxleSpeed_2 = 0
    AxleSpeed_3 = 0
    AxleSpeed_4 = 0

    D111 = Ddata()
    D112 = Ddata()
    D121 = Ddata()
    D122 = Ddata()
    D131 = Ddata()
    D132 = Ddata()
    D141 = Ddata()
    D142 = Ddata()

    D103 = Ddata()
    D104 = Ddata()
    D105 = Ddata()
    D106 = Ddata()
    D107 = Ddata()
    D108 = Ddata()
    D109 = Ddata()
    D110 = Ddata()
    D401 = Ddata()
    D402 = Ddata()
    D403 = Ddata()

    BZ1EN = False
    BZ2EN = False
    BZ3EN = False
    BZ4EN = False

'''