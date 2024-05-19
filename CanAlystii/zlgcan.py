# -*- coding:utf-8 -*-
#  zlgcan.py
#
#  ~~~~~~~~~~~~
#
#  ZLGCAN API
#
#  ~~~~~~~~~~~~
#
#  ------------------------------------------------------------------
#  Author : guochuangjian    
#  Last change: 21.02.2019
#
#  Language: Python 2.7, 3.6
#  ------------------------------------------------------------------
#
import os
from ctypes import *
import platform
import threading
import time
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import globalVAR
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Ddata():
    ID = ''
    D1 = 0
    D2 = 0
    D3 = 0
    D4 = 0


ZCAN_DEVICE_TYPE = c_uint

INVALID_DEVICE_HANDLE = 0
INVALID_CHANNEL_HANDLE = 0

'''
 Device Type
'''
ZCAN_PCI5121 = ZCAN_DEVICE_TYPE(1)
ZCAN_PCI9810 = ZCAN_DEVICE_TYPE(2)
ZCAN_USBCAN1 = ZCAN_DEVICE_TYPE(3)
ZCAN_USBCAN2 = ZCAN_DEVICE_TYPE(4)
ZCAN_PCI9820 = ZCAN_DEVICE_TYPE(5)
ZCAN_CAN232 = ZCAN_DEVICE_TYPE(6)
ZCAN_PCI5110 = ZCAN_DEVICE_TYPE(7)
ZCAN_CANLITE = ZCAN_DEVICE_TYPE(8)
ZCAN_ISA9620 = ZCAN_DEVICE_TYPE(9)
ZCAN_ISA5420 = ZCAN_DEVICE_TYPE(10)
ZCAN_PC104CAN = ZCAN_DEVICE_TYPE(11)
ZCAN_CANETUDP = ZCAN_DEVICE_TYPE(12)
ZCAN_CANETE = ZCAN_DEVICE_TYPE(12)
ZCAN_DNP9810 = ZCAN_DEVICE_TYPE(13)
ZCAN_PCI9840 = ZCAN_DEVICE_TYPE(14)
ZCAN_PC104CAN2 = ZCAN_DEVICE_TYPE(15)
ZCAN_PCI9820I = ZCAN_DEVICE_TYPE(16)
ZCAN_CANETTCP = ZCAN_DEVICE_TYPE(17)
ZCAN_PCIE_9220 = ZCAN_DEVICE_TYPE(18)
ZCAN_PCI5010U = ZCAN_DEVICE_TYPE(19)
ZCAN_USBCAN_E_U = ZCAN_DEVICE_TYPE(20)
ZCAN_USBCAN_2E_U = ZCAN_DEVICE_TYPE(21)
ZCAN_PCI5020U = ZCAN_DEVICE_TYPE(22)
ZCAN_EG20T_CAN = ZCAN_DEVICE_TYPE(23)
ZCAN_PCIE9221 = ZCAN_DEVICE_TYPE(24)
ZCAN_WIFICAN_TCP = ZCAN_DEVICE_TYPE(25)
ZCAN_WIFICAN_UDP = ZCAN_DEVICE_TYPE(26)
ZCAN_PCIe9120 = ZCAN_DEVICE_TYPE(27)
ZCAN_PCIe9110 = ZCAN_DEVICE_TYPE(28)
ZCAN_PCIe9140 = ZCAN_DEVICE_TYPE(29)
ZCAN_USBCAN_4E_U = ZCAN_DEVICE_TYPE(31)
ZCAN_CANDTU_200UR = ZCAN_DEVICE_TYPE(32)
ZCAN_CANDTU_MINI = ZCAN_DEVICE_TYPE(33)
ZCAN_USBCAN_8E_U = ZCAN_DEVICE_TYPE(34)
ZCAN_CANREPLAY = ZCAN_DEVICE_TYPE(35)
ZCAN_CANDTU_NET = ZCAN_DEVICE_TYPE(36)
ZCAN_CANDTU_100UR = ZCAN_DEVICE_TYPE(37)
ZCAN_PCIE_CANFD_100U = ZCAN_DEVICE_TYPE(38)
ZCAN_PCIE_CANFD_200U = ZCAN_DEVICE_TYPE(39)
ZCAN_PCIE_CANFD_400U = ZCAN_DEVICE_TYPE(40)
ZCAN_USBCANFD_200U = ZCAN_DEVICE_TYPE(41)
ZCAN_USBCANFD_100U = ZCAN_DEVICE_TYPE(42)
ZCAN_USBCANFD_MINI = ZCAN_DEVICE_TYPE(43)
ZCAN_CANFDCOM_100IE = ZCAN_DEVICE_TYPE(44)
ZCAN_CANSCOPE = ZCAN_DEVICE_TYPE(45)
ZCAN_CLOUD = ZCAN_DEVICE_TYPE(46)
ZCAN_CANDTU_NET_400 = ZCAN_DEVICE_TYPE(47)
ZCAN_CANFDNET_200U_TCP = ZCAN_DEVICE_TYPE(48)
ZCAN_CANFDNET_200U_UDP = ZCAN_DEVICE_TYPE(49)
ZCAN_CANFDWIFI_100U_TCP = ZCAN_DEVICE_TYPE(50)
ZCAN_CANFDWIFI_100U_UDP = ZCAN_DEVICE_TYPE(51)
ZCAN_CANFDNET_400U_TCP = ZCAN_DEVICE_TYPE(52)
ZCAN_CANFDNET_400U_UDP = ZCAN_DEVICE_TYPE(53)
ZCAN_CANFDBLUE_200U = ZCAN_DEVICE_TYPE(54)
ZCAN_CANFDNET_100U_TCP = ZCAN_DEVICE_TYPE(55)
ZCAN_CANFDNET_100U_UDP = ZCAN_DEVICE_TYPE(56)
ZCAN_CANFDNET_800U_TCP = ZCAN_DEVICE_TYPE(57)
ZCAN_CANFDNET_800U_UDP = ZCAN_DEVICE_TYPE(58)
ZCAN_USBCANFD_800U = ZCAN_DEVICE_TYPE(59)
ZCAN_PCIE_CANFD_100U_EX = ZCAN_DEVICE_TYPE(60)
ZCAN_PCIE_CANFD_400U_EX = ZCAN_DEVICE_TYPE(61)
ZCAN_PCIE_CANFD_200U_MINI = ZCAN_DEVICE_TYPE(62)
ZCAN_PCIE_CANFD_200U_M2 = ZCAN_DEVICE_TYPE(63)
ZCAN_PCIE_CANFD_200U_EX = ZCAN_DEVICE_TYPE(62)
ZCAN_CANFDDTU_400_TCP = ZCAN_DEVICE_TYPE(64)
ZCAN_CANFDDTU_400_UDP = ZCAN_DEVICE_TYPE(65)
ZCAN_CANFDWIFI_200U_TCP = ZCAN_DEVICE_TYPE(66)
ZCAN_CANFDWIFI_200U_UDP = ZCAN_DEVICE_TYPE(67)
ZCAN_CANFDDTU_800ER_TCP = ZCAN_DEVICE_TYPE(68)
ZCAN_CANFDDTU_800ER_UDP = ZCAN_DEVICE_TYPE(69)
ZCAN_CANFDDTU_800EWGR_TCP = ZCAN_DEVICE_TYPE(70)
ZCAN_CANFDDTU_800EWGR_UDP = ZCAN_DEVICE_TYPE(71)
ZCAN_CANFDDTU_600EWGR_TCP = ZCAN_DEVICE_TYPE(72)
ZCAN_CANFDDTU_600EWGR_UDP = ZCAN_DEVICE_TYPE(73)
ZCAN_VIRTUAL_DEVICE = ZCAN_DEVICE_TYPE(99)

'''
 Interface return status
'''
ZCAN_STATUS_ERR = 0
ZCAN_STATUS_OK = 1
ZCAN_STATUS_ONLINE = 2
ZCAN_STATUS_OFFLINE = 3
ZCAN_STATUS_UNSUPPORTED = 4

'''
 CAN type
'''
ZCAN_TYPE_CAN = c_uint(0)
ZCAN_TYPE_CANFD = c_uint(1)

'''
 UI
'''

tab11l = [[sg.Frame(
    '监控参数',
    [

        [sg.Text('电机转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ1Rotor', expand_x=True)],
        [sg.Text('给定转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ1GivenRotor', expand_x=True)],
        [sg.Text('电枢电流( mA): ')] + [
            sg.Text("NULL", enable_events=False, key='GetBZ1RotorCurrent', expand_x=True, size=(5, 1))],
        [sg.Text('电机温度( ℃): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ1Temperature', expand_x=True)],
        [sg.Text('最大转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ1MAXS', expand_x=True)],
        [sg.Text('最小转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ1MINS', expand_x=True)],
        [sg.Text('1110播种电机速度低', key='A1110')] + [sg.Text('1111播种电机超速 ', key='A1111')],
    ])]]

tab11r = [[sg.Frame(
    '输入参数',
    [
        [sg.Checkbox(text='播种电机使能', enable_events=True, key='CheckBZ1')],
        [sg.Text('设置最大转速(RPM): ')] + [sg.Input(enable_events=True, key='SetBZ1MAXS')],
        [sg.Text('设置最小转速(RPM): ')] + [sg.Input(enable_events=True, key='SetBZ1MINS')],
        [sg.HorizontalSeparator()],
        [sg.Text('设置给定转速(RPM): ')] + [sg.Input(enable_events=True, key='SetBZ1GivenRotor')],
        # [sg.Text('滑块调节给定转速: ')] + [sg.Slider((0, 100), orientation='h', s=(40, 15), key='BZSlider',enable_events=True)],
        # [sg.Button('确定', key='BZButton')],
        # [sg.HorizontalSeparator()],

    ])]]

tab12l = [[sg.Frame(
    '监控参数',
    [

        [sg.Text('电机转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ2Rotor', expand_x=True)],
        [sg.Text('给定转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ2GivenRotor', expand_x=True)],
        [sg.Text('电枢电流( mA): ')] + [
            sg.Text("NULL", enable_events=False, key='GetBZ2RotorCurrent', expand_x=True, size=(5, 1))],
        [sg.Text('电机温度( ℃): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ2Temperature', expand_x=True)],
        [sg.Text('最大转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ2MAXS', expand_x=True)],
        [sg.Text('最小转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ2MINS', expand_x=True)],
        [sg.Text('1210播种电机速度低', key='A1210')] + [sg.Text('1211播种电机超速 ', key='A1211')],
    ])]]

tab12r = [[sg.Frame(
    '输入参数',
    [
        [sg.Checkbox(text='播种电机使能', enable_events=True, key='CheckBZ2')],
        [sg.Text('设置最大转速(RPM): ')] + [sg.Input(enable_events=True, key='SetBZ2MAXS')],
        [sg.Text('设置最小转速(RPM): ')] + [sg.Input(enable_events=True, key='SetBZ2MINS')],
        [sg.HorizontalSeparator()],
        [sg.Text('设置给定转速(RPM): ')] + [sg.Input(enable_events=True, key='SetBZ2GivenRotor')],
        # [sg.Text('滑块调节给定转速: ')] + [sg.Slider((0, 100), orientation='h', s=(40, 15), key='BZSlider',enable_events=True)],

        # [sg.Button('确定', key='BZButton')],
        # [sg.HorizontalSeparator()],

    ])]]

tab13l = [[sg.Frame(
    '监控参数',
    [

        [sg.Text('电机转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ3Rotor', expand_x=True)],
        [sg.Text('给定转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ3GivenRotor', expand_x=True)],
        [sg.Text('电枢电流( mA): ')] + [
            sg.Text("NULL", enable_events=False, key='GetBZ3RotorCurrent', expand_x=True, size=(5, 1))],
        [sg.Text('电机温度( ℃): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ3Temperature', expand_x=True)],
        [sg.Text('最大转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ3MAXS', expand_x=True)],
        [sg.Text('最小转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ3MINS', expand_x=True)],
        [sg.Text('1310播种电机速度低', key='A1310')] + [sg.Text('1311播种电机超速 ', key='A1311')],
    ])]]

tab13r = [[sg.Frame(
    '输入参数',
    [
        [sg.Checkbox(text='播种电机使能', enable_events=True, key='CheckBZ3')],
        [sg.Text('设置最大转速(RPM): ')] + [sg.Input(enable_events=True, key='SetBZ3MAXS')],
        [sg.Text('设置最小转速(RPM): ')] + [sg.Input(enable_events=True, key='SetBZ3MINS')],
        [sg.HorizontalSeparator()],
        [sg.Text('设置给定转速(RPM): ')] + [sg.Input(enable_events=True, key='SetBZ3GivenRotor')],
        # [sg.Text('滑块调节给定转速: ')] + [sg.Slider((0, 100), orientation='h', s=(40, 15), key='BZSlider',enable_events=True)],
        # [sg.Button('确定', key='BZButton')],
        # [sg.HorizontalSeparator()],

    ])]]

tab14l = [[sg.Frame(
    '监控参数',
    [

        [sg.Text('电机转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ4Rotor', expand_x=True)],
        [sg.Text('给定转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ4GivenRotor', expand_x=True)],
        [sg.Text('电枢电流( mA): ')] + [
            sg.Text("NULL", enable_events=False, key='GetBZ4RotorCurrent', expand_x=True, size=(5, 1))],
        [sg.Text('电机温度( ℃): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ4Temperature', expand_x=True)],
        [sg.Text('最大转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ4MAXS', expand_x=True)],
        [sg.Text('最小转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='GetBZ4MINS', expand_x=True)],
        [sg.Text('1410播种电机速度低', key='A1410')] + [sg.Text('1411播种电机超速 ', key='A1411')],
    ])]]

tab14r = [[sg.Frame(
    '输入参数',
    [
        [sg.Checkbox(text='播种电机使能', enable_events=True, key='CheckBZ4')],
        [sg.Text('设置最大转速(RPM): ')] + [sg.Input(enable_events=True, key='SetBZ4MAXS')],
        [sg.Text('设置最小转速(RPM): ')] + [sg.Input(enable_events=True, key='SetBZ4MINS')],
        [sg.HorizontalSeparator()],
        [sg.Text('设置给定转速(RPM): ')] + [sg.Input(enable_events=True, key='SetBZ4GivenRotor')],
        # [sg.Text('滑块调节给定转速: ')] + [sg.Slider((0, 100), orientation='h', s=(40, 15), key='BZSlider',enable_events=True)],
        # [sg.Button('确定', key='BZButton')],
        # [sg.HorizontalSeparator()],

    ])]]

tab11_layout = [[sg.Column(tab11l), sg.VSeperator(), sg.Column(tab11r)]]
tab12_layout = [[sg.Column(tab12l), sg.VSeperator(), sg.Column(tab12r)]]
tab13_layout = [[sg.Column(tab13l), sg.VSeperator(), sg.Column(tab13r)]]
tab14_layout = [[sg.Column(tab14l), sg.VSeperator(), sg.Column(tab14r)]]









tab4l = [[sg.Frame('', [
    [sg.Frame('电机1', [
        [sg.Text('转速:')] + [sg.Text('NULL', enable_events=True, key='ABZ1Rotor', size=(2, 1))] +
        [sg.Text('温度:')] + [sg.Text('NULL', enable_events=True, key='ABZ1Temperature', size=(2, 1))] +
        [sg.Text('电流:')] + [sg.Text('NULL', enable_events=True, key='ABZ1RotorCurrent', size=(4, 1))] +
        [sg.Text('1110播种电机速度低', key='A1110')] + [sg.Text('1111播种电机超速 ',key='A1111')],
    ])],
    [sg.Frame('电机2', [
        [sg.Text('转速:')] + [sg.Text('NULL', enable_events=True, key='ABZ2Rotor')] +
        [sg.Text('温度:')] + [sg.Text('NULL', enable_events=True, key='ABZ2Temperature')] +
        [sg.Text('电流:')] + [sg.Text('NULL', enable_events=True, key='ABZ2RotorCurrent')] +
        [sg.Text('1210播种电机速度低', key='A1210')] + [sg.Text('1211播种电机超速 ', key='A1211')],
    ])],
    [sg.Frame('电机3', [
        [sg.Text('转速:')] + [sg.Text('NULL', enable_events=True, key='ABZ3Rotor')] +
        [sg.Text('温度:')] + [sg.Text('NULL', enable_events=True, key='ABZ3Temperature')] +
        [sg.Text('电流:')] + [sg.Text('NULL', enable_events=True, key='ABZ3RotorCurrent')] +
        [sg.Text('1310播种电机速度低', key='A1310')] + [sg.Text('1311播种电机超速 ', key='A1311')],
    ])],
    [sg.Frame('电机4', [
        [sg.Text('转速:')] + [sg.Text('NULL', enable_events=True, key='ABZ4Rotor')] +
        [sg.Text('温度:')] + [sg.Text('NULL', enable_events=True, key='ABZ4Temperature')] +
        [sg.Text('电流:')] + [sg.Text('NULL', enable_events=True, key='ABZ4RotorCurrent')] +
        [sg.Text('1410播种电机速度低', key='A1410')] + [sg.Text('1411播种电机超速 ', key='A1411')],
    ])],
    [sg.Text('给定转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='ALLBZGiven')] +
    [sg.Text('最大转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='ALLBZMAX')] +
    [sg.Text('最小转速(RPM): ')] + [sg.Text("NULL", enable_events=False, key='ALLBZMIN')],

])]]

tab4r = [[sg.Frame('输入参数', [
    [sg.Checkbox(text='四电机开关', enable_events=True, key='ALLBZEN')],
    [sg.Text('设置最大转速(RPM): ')] + [sg.Input(enable_events=True, key='SetALLBZMAX', size=(5, 1))],
    [sg.Text('设置最小转速(RPM): ')] + [sg.Input(enable_events=True, key='SetALLBZMIN', size=(5, 1))],
    [sg.Text('设置给定转速(RPM): ')] + [sg.Input(enable_events=True, key='SetALLBZGiven', size=(5, 1))],
])]]

tab4_layout = [
    [sg.Column(tab4l, element_justification='c'), sg.VSeperator(), sg.Column(tab4r, element_justification='c')]]

layout = [
    [[sg.Text('载具速度:')] + [sg.Text('NULL', key='VehicleSpeed')] + [sg.Text(' KM/H')],


    [sg.TabGroup([[sg.Tab('播种电机1', tab11_layout),
                   sg.Tab('播种电机2', tab12_layout),
                   sg.Tab('播种电机3', tab13_layout),
                   sg.Tab('播种电机4', tab14_layout),
                   sg.Tab('四电机', tab4_layout), ]])]]]

'''
 Device information
'''


class ZCAN_DEVICE_INFO(Structure):
    _fields_ = [("hw_Version", c_ushort),
                ("fw_Version", c_ushort),
                ("dr_Version", c_ushort),
                ("in_Version", c_ushort),
                ("irq_Num", c_ushort),
                ("can_Num", c_ubyte),
                ("str_Serial_Num", c_ubyte * 20),
                ("str_hw_Type", c_ubyte * 40),
                ("reserved", c_ushort * 4)]

    def __str__(self):
        return "Hardware Version:%s\nFirmware Version:%s\nDriver Interface:%s\nInterface Interface:%s\nInterrupt Number:%d\nCAN Number:%d\nSerial:%s\nHardware Type:%s\n" % ( \
            self.hw_version, self.fw_version, self.dr_version, self.in_version, self.irq_num, self.can_num, self.serial,
            self.hw_type)

    def _version(self, version):
        return ("V%02x.%02x" if version // 0xFF >= 9 else "V%d.%02x") % (version // 0xFF, version & 0xFF)

    @property
    def hw_version(self):
        return self._version(self.hw_Version)

    @property
    def fw_version(self):
        return self._version(self.fw_Version)

    @property
    def dr_version(self):
        return self._version(self.dr_Version)

    @property
    def in_version(self):
        return self._version(self.in_Version)

    @property
    def irq_num(self):
        return self.irq_Num

    @property
    def can_num(self):
        return self.can_Num

    @property
    def serial(self):
        serial = ''
        for c in self.str_Serial_Num:
            if c > 0:
                serial += chr(c)
            else:
                break
        return serial

    @property
    def hw_type(self):
        hw_type = ''
        for c in self.str_hw_Type:
            if c > 0:
                hw_type += chr(c)
            else:
                break
        return hw_type


class _ZCAN_CHANNEL_CAN_INIT_CONFIG(Structure):
    _fields_ = [("acc_code", c_uint),
                ("acc_mask", c_uint),
                ("reserved", c_uint),
                ("filter", c_ubyte),
                ("timing0", c_ubyte),
                ("timing1", c_ubyte),
                ("mode", c_ubyte)]


class _ZCAN_CHANNEL_CANFD_INIT_CONFIG(Structure):
    _fields_ = [("acc_code", c_uint),
                ("acc_mask", c_uint),
                ("abit_timing", c_uint),
                ("dbit_timing", c_uint),
                ("brp", c_uint),
                ("filter", c_ubyte),
                ("mode", c_ubyte),
                ("pad", c_ushort),
                ("reserved", c_uint)]


class _ZCAN_CHANNEL_INIT_CONFIG(Union):
    _fields_ = [("can", _ZCAN_CHANNEL_CAN_INIT_CONFIG), ("canfd", _ZCAN_CHANNEL_CANFD_INIT_CONFIG)]


class ZCAN_CHANNEL_INIT_CONFIG(Structure):
    _fields_ = [("can_type", c_uint),
                ("config", _ZCAN_CHANNEL_INIT_CONFIG)]


class ZCAN_CHANNEL_ERR_INFO(Structure):
    _fields_ = [("error_code", c_uint),
                ("passive_ErrData", c_ubyte * 3),
                ("arLost_ErrData", c_ubyte)]


class ZCAN_CHANNEL_STATUS(Structure):
    _fields_ = [("errInterrupt", c_ubyte),
                ("regMode", c_ubyte),
                ("regStatus", c_ubyte),
                ("regALCapture", c_ubyte),
                ("regECCapture", c_ubyte),
                ("regEWLimit", c_ubyte),
                ("regRECounter", c_ubyte),
                ("regTECounter", c_ubyte),
                ("Reserved", c_ubyte)]


class ZCAN_CAN_FRAME(Structure):
    _fields_ = [("can_id", c_uint, 29),
                ("err", c_uint, 1),
                ("rtr", c_uint, 1),
                ("eff", c_uint, 1),
                ("can_dlc", c_ubyte),
                ("__pad", c_ubyte),
                ("__res0", c_ubyte),
                ("__res1", c_ubyte),
                ("data", c_ubyte * 8)]


class ZCAN_CANFD_FRAME(Structure):
    _fields_ = [("can_id", c_uint, 29),
                ("err", c_uint, 1),
                ("rtr", c_uint, 1),
                ("eff", c_uint, 1),
                ("len", c_ubyte),
                ("brs", c_ubyte, 1),
                ("esi", c_ubyte, 1),
                ("__res", c_ubyte, 6),
                ("__res0", c_ubyte),
                ("__res1", c_ubyte),
                ("data", c_ubyte * 64)]


class ZCAN_Transmit_Data(Structure):
    _fields_ = [("frame", ZCAN_CAN_FRAME), ("transmit_type", c_uint)]


class ZCAN_Receive_Data(Structure):
    _fields_ = [("frame", ZCAN_CAN_FRAME), ("timestamp", c_ulonglong)]


class ZCAN_TransmitFD_Data(Structure):
    _fields_ = [("frame", ZCAN_CANFD_FRAME), ("transmit_type", c_uint)]


class ZCAN_ReceiveFD_Data(Structure):
    _fields_ = [("frame", ZCAN_CANFD_FRAME), ("timestamp", c_ulonglong)]


class ZCAN_AUTO_TRANSMIT_OBJ(Structure):
    _fields_ = [("enable", c_ushort),
                ("index", c_ushort),
                ("interval", c_uint),
                ("obj", ZCAN_Transmit_Data)]


class ZCANFD_AUTO_TRANSMIT_OBJ(Structure):
    _fields_ = [("enable", c_ushort),
                ("index", c_ushort),
                ("interval", c_uint),
                ("obj", ZCAN_TransmitFD_Data)]


class IProperty(Structure):
    _fields_ = [("SetValue", c_void_p),
                ("GetValue", c_void_p),
                ("GetPropertys", c_void_p)]


class RX_DATA(Structure):
    _fields_ = [("ID", c_uint),
                ("DATA", c_ubyte * 8),
                ("Timer", c_uint)]


class ZCAN(object):
    def __init__(self):
        if platform.system() == "Windows":
            # noinspection SpellCheckingInspection
            self.__dll = windll.LoadLibrary("./zlgcan.dll")
        else:
            print("No support now!")
        if self.__dll == None:
            print("DLL couldn't be loaded!")

    def OpenDevice(self, device_type, device_index, reserved):
        try:
            return self.__dll.ZCAN_OpenDevice(device_type, device_index, reserved)
        except:
            print("Exception on OpenDevice!")
            raise

    def CloseDevice(self, device_handle):
        try:
            return self.__dll.ZCAN_CloseDevice(device_handle)
        except:
            print("Exception on CloseDevice!")
            raise

    def GetDeviceInf(self, device_handle):
        try:
            info = ZCAN_DEVICE_INFO()
            ret = self.__dll.ZCAN_GetDeviceInf(device_handle, byref(info))
            return info if ret == ZCAN_STATUS_OK else None
        except:
            print("Exception on ZCAN_GetDeviceInf")
            raise

    def DeviceOnLine(self, device_handle):
        try:
            return self.__dll.ZCAN_IsDeviceOnLine(device_handle)
        except:
            print("Exception on ZCAN_ZCAN_IsDeviceOnLine!")
            raise

    def InitCAN(self, device_handle, can_index, init_config):
        try:
            return self.__dll.ZCAN_InitCAN(device_handle, can_index, byref(init_config))
        except:
            print("Exception on ZCAN_InitCAN!")
            raise

    def StartCAN(self, chn_handle):
        try:
            return self.__dll.ZCAN_StartCAN(chn_handle)
        except:
            print("Exception on ZCAN_StartCAN!")
            raise

    def ResetCAN(self, chn_handle):
        try:
            return self.__dll.ZCAN_ResetCAN(chn_handle)
        except:
            print("Exception on ZCAN_ResetCAN!")
            raise

    def ClearBuffer(self, chn_handle):
        try:
            return self.__dll.ZCAN_ClearBuffer(chn_handle)
        except:
            print("Exception on ZCAN_ClearBuffer!")
            raise

    def ReadChannelErrInfo(self, chn_handle):
        try:
            ErrInfo = ZCAN_CHANNEL_ERR_INFO()
            ret = self.__dll.ZCAN_ReadChannelErrInfo(chn_handle, byref(ErrInfo))
            return ErrInfo if ret == ZCAN_STATUS_OK else None
        except:
            print("Exception on ZCAN_ReadChannelErrInfo!")
            raise

    def ReadChannelStatus(self, chn_handle):
        try:
            status = ZCAN_CHANNEL_STATUS()
            ret = self.__dll.ZCAN_ReadChannelStatus(chn_handle, byref(status))
            return status if ret == ZCAN_STATUS_OK else None
        except:
            print("Exception on ZCAN_ReadChannelStatus!")
            raise

    def GetReceiveNum(self, chn_handle, can_type=ZCAN_TYPE_CAN):
        try:
            return self.__dll.ZCAN_GetReceiveNum(chn_handle, can_type)
        except:
            print("Exception on ZCAN_GetReceiveNum!")
            raise

    def Transmit(self, chn_handle, std_msg, len):
        try:
            return self.__dll.ZCAN_Transmit(chn_handle, byref(std_msg), len)
        except:
            print("Exception on ZCAN_Transmit!")
            raise

    def Receive(self, chn_handle, rcv_num, wait_time=c_int(-1)):
        try:
            rcv_can_msgs = (ZCAN_Receive_Data * rcv_num)()
            ret = self.__dll.ZCAN_Receive(chn_handle, byref(rcv_can_msgs), rcv_num, wait_time)
            return rcv_can_msgs, ret
        except:
            print("Exception on ZCAN_Receive!")
            raise

    def TransmitFD(self, chn_handle, fd_msg, len):
        try:
            return self.__dll.ZCAN_TransmitFD(chn_handle, byref(fd_msg), len)
        except:
            print("Exception on ZCAN_TransmitFD!")
            raise

    def ReceiveFD(self, chn_handle, rcv_num, wait_time=c_int(-1)):
        try:
            rcv_canfd_msgs = (ZCAN_ReceiveFD_Data * rcv_num)()
            ret = self.__dll.ZCAN_ReceiveFD(chn_handle, byref(rcv_canfd_msgs), rcv_num, wait_time)
            return rcv_canfd_msgs, ret
        except:
            print("Exception on ZCAN_ReceiveFD!")
            raise

    def GetIProperty(self, device_handle):
        try:
            self.__dll.GetIProperty.restype = POINTER(IProperty)
            return self.__dll.GetIProperty(device_handle)
        except:
            print("Exception on ZCAN_GetIProperty!")
            raise

    def SetValue(self, iproperty, path, value):
        try:
            func = CFUNCTYPE(c_uint, c_char_p, c_char_p)(iproperty.contents.SetValue)
            return func(c_char_p(path.encode("utf-8")), c_char_p(value.encode("utf-8")))
        except:
            print("Exception on IProperty SetValue")
            raise

    def GetValue(self, iproperty, path):
        try:
            func = CFUNCTYPE(c_char_p, c_char_p)(iproperty.contents.GetValue)
            return func(c_char_p(path.encode("utf-8")))
        except:
            print("Exception on IProperty GetValue")
            raise

    def ReleaseIProperty(self, iproperty):
        try:
            return self.__dll.ReleaseIProperty(iproperty)
        except:
            print("Exception on ZCAN_ReleaseIProperty!")
            raise


###############################################################################

'''
USBCAN-II Start Demo
'''


def toInt(low, high):
    low = low[2:]
    high = high[2:]
    # print("Low:",low," High:",high)
    if len(low) == 1:
        low = '0' + low
    intdata = high + low
    if len(intdata) != 0:
        return int(intdata, 16)


def toREAL(b1, b2, b3, b4):
    if len(b1) == 1:
        b1 = '0' + b1
    elif len(b2) == 1:
        b2 = '0' + b2
    elif len(b2) == 1:
        b3 = '0' + b3

    realdata = b4 + b3 + b2 + b1
    if len(realdata) != 0:
        if int(realdata, 16) > int('0x80000000', 16):
            fnum = int('0x100000000', 16) - int(realdata, 16)
            return 0 - fnum
        else:
            return int(realdata, 16)
        # return struct.unpack('<f', bytes.fromhex(realdata))[0]


def toRead(mod, lister, ID):
    temp = Ddata()
    temp.ID = ID
    if mod == 1:
        l1 = str(lister[0])
        h1 = str(lister[1])
        temp.D1 = toInt(l1, h1)

        l2 = str(lister[2])
        h2 = str(lister[3])
        temp.D2 = toInt(l2, h2)

        l3 = str(lister[4])
        h3 = str(lister[5])
        temp.D3 = toInt(l3, h3)

        l4 = str(lister[6])
        h4 = str(lister[7])
        temp.D4 = toInt(l4, h4)
        # print("ID:",ID," l1:",l1," h1:",h1," l2:",l2," h2:",h2," l3:",l3," h3:",h3," l4:",l4," h4:",h4)
        # print('ID:',ID,' source:',lister)

    elif mod == 2:
        d1 = str(lister[0])[2:]
        d2 = str(lister[1])[2:]
        d3 = str(lister[2])[2:]
        d4 = str(lister[3])[2:]
        temp.D1 = toREAL(d1, d2, d3, d4)

        d5 = str(lister[4])[2:]
        d6 = str(lister[5])[2:]
        d7 = str(lister[6])[2:]
        d8 = str(lister[7])[2:]
        temp.D2 = toREAL(d5, d6, d7, d8)

    # print("ID:", temp.ID, " D1:", temp.D1, " D2:", temp.D2, " D3:", temp.D3, " D4:", temp.D4)
    return temp


def can_I_start(zcanlib, device_handle, chn):
    ip = zcanlib.GetIProperty(device_handle)
    ret = zcanlib.SetValue(ip, str(chn) + "/baud_rate", "1000000")  # 1000Kbps
    if ret != ZCAN_STATUS_OK:
        print("Set CH%d CAN_E_U baud_rate failed!" % (chn))
        exit(0)
    chn_init_cfg = ZCAN_CHANNEL_INIT_CONFIG()
    chn_init_cfg.can_type = ZCAN_TYPE_CAN
    chn_init_cfg.config.can.acc_code = 0
    chn_init_cfg.config.can.acc_mask = 0xFFFFFFFF
    chn_init_cfg.config.can.mode = 0
    chn_handle = zcanlib.InitCAN(device_handle, chn, chn_init_cfg)
    if chn_handle == 0:
        print("initCAN failed!" % (chn))
        exit(0)
    zcanlib.ReleaseIProperty(ip)

    ret = zcanlib.StartCAN(chn_handle)
    if ret != ZCAN_STATUS_OK:
        print("startCAN%d  failed!" % (chn))
        exit(0)
    return chn_handle


def tx_msge(chn_handle, data, ids, num=1):
    number = num
    msgs = (ZCAN_Transmit_Data * number)()
    for i in range(num):
        msgs[i].transmit_type = 1
        msgs[i].frame.eff = 0  # 0-标准帧，1-扩展帧
        msgs[i].frame.rtr = 0  # 0-数据帧，1-远程帧
        msgs[i].frame.can_id = int(ids, 16)
        msgs[i].frame.can_dlc = 8
        for j in range(msgs[i].frame.can_dlc):
            msgs[i].frame.data[j] = int(data[j], 16)
    ret = zcanlib.Transmit(chn_handle, msgs, number)
    time.sleep(0.02)  # 延时20ms
    # print("Tranmit Num: %d." % ret)


def rx_msge(chn_handle):
    global ZCAN_TYPE_CAN
    tempdata = ['', '', '', '', '', '', '', '']
    # while True:
    rcv_num = zcanlib.GetReceiveNum(chn_handle, ZCAN_TYPE_CAN)
    if rcv_num:
        rcv_msg, rcv_num = zcanlib.Receive(chn_handle, rcv_num)
        for i in range(rcv_num):
            CANID = int("%x" % rcv_msg[i].frame.can_id)
            # CANID = int(str(rcv_msg[i].frame.can_id),16)
            for a in range(rcv_msg[i].frame.can_dlc):
                tempdata[a] = hex(rcv_msg[i].frame.data[a])

            if CANID == 111:
                # D111 = toRead(1, tempdata, CANID)
                globalVAR.set_value('D111', toRead(1, tempdata, CANID))
                # print(globalVAR.get_val('D111').D3," ", toRead(1, tempdata, CANID).D3)
            elif CANID == 112:
                # globalVAR.get_val('D112') = toRead(1, tempdata, CANID)
                globalVAR.set_value('D112', toRead(1, tempdata, CANID))
                globalVAR.set_value('AxleSpeed_1', toRead(1, tempdata, CANID).D4)
                # print(globalVAR.get_val('AxleSpeed_1'), toRead(1, tempdata, CANID).D4)

            elif CANID == 121:
                # globalVAR.get_val('D121') = toRead(1, tempdata, CANID)
                globalVAR.set_value('D121', toRead(1, tempdata, CANID))
            elif CANID == 122:
                # globalVAR.get_val('D122') = toRead(1, tempdata, CANID)
                globalVAR.set_value('D122', toRead(1, tempdata, CANID))
                globalVAR.set_value('AxleSpeed_2', toRead(1, tempdata, CANID).D4)
            elif CANID == 131:
                # globalVAR.get_val('D131') = toRead(1, tempdata, CANID)
                globalVAR.set_value('D131', toRead(1, tempdata, CANID))
            elif CANID == 132:
                # globalVAR.get_val('D132') = toRead(1, tempdata, CANID)
                globalVAR.set_value('D132', toRead(1, tempdata, CANID))
                globalVAR.set_value('AxleSpeed_3', toRead(1, tempdata, CANID).D4)
            elif CANID == 141:
                # globalVAR.get_val('globalVAR.get_val('D141')') = toRead(1, tempdata, CANID)
                globalVAR.set_value('D141', toRead(1, tempdata, CANID))
            elif CANID == 142:
                # globalVAR.get_val('D142') = toRead(1, tempdata, CANID)
                globalVAR.set_value('D142', toRead(1, tempdata, CANID))
                globalVAR.set_value('AxleSpeed_4', toRead(1, tempdata, CANID).D4)
            elif CANID == 103:
                # globalVAR.get_val('D103') = toRead(2, tempdata, CANID)
                globalVAR.set_value('D103', toRead(2, tempdata, CANID))
            elif CANID == 104:
                # globalVAR.get_val('D104') = toRead(2, tempdata, CANID)
                globalVAR.set_value('D104', toRead(2, tempdata, CANID))
            elif CANID == 105:
                # globalVAR.get_val('D105') = toRead(1, tempdata, CANID)
                globalVAR.set_value('D105', toRead(1, tempdata, CANID))
            elif CANID == 106:
                # globalVAR.get_val('D106') = toRead(1, tempdata, CANID)
                globalVAR.set_value('D106', toRead(1, tempdata, CANID))
            elif CANID == 107:
                # D107 = toRead(1, tempdata, CANID)
                globalVAR.set_value('D107', toRead(1, tempdata, CANID))
            elif CANID == 108:
                # globalVAR.get_val('D108') = toRead(2, tempdata, CANID)
                globalVAR.set_value('D108', toRead(2, tempdata, CANID))
            elif CANID == 109:
                # D109 = toRead(1, tempdata, CANID)
                globalVAR.set_value('D109', toRead(1, tempdata, CANID))
            elif CANID == 110:
                # globalVAR.get_val('D110') = toRead(2, tempdata, CANID)
                globalVAR.set_value('D110', toRead(2, tempdata, CANID))
            elif CANID == 140:
                # D140 = toRead(1, tempdata, CANID)
                globalVAR.set_value('D140', toRead(1, tempdata, CANID))
            elif CANID == 401:
                # D401 = toRead(1, tempdata, CANID)
                globalVAR.set_value('D401', toRead(1, tempdata, CANID))
            elif CANID == 402:
                # D402 = toRead(1, tempdata, CANID)
                globalVAR.set_value('D402', toRead(1, tempdata, CANID))
            elif CANID == 403:
                #D403 = toRead(1, tempdata, CANID)
                globalVAR.set_value('D403', toRead(1, tempdata, CANID))
                #print(globalVAR.get_val('D403').D1)


def refresh(win):
    win['GetBZ1Rotor'].update(globalVAR.get_val('D112').D4)
    win['GetBZ1GivenRotor'].update(globalVAR.get_val('D112').D3)
    win['GetBZ1RotorCurrent'].update(globalVAR.get_val('D111').D2)
    win['GetBZ1Temperature'].update(globalVAR.get_val('D111').D3)
    win['GetBZ1MAXS'].update(globalVAR.get_val('D112').D1)
    win['GetBZ1MINS'].update(globalVAR.get_val('D112').D2)

    win['GetBZ2Rotor'].update(globalVAR.get_val('D122').D4)
    win['GetBZ2GivenRotor'].update(globalVAR.get_val('D122').D3)
    win['GetBZ2RotorCurrent'].update(globalVAR.get_val('D121').D2)
    win['GetBZ2Temperature'].update(globalVAR.get_val('D121').D3)
    win['GetBZ2MAXS'].update(globalVAR.get_val('D122').D1)
    win['GetBZ2MINS'].update(globalVAR.get_val('D122').D2)

    win['GetBZ3Rotor'].update(globalVAR.get_val('D132').D4)
    win['GetBZ3GivenRotor'].update(globalVAR.get_val('D132').D3)
    win['GetBZ3RotorCurrent'].update(globalVAR.get_val('D131').D2)
    win['GetBZ3Temperature'].update(globalVAR.get_val('D131').D3)
    win['GetBZ3MAXS'].update(globalVAR.get_val('D132').D1)
    win['GetBZ3MINS'].update(globalVAR.get_val('D132').D2)

    win['GetBZ4Rotor'].update(globalVAR.get_val('D142').D4)
    win['GetBZ4GivenRotor'].update(globalVAR.get_val('D142').D3)
    win['GetBZ4RotorCurrent'].update(globalVAR.get_val('D141').D2)
    win['GetBZ4Temperature'].update(globalVAR.get_val('D141').D3)
    win['GetBZ4MAXS'].update(globalVAR.get_val('D142').D1)
    win['GetBZ4MINS'].update(globalVAR.get_val('D142').D2)

    win['GetPFMAXS'].update(globalVAR.get_val('D106').D1)
    win['GetPFMINS'].Update(globalVAR.get_val('D106').D2)
    win['GetPFRotor'].Update(globalVAR.get_val('D103').D1 / 100)
    win['GetPFGivenRotor'].Update(globalVAR.get_val('D105').D1)
    win['GetPFPressure'].Update(globalVAR.get_val('D103').D2)

    win['GetFJMAXS'].Update(globalVAR.get_val('D106').D3)
    win['GetFJMINS'].Update(globalVAR.get_val('D106').D4)
    win['GetFJRotor'].Update(globalVAR.get_val('D104').D1 / 100)
    win['GetFJGivenRotor'].Update(globalVAR.get_val('D105').D2)
    win['GetFJPressure'].Update(globalVAR.get_val('D104').D2)
    win['GetFJPressure2'].Update(globalVAR.get_val('D110').D1)
    win['VehicleSpeed'].Update(globalVAR.get_val('D108').D1 / 100)

    win['ABZ1Rotor'].update(globalVAR.get_val('D112').D4)
    win['ABZ1Temperature'].update(globalVAR.get_val('D111').D3)
    win['ABZ1RotorCurrent'].update(globalVAR.get_val('D111').D2)

    win['ABZ2Rotor'].update(globalVAR.get_val('D122').D4)
    win['ABZ2Temperature'].update(globalVAR.get_val('D121').D3)
    win['ABZ2RotorCurrent'].update(globalVAR.get_val('D121').D2)

    win['ABZ3Rotor'].update(globalVAR.get_val('D132').D4)
    win['ABZ3Temperature'].update(globalVAR.get_val('D131').D3)
    win['ABZ3RotorCurrent'].update(globalVAR.get_val('D131').D2)

    win['ABZ4Rotor'].update(globalVAR.get_val('D142').D4)
    win['ABZ4Temperature'].update(globalVAR.get_val('D141').D3)
    win['ABZ4RotorCurrent'].update(globalVAR.get_val('D141').D2)

    win['ALLBZMAX'].update(win['SetALLBZMAX'].get())
    win['ALLBZMIN'].update(win['SetALLBZMIN'].get())
    win['ALLBZGiven'].update(win['SetALLBZGiven'].get())



def to16(h):
    if h == '' or h == ' ':
        givenH = '0'
        givenL = '0'
        return givenL, givenH

    if len(h) != 0:
        # givenHex = int(h)
        givenHex = hex(int(h))[2:]
    if len(h) == 0:
        givenH = '0'
        givenL = '0'
        return givenL, givenH
    if len(givenHex) <= 2:
        givenH = '0'
        givenL = givenHex
        return givenL, givenH
    if len(givenHex) == 3:
        givenH = '0' + givenHex[-3:-2]
        givenL = givenHex[-2:]
        return givenL, givenH
    if len(givenHex) >= 4:
        givenH = givenHex[-4:-2]
        givenL = givenHex[-2:]
        return givenL, givenH


def toBool(b):
    if b:
        return 1
    else:
        return 0


def toMOTOR(given, max, min, en):
    global chn_handle
    gl, gh = to16(given)
    maxl, maxh = to16(max)
    minl, minh = to16(min)
    e = str(int(toBool(en)))
    templist = [gh, gl, maxh, maxl, minh, minl, '0', e]
    return templist


def setAllBZ(values):
    global chn_handle, window
    givenspeed = window['SetALLBZGiven'].get()
    maxspeed = window['SetALLBZMAX'].get()
    minspeed = window['SetALLBZMIN'].get()
    bz = window['ALLBZEN'].get()

    lister = toMOTOR(givenspeed, maxspeed, minspeed, bz)
    tx_msge(chn_handle, lister, "301", 1)
    tx_msge(chn_handle, lister, "311", 1)
    tx_msge(chn_handle, lister, "321", 1)
    tx_msge(chn_handle, lister, "331", 1)


def setBZ1(values):
    global chn_handle, window
    givenspeed = window['SetBZ1GivenRotor'].get()
    maxspeed = window['SetBZ1MAXS'].get()
    minspeed = window['SetBZ1MINS'].get()
    bz = window['CheckBZ1'].get()

    lister = toMOTOR(givenspeed, maxspeed, minspeed, bz)
    tx_msge(chn_handle, lister, "301", 1)


def setBZ2(values):
    global chn_handle, window
    givenspeed = window['SetBZ2GivenRotor'].get()
    maxspeed = window['SetBZ2MAXS'].get()
    minspeed = window['SetBZ2MINS'].get()
    bz = window['CheckBZ2'].get()

    lister = toMOTOR(givenspeed, maxspeed, minspeed, bz)
    tx_msge(chn_handle, lister, "311", 1)


def setBZ3(values):
    global chn_handle, window
    givenspeed = window['SetBZ3GivenRotor'].get()
    maxspeed = window['SetBZ3MAXS'].get()
    minspeed = window['SetBZ3MINS'].get()
    bz = window['CheckBZ3'].get()

    lister = toMOTOR(givenspeed, maxspeed, minspeed, bz)
    tx_msge(chn_handle, lister, "321", 1)


def setBZ4(values):
    global chn_handle, window
    givenspeed = window['SetBZ4GivenRotor'].get()
    maxspeed = window['SetBZ4MAXS'].get()
    minspeed = window['SetBZ4MINS'].get()
    bz = window['CheckBZ4'].get()

    lister = toMOTOR(givenspeed, maxspeed, minspeed, bz)
    tx_msge(chn_handle, lister, "331", 1)


def setPF(values):
    givenspeed = window['SetPFGivenRotor'].get()
    maxspeed = window['SetPFMAXS'].get()
    minspeed = window['SetPFMINS'].get()
    pf = window['CheckPF'].get()

    lister = toMOTOR(givenspeed, maxspeed, minspeed, pf)
    tx_msge(chn_handle, lister, "302", 1)


def setFJ(values):
    givenspeed = window['SetFJGivenRotor'].get()
    maxspeed = window['SetFJMAXS'].get()
    minspeed = window['SetFJMINS'].get()
    fj = window['CheckFJ'].get()

    lister = toMOTOR(givenspeed, maxspeed, minspeed, fj)
    tx_msge(chn_handle, lister, "303", 1)


def setAuto(values):
    val = window['CheckAuto'].get()
    val2 = window['CheckY1'].get()
    lister = [str(int(val)), '0', str(int(val2)), '0', '0', '0', '0', '0']
    tx_msge(chn_handle, lister, "304", 1)


def setY1(values):
    val = window['CheckAuto'].get()
    val2 = window['CheckY1'].get()
    lister = [str(int(val)), '0', str(int(val2)), '0', '0', '0', '0', '0']
    tx_msge(chn_handle, lister, "304", 1)


def drawError(errorID, textKey, mods):
    if mods == 1:
        mod = 'E'
    elif mods == 2:
        mod = "A"

    if errorID != 0:
        state = int(str(errorID)[-1:])
        ids = mod + str(errorID)
        #print(errorID,state)
        if state == 1:
            window[ids].Update(value=window[ids].get(), text_color='red')
            #print(ids)
        if state == 0:
            window[ids].Update(value=window[ids].get(), text_color='yellow')
            #print(ids)

    else:
        window[mod + str(textKey)].Update(value=window[mod + str(textKey)].get(), text_color='white')
        window[mod + str(textKey + 1)].Update(value=window[mod + str(textKey + 1)].get(), text_color='white')


def downerErrorMessage():
    drawError(globalVAR.get_val('D401').D2, 1030, 1)
    drawError(globalVAR.get_val('D401').D3, 1040, 1)
    drawError(globalVAR.get_val('D402').D1, 2030, 1)
    drawError(globalVAR.get_val('D402').D2, 2040, 1)
    drawError(globalVAR.get_val('D402').D3, 2050, 1)

    drawError(globalVAR.get_val('D403').D1, 1110, 2)
    drawError(globalVAR.get_val('D403').D2, 1210, 2)
    drawError(globalVAR.get_val('D403').D3, 1310, 2)
    drawError(globalVAR.get_val('D403').D4, 1410, 2)

    #print(str(globalVAR.get_val('D403').D1))

event_callbacks = {
    'SetBZ1GivenRotor': setBZ1,
    'SetBZ1MAXS': setBZ1,
    'SetBZ1MINS': setBZ1,
    'CheckBZ1': setBZ1,

    'SetBZ2GivenRotor': setBZ2,
    'SetBZ2MAXS': setBZ2,
    'SetBZ2MINS': setBZ2,
    'CheckBZ2': setBZ2,

    'SetBZ3GivenRotor': setBZ3,
    'SetBZ3MAXS': setBZ3,
    'SetBZ3MINS': setBZ3,
    'CheckBZ3': setBZ3,

    'SetBZ4GivenRotor': setBZ4,
    'SetBZ4MAXS': setBZ4,
    'SetBZ4MINS': setBZ4,
    'CheckBZ4': setBZ4,

    'SetPFGivenRotor': setPF,
    'SetPFMAXS': setPF,
    'SetPFMINS': setPF,
    'CheckPF': setPF,
    'SetFJGivenRotor': setFJ,
    'SetFJMAXS': setFJ,
    'SetFJMINS': setFJ,
    'CheckFJ': setFJ,
    'CheckAuto': setAuto,
    'CheckY1': setY1,

    'SetALLBZMAX': setAllBZ,
    'SetALLBZMIN': setAllBZ,
    'SetALLBZGiven': setAllBZ,
}


def ini_var():
    globalVAR._ini()
    globalVAR.set_value('AxleSpeed_1', 0)
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

def temp():
    global chn_handle
    zcanlib = ZCAN()
    handle = zcanlib.OpenDevice(ZCAN_USBCAN2, 0, 0)

    if handle == INVALID_DEVICE_HANDLE:
        print("Open USBCAN-II device failed!")
        exit(0)
    print("Open USBCAN-II device success!")

    print("device handle:%d." % (handle))

    info = zcanlib.GetDeviceInf(handle)
    print("Device Information:\n%s" % (info))

    # Start CAN

    chn_handle = can_I_start(zcanlib, handle, 0)

    print("channel handle:%d." % (chn_handle))

    ini_var()


if __name__ == "__main__":
    #sg.main()




    window = sg.Window('测试', layout)



    while True:
        event, values = window.read(timeout=250)
        if event == sg.WINDOW_CLOSED:
            break
        #if event in event_callbacks:
            #event_callbacks[event](values)

        #t = threading.Thread(target=rx_msge, args=(chn_handle,))

        #t.start()
        #time.sleep(0.005)
        #refresh(window)
        #downerErrorMessage()
        #window.refresh()
        #t.join()



