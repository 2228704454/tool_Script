#!/usr/bin/env python

import subprocess

def record_topics(bag_path):
    topics = [
    # '/tf_static',
    # '/camera/rgb/image_raw',
    # '/camera/rgb/camera_info',
    # '/camera/depth/image_rect',
    # '/camera/depth/camera_info',
    # '/scan',
    # '/tf'
    # '/tf' ,
    # '/map',
      # '/camera/depth/image_rect',
      
      # '/head_camera/color/image_raw',
      # '/camera/depth_registered/points',
      #   '/camera/rgb/image_raw',
      #     '/move_group/monitored_planning_scene',
      #       '/tf_static',
      #         '/mobile/odom',
      #           '/joint_states',
      #             '/amcl_pose',
      #               '/odom_combined',
      #                 '/odom'
      '/camera/rgb/image_raw',
      '/camera/depth/image_raw'

        ]  # 指定要录制的话题列表

    # 构建 rosbag record 命令
    command = ['rosbag', 'record', '-O', bag_path ,'--split','--size=1024'] + topics

    # 执行命令
    subprocess.call(command)

if __name__ == '__main__':
    bag_path = '/home/reeman/JacobiWorkspace/rosbag_record/lab_for_video/image8/image.bag'  # 指定数据包的保存路径
    record_topics(bag_path)
