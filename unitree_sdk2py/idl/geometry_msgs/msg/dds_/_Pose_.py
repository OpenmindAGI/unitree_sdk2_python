"""
  Generated by Eclipse Cyclone DDS idlc Python Backend
  Cyclone DDS IDL version: v0.11.0
  Module: geometry_msgs.msg.dds_
  IDL file: Pose_.idl

"""

from enum import auto
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass

import cyclonedds.idl as idl
import cyclonedds.idl.annotations as annotate
import cyclonedds.idl.types as types

# root module import for resolving types
# import geometry_msgs


@dataclass
@annotate.final
@annotate.autoid("sequential")
class Pose_(idl.IdlStruct, typename="geometry_msgs.msg.dds_.Pose_"):
    position: 'unitree.unitree_sdk2py.idl.geometry_msgs.msg.dds_.Point_'
    orientation: 'unitree.unitree_sdk2py.idl.geometry_msgs.msg.dds_.Quaternion_'


