class parameter:
    
    # ����ZYNQ�����ѳ������ݻش�����λ��
    remoteAddr_image = ("192.168.137.100", 9999) # ("127.0.0.1", 9999)  ("192.168.0.35", 9999)
    localAddr_image = ("192.168.137.1", 10000)
    # ������λ����ZYNQ���Ϳ����ź�
    remoteAddr_ctrl = ("192.168.137.100", 8889)
    localAddr_ctrl = ("192.168.137.1", 8888)
    # ������λ����ZYNQ���͹ر��ź�
    remoteAddr_close = ("192.168.137.100", 8001)
    localAddr_close = ("192.168.137.1", 8000)

    # remoteAddr_image = ("127.0.0.1", 9999) # ("127.0.0.1", 9999)  ("192.168.0.35", 9999)
    # localAddr_image = ("127.0.0.1", 10000)
    # # ������λ����ZYNQ���Ϳ����ź�
    # remoteAddr_ctrl = ("127.0.0.1", 8889)
    # localAddr_ctrl = ("127.0.0.1", 8888)
    # ������λ����ZYNQ���͹ر��ź�
    # remoteAddr_close = ("127.0.0.1", 8001)
    # localAddr_close = ("127.0.0.1", 8000)

    bytes_perImage = 1     # 1: uint8      4: float32
    
    numRow = 200 #200  #800
    numCol = 336 #336  #1024 
    send_bytes_max = 200*12  #  #8192
    numPoints = numRow * numCol

    def __init__(self):
        # # ��ȡ��ǰ�ű���main.py����·��
        # current_file_path = os.path.abspath(__file__)
        
        # # ��ȡ��ǰ�ű����ڵ�Ŀ¼
        # outpath = os.path.dirname(current_file_path)
        self.prf = 30  # Hz
        self.B = 10 # GHz
        self.fc = 121 # GHz
        self.T = 315e-6*1000 # ms

    def rstParameter(self):
        self.prf = 30  # Hz
        self.B = 10 # GHz
        self.fc = 121 # GHz
        self.T = 315e-6*1000 # ms