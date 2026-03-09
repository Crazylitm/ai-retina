# AI Retina

**A Biomimetic Vision Frontend Inspired by the Human Retina**

> Artificial retina vision system for exploring bio-inspired visual preprocessing, event-based vision, and low-power intelligent perception.

---

## 1. 项目简介

AI Retina 是一个探索性项目，目标是模拟 **人类视网膜（Retina）** 的早期视觉计算机制。

在人类视觉系统中：

```
光子 → 视网膜 → 视神经 → 大脑视觉皮层 → 认知
```

视网膜并不是一个简单的"摄像头"，而是一个 **高效的神经计算前端**，会在信号进入大脑之前完成大量预处理，例如：

- 边缘检测
- 对比增强
- 亮度变化检测
- 运动检测
- 稀疏编码

AI Retina 项目的目标是：

> 使用普通摄像头 + Python 实现一个 **仿生视觉前端**，将连续图像转换为更接近生物视觉系统的 **特征流 / 事件流**。

---

## 2. 为什么要做这个项目

传统计算机视觉流程：

```
摄像头
  ↓
完整图像
  ↓
神经网络
  ↓
识别
```

问题：

- 数据量巨大
- 冗余信息很多
- 算力消耗大
- 延迟高

而生物视觉系统使用：

```
光子
  ↓
视网膜计算
  ↓
特征编码
  ↓
大脑识别
```

视网膜只输出 **最重要的信息**：

- 边缘
- 对比
- 运动
- 变化

AI Retina 的研究目标是验证：

> 如果 AI 系统也使用类似的前端结构，是否可以获得更高效、更鲁棒的视觉能力。

---

## 3. 项目目标

AI Retina V1 将实现以下模块：

### 1. 中心-周围感受野

模拟视网膜的空间对比增强。

实现方法：

```
Difference of Gaussian (DoG)
```

作用：

- 突出边缘
- 抑制平坦区域

### 2. ON / OFF 通道

模拟视网膜对亮度变化的双通路处理。

```
ON  → 变亮
OFF → 变暗
```

作用：

- 提高动态变化敏感度

### 3. 时间变化检测

检测视觉场景中的变化。

```
frame(t) - frame(t-1)
```

作用：

- 突出运动物体
- 抑制静止背景

### 4. 事件视觉编码

将连续图像转换为类似 Event Camera 的事件流。

事件格式：

```
(x, y, timestamp, polarity)
```

其中：

```
polarity = +1 → 变亮
polarity = -1 → 变暗
```

---

## 4. 项目架构

```
摄像头 / 视频
        ↓
    AI Retina
        ↓
+-------------------+
| Center-Surround   |
| ON/OFF Channels   |
| Temporal Filter   |
| Event Encoder     |
+-------------------+
        ↓
Feature Stream / Event Stream
        ↓
下游 AI / 机器人 / 认知系统
```

---

## 5. 项目目录结构

```
ai-retina/
│
├── retina/
│   ├── dog_filter.py        # 中心-周围滤波
│   ├── on_off.py            # ON / OFF 通道
│   ├── temporal.py          # 时间变化检测
│   ├── event_encoder.py     # 事件流编码
│   └── utils.py
│
├── viz/
│   └── dashboard.py         # 可视化面板
│
├── tasks/
│   └── motion_detect.py     # 验证任务
│
├── notebooks/               # 实验 notebook
│
├── data/                    # 视频数据
│
├── main.py                  # 主程序
├── requirements.txt
└── README.md
```

---

## 6. 环境安装

建议使用 Python 3.10+

安装依赖：

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
numpy
opencv-python
matplotlib
scipy
```

---

## 7. 运行项目

直接运行：

```bash
python main.py
```

系统会打开摄像头并显示：

- 原始图像
- DoG 边缘图
- ON 通道
- OFF / Motion
- 事件流

---

## 8. 第一个学习任务

建议你按以下顺序实现模块。

**Step 1** — 实现 `retina/dog_filter.py`，完成中心-周围感受野。

**Step 2** — 实现 `retina/on_off.py`，完成 ON / OFF 通道。

**Step 3** — 实现 `retina/temporal.py`，完成时间变化检测。

**Step 4** — 实现 `retina/event_encoder.py`，完成事件流编码。

**Step 5** — 实现 `viz/dashboard.py`，完成可视化面板。

---

## 9. 验证任务

AI Retina 的一个简单验证任务：

### 运动目标检测

对比两种方法：

**方法 A** — 直接使用原始视频。

**方法 B** — 使用 AI Retina 输出：

- 边缘
- ON/OFF
- 事件流

比较：

- 稳定性
- 抗光照能力
- 算力需求

---

## 10. 项目路线图

| Version | Focus | Key Features |
|---------|-------|-------------|
| **V1** | 仿生视网膜前端 | DoG, ON/OFF, Temporal filter, Event encoding |
| **V2** | 多尺度视觉 | 多层感受野, 方向选择, 颜色对手通道 |
| **V3** | 机器人视觉 | 接入 ROS, 接入机械臂, 低功耗视觉 |
| **V4** | 神经编码研究 | Spike-based vision, Population coding, Brain-inspired perception |
| **V5** | 脑机接口视觉前端 | AI Retina → 神经编码 → 脑机接口 → 视觉皮层 |

---

## 11. 参考资料

经典视觉神经科学书籍：

- **Principles of Neural Science** — Eric Kandel
- **Vision Science** — Stephen Palmer
- **Theoretical Neuroscience** — Peter Dayan

---

## 12. 项目愿景

AI Retina 的长期目标是探索：

> **生物视觉 + 人工智能 + 低功耗计算**

是否可以构建下一代 **高效智能视觉系统**。

这个项目既是：

- 工程实验
- 科学探索
- 长期个人技术研究

---

## 13. 更新日志

### V1.0.0 — 2026-03-09 | 核心模块实现

所有 V1 仿生视网膜前端模块已实现，可通过摄像头实时运行完整 pipeline。

#### 已实现的模块

**`retina/dog_filter.py` — 中心-周围感受野 (DoG)**

- 使用 `cv2.GaussianBlur` 实现 Difference of Gaussian
- 支持自定义 `sigma_center`（默认 1.0）和 `sigma_surround`（默认 3.0）
- 输出浮点数差分图像，突出边缘、抑制平坦区域

**`retina/on_off.py` — ON / OFF 通道**

- 计算相邻帧的亮度差异
- ON 通道：`max(current - previous, 0)` — 变亮区域
- OFF 通道：`max(previous - current, 0)` — 变暗区域

**`retina/temporal.py` — 时间变化检测**

- 使用 `cv2.absdiff` 计算帧间差异
- 阈值化生成二值运动掩码（默认阈值 15）
- 形态学操作（开运算 + 膨胀）去噪

**`retina/event_encoder.py` — 事件流编码**

- 将帧差异转换为 `(x, y, timestamp, polarity)` 事件元组
- `polarity = +1`（变亮） / `polarity = -1`（变暗）
- 新增 `render_events()` 函数：ON 事件显示为绿色，OFF 事件显示为红色

**`viz/dashboard.py` — 可视化面板**

- 2×3 网格布局，同时显示 6 个面板：
  - 原始画面 | DoG 边缘图 | ON 通道（绿色）
  - OFF 通道（红色）| 事件流可视化 | 信息面板
- 每个面板带标签，自动缩放

**`main.py` — 主程序入口**

- 支持命令行参数 `--cam N` 选择摄像头
- 完整 pipeline：灰度化 → DoG → ON/OFF → 时间变化 → 事件编码 → Dashboard
- 实时 FPS 和事件数显示
- 按 `q` 键退出

**`retina/utils.py` — 工具函数**

- `to_grayscale()` — BGR 转灰度
- `normalize()` — 归一化到 0-255 范围

#### 新增文件

- `retina/__init__.py` — Python 包初始化
- `viz/__init__.py` — Python 包初始化
- `tasks/__init__.py` — Python 包初始化

#### 运行方式

```bash
# 安装依赖
pip install -r requirements.txt

# 使用默认摄像头
python3 main.py

# 指定摄像头索引（例如 Logitech 外接摄像头）
python3 main.py --cam 1
```

> **注意：** macOS 用户需在 **系统设置 → 隐私与安全性 → 摄像头** 中授权 Terminal 访问摄像头。

---

## 14. 作者

**Mike Li**
AI / Robotics / Vision Exploration
