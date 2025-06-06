"""
  Generated by Eclipse Cyclone DDS idlc Python Backend
  Cyclone DDS IDL version: v0.11.0
  Module: geometry_msgs.msg.dds_
  IDL file: PoseStamped_.idl

"""

from enum import auto
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass

import cyclonedds.idl as idl
import cyclonedds.idl.annotations as annotate
import cyclonedds.idl.types as types

# root module import for resolving types
# import geometry_msgs

# if TYPE_CHECKING:
#     import std_msgs.msg.dds_



@dataclass
@annotate.final
@annotate.autoid("sequential")
class PoseStamped_(idl.IdlStruct, typename="geometry_msgs.msg.dds_.PoseStamped_"):
    header: 'unitree.unitree_sdk2py.idl.std_msgs.msg.dds_.Header_'
    pose: 'unitree.unitree_sdk2py.idl.geometry_msgs.msg.dds_.Pose_'


