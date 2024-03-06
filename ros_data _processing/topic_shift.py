import rosbag
import rospy
from cv_bridge import CvBridge
import cv2
import os
os.environ['LD_PRELOAD'] = '/usr/lib/x86_64-linux-gnu/libp11-kit.so.0'

bag_file = [
    '/home/jacobi/data/rosbag_record/lab_for_video/hand/image2/image_0.bag',
    '/home/jacobi/data/rosbag_record/lab_for_video/hand/image2/image_1.bag'
    
] # 替换成你的bag文件路径


rgb_output_dir = '/home/jacobi/data/rosbag_record/lab_for_video/hand/image2/fourth_floor/rgb/'  # 替换成保存彩色图像的文件夹路径
depth_output_dir = '/home/jacobi/data/rosbag_record/lab_for_video/hand/image2/fourth_floor/depth/'  # 替换成保存深度图像的文件夹路径

# 创建输出文件夹
import os
os.makedirs(rgb_output_dir, exist_ok=True)
os.makedirs(depth_output_dir, exist_ok=True)

# 初始化ROS节点
rospy.init_node('bag_to_images')

# 创建cv_bridge对象
bridge = CvBridge()

# 遍历每个bag文件
for bag_path in bag_file:
    # 打开bag文件
    bag = rosbag.Bag(bag_path)

    # 遍历bag文件中的消息
    for topic, msg, t in bag.read_messages(topics=['/camera/color/image_raw', '/camera/depth/image_raw']):
        # 从彩色图像消息中提取图像并保存到彩色图像文件夹
        if topic == '/camera/rgb/image_raw':
            cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            output_path = os.path.join(rgb_output_dir, f'rgb_{str(t)}.jpg')
            cv2.imwrite(output_path, cv_image)
            print(f'Saved RGB image: {output_path}')

        # 从深度图像消息中提取图像并保存到深度图像文件夹
        if topic == '/camera/depth/image_raw':
            cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
            output_path = os.path.join(depth_output_dir, f'depth_{str(t)}.png')
            cv2.imwrite(output_path, cv_image)
            print(f'Saved depth image: {output_path}')

    # 关闭当前的bag文件
    bag.close()

print('转换完成！')






