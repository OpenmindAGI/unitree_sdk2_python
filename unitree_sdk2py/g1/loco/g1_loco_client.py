import json

from ...rpc.client import Client
from .g1_loco_api import *

"""
" class SportClient
"""
class LocoClient(Client):
    def __init__(self):
        super().__init__(LOCO_SERVICE_NAME, False)
        self.first_shake_hand_stage_ = -1

    def Init(self):
        # set api version
        self._SetApiVerson(LOCO_API_VERSION)

        # regist api
        self._RegistApi(ROBOT_API_ID_LOCO_GET_FSM_ID, 0)
        self._RegistApi(ROBOT_API_ID_LOCO_GET_FSM_MODE, 0)
        self._RegistApi(ROBOT_API_ID_LOCO_GET_BALANCE_MODE, 0)
        self._RegistApi(ROBOT_API_ID_LOCO_GET_SWING_HEIGHT, 0)
        self._RegistApi(ROBOT_API_ID_LOCO_GET_STAND_HEIGHT, 0)
        self._RegistApi(ROBOT_API_ID_LOCO_GET_PHASE, 0) # deprecated

        self._RegistApi(ROBOT_API_ID_LOCO_SET_FSM_ID, 0)
        self._RegistApi(ROBOT_API_ID_LOCO_SET_BALANCE_MODE, 0)
        self._RegistApi(ROBOT_API_ID_LOCO_SET_SWING_HEIGHT, 0)
        self._RegistApi(ROBOT_API_ID_LOCO_SET_STAND_HEIGHT, 0)
        self._RegistApi(ROBOT_API_ID_LOCO_SET_VELOCITY, 0)
        self._RegistApi(ROBOT_API_ID_LOCO_SET_ARM_TASK, 0)

    # 7101
    def SetFsmId(self, fsm_id: int, noReply: bool = False):
        p = {}
        p["data"] = fsm_id
        parameter = json.dumps(p)
        if noReply:
            return self._CallNoReply(ROBOT_API_ID_LOCO_SET_FSM_ID, parameter)
        code, data = self._Call(ROBOT_API_ID_LOCO_SET_FSM_ID, parameter)
        return code

    # 7102
    def SetBalanceMode(self, balance_mode: int, noReply: bool = False):
        p = {}
        p["data"] = balance_mode
        parameter = json.dumps(p)
        if noReply:
            return self._CallNoReply(ROBOT_API_ID_LOCO_SET_BALANCE_MODE, parameter)
        code, data = self._Call(ROBOT_API_ID_LOCO_SET_BALANCE_MODE, parameter)
        return code

    # 7104
    def SetStandHeight(self, stand_height: float, noReply: bool = False):
        p = {}
        p["data"] = stand_height
        parameter = json.dumps(p)
        if noReply:
            return self._CallNoReply(ROBOT_API_ID_LOCO_SET_STAND_HEIGHT, parameter)
        code, data = self._Call(ROBOT_API_ID_LOCO_SET_STAND_HEIGHT, parameter)
        return code

    # 7105
    def SetVelocity(self, vx: float, vy: float, omega: float, duration: float = 1.0, noReply: bool = False):
        p = {}
        velocity = [vx,vy,omega]
        p["velocity"] = velocity
        p["duration"] = duration
        parameter = json.dumps(p)
        if noReply:
            return self._CallNoReply(ROBOT_API_ID_LOCO_SET_VELOCITY, parameter)
        code, data = self._Call(ROBOT_API_ID_LOCO_SET_VELOCITY, parameter)
        return code
    
    # 7106
    def SetTaskId(self, task_id: float, noReply: bool = False):
        p = {}
        p["data"] = task_id
        parameter = json.dumps(p)
        if noReply:
            return self._CallNoReply(ROBOT_API_ID_LOCO_SET_ARM_TASK, parameter)
        code, data = self._Call(ROBOT_API_ID_LOCO_SET_ARM_TASK, parameter)
        return code

    def Damp(self, noReply: bool = False):
        self.SetFsmId(1, noReply)
    
    def Start(self, noReply: bool = False):
        self.SetFsmId(200, noReply)

    def Squat2StandUp(self):
        self.SetFsmId(706)

    def Lie2StandUp(self):
        self.SetFsmId(702)

    def Sit(self, noReply: bool = False):
        self.SetFsmId(3, noReply)

    def StandUp2Squat(self):
        self.SetFsmId(706)

    def ZeroTorque(self, noReply: bool = False):
        self.SetFsmId(0, noReply)

    def StopMove(self, noReply: bool = False):
        self.SetVelocity(0., 0., 0., noReply)

    def HighStand(self, noReply: bool = False):
        UINT32_MAX = (1 << 32) - 1
        self.SetStandHeight(UINT32_MAX, noReply)

    def LowStand(self, noReply: bool = False):
        UINT32_MIN = 0
        self.SetStandHeight(UINT32_MIN, noReply)

    def Move(self, vx: float, vy: float, vyaw: float, continous_move: bool = False, noReply: bool = False):
        duration = 864000.0 if continous_move else 1
        self.SetVelocity(vx, vy, vyaw, duration, noReply)

    def BalanceStand(self, balance_mode: int, noReply: bool = False):
        self.SetBalanceMode(balance_mode, noReply)

    def WaveHand(self, turn_flag: bool = False, noReply: bool = False):
        self.SetTaskId(1 if turn_flag else 0, noReply)

    def ShakeHand(self, stage: int = -1, noReply: bool = False):
        if stage == 0:
            self.first_shake_hand_stage_ = False
            self.SetTaskId(2, noReply)
        elif stage == 1:
            self.first_shake_hand_stage_ = True
            self.SetTaskId(3, noReply)
        else:
            self.first_shake_hand_stage_ = not self.first_shake_hand_stage_
            return self.SetTaskId(3 if self.first_shake_hand_stage_ else 2, noReply)
    