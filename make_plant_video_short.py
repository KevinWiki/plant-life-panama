#!/usr/bin/env python3
# 快速版 - 10张 × 1秒 无字幕 静音

import subprocess
import os

# 图片顺序 - 完全按你发的顺序
source_images = [
    "/root/.openclaw/media/inbound/620fd4de-f45d-41ee-9480-c235fe10e1f7.jpg",  # 1. 红叶植物+蓝海城市天际线
    "/root/.openclaw/media/inbound/1899dec4-257c-4734-81d9-f29d817f7080.jpg",  # 2. 黄斑绿萝叶片特写
    "/root/.openclaw/media/inbound/4c842135-b958-4ec6-bb58-70ce6d24e78f.jpg",  # 3. 绿萝成长相框
    "/root/.openclaw/media/inbound/eb303ccd-140c-4953-aaa1-eec49c701211.jpg",  # 4. 开花植物特写
    "/root/.openclaw/media/inbound/1eb4cc04-9436-4d0f-8960-165b78c96f7b.jpg",  # 5. 鹿角蕨上墙
    "/root/.openclaw/media/inbound/4ec4da8e-d0bb-4e89-b083-ed761f855374.jpg",  # 6. 发财树
    "/root/.openclaw/media/inbound/fcfdb9da-d931-4400-94f1-2bc127a3b7c7.jpg",  # 7. 黄金绿萝柜顶
    "/root/.openclaw/media/inbound/4054a308-b3bf-40b6-8a35-08af7dda30ef.jpg",  # 8. 水培靠窗
    "/root/.openclaw/media/inbound/c751e23b-95c9-4228-9c0a-d042d9f1705b.jpg",  # 9. 黄斑绿萝爬柱子+海景
    "/root/.openclaw/media/inbound/690b31e2-8571-4216-b209-e0030b58ef3c.jpg",  # 10. 四层植物全景 收官
]

# 每张1秒
duration_per_image = 1

os.makedirs("/tmp/plant_video_short", exist_ok=True)

# 复制并重命名
for i, src in enumerate(source_images):
    dst = f"/tmp/plant_video_short/{i+1}.jpg"
    subprocess.run(["cp", src, dst], check=True)

# 生成concat文件
with open("/tmp/plant_video_short/concat.txt", "w") as f:
    for i in range(len(source_images)):
        img = f"{i+1}.jpg"
        f.write(f"file '{img}'\n")
        f.write(f"duration {duration_per_image}\n")

# 生成静音视频 - 你自己加音乐
cmd = [
    "ffmpeg", "-y",
    "-f", "concat", "-safe", "0", "-i", "/tmp/plant_video_short/concat.txt",
    "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
    "-vf", "scale=1080:1920",
    "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p",
    "/tmp/plant_video_short/plant-life-10s.mp4"
]

print("开始生成短视频...")
subprocess.run(cmd, check=True)
print("短视频生成完成")

size = os.path.getsize("/tmp/plant_video_short/plant-life-10s.mp4") / (1024*1024)
print(f"文件大小: {size:.1f} MB")
