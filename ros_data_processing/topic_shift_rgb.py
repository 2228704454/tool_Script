import rospy
import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os

# 输入bag文件路径
bag_files = [
    '/home/jacobi/data/rosbag_record/lab_for_video/hand/image8/image_0.bag'
    # '/home/jacobi/data/rosbag_record/lab_for_video/hand/image4/image_1.bag'
]

# 输出深度图像集的文件夹路径
depth_output_folder = '/home/jacobi/data/rosbag_record/lab_for_video/hand/image8/overall2/depth'

# 输出彩色图像集的文件夹路径
rgb_output_folder = '/home/jacobi/data/rosbag_record/lab_for_video/hand/image8/overall2/rgb'

# 创建输出文件夹
if not os.path.exists(depth_output_folder):
    os.makedirs(depth_output_folder)

if not os.path.exists(rgb_output_folder):
    os.makedirs(rgb_output_folder)

# 创建CvBridge对象
bridge = CvBridge()

# 定义回调函数来处理图像消息
def image_callback(msg, topic):
    try:
        # 将ROS图像消息转换为OpenCV图像
        cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")

        # 生成图像文件名
        image_file = os.path.join(depth_output_folder if "depth" in topic else rgb_output_folder, topic[1:].replace('/', '_') + "_" + str(msg.header.stamp) + ".jpg")

        # 保存图像
        cv2.imwrite(image_file, cv_image)

        print("Saved image: ", image_file)

    except Exception as e:
        print(e)

# 遍历所有bag文件
for bag_file in bag_files:
    # 读取bag文件
    bag = rosbag.Bag(bag_file)

    # 遍历bag文件中的消息
    for topic, msg, t in bag.read_messages():
        if topic == "/camera/depth/image_raw" or topic == "/camera/rgb/image_raw":
            # 处理图像消息
            image_callback(msg, topic)

    # 关闭bag文件
    bag.close()
