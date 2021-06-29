#!/usr/bin/env python3

from pyrobot import Robot

bot = Robot('locobot')

bot.camera.reset()

camera_pose = [0, 0.7]
bot.camera.set_pan_tilt(camera_pose[0], camera_pose[1], wait=True)

camera_pose = [-0.4, 0.7]
bot.camera.set_pan_tilt(camera_pose[0], camera_pose[1], wait=True)

camera_pose = [0.4, 0.7]
bot.camera.set_pan_tilt(camera_pose[0], camera_pose[1], wait=True)

camera_pose = [-0.4, 0.7]     
bot.camera.set_pan_tilt(camera_pose[0], camera_pose[1], wait=True)

camera_pose = [0.4, 0.7]
bot.camera.set_pan_tilt(camera_pose[0], camera_pose[1], wait=True)

camera_pose = [0, 0.7]
bot.camera.set_pan_tilt(camera_pose[0], camera_pose[1], wait=True)

bot.camera.reset()
