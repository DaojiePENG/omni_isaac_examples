# Copyright (c) 2020-2023, NVIDIA CORPORATION. All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto. Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#

import os

from omni.isaac.examples.base_sample import BaseSampleExtension
from omni.isaac.examples.go2 import Go2Example


class Go2ExampleExtension(BaseSampleExtension):
    def on_startup(self, ext_id: str):
        super().on_startup(ext_id)

        overview = "This Example shows an Unitree Go2 running a flat terrain policy trained in Isaac Lab"
        overview += "\n\tKeybord Input:"
        overview += "\n\t\tup arrow / numpad 8: Move Forward"
        overview += "\n\t\down arrow / numpad 2: Move Backward"
        overview += "\n\t\tleft arrow/ numpad 4: Spin Counterclockwise"
        overview += "\n\t\tright arrow / numpad 6: Spin Clockwise"
        overview += "\n\nPress the 'Open in IDE' button to view the source code."

        super().start_extension(
            menu_name="tian",
            submenu_name="",
            name="QuadrupedGo2",
            title="Unitree Go2 Example",
            doc_link="https://docs.omniverse.nvidia.com/isaacsim/latest/isaac_lab_tutorials/tutorial_policy_deployment.html",
            overview=overview,
            file_path=os.path.abspath(__file__),
            sample=Go2Example(),
        )
