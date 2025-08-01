#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ant Design风格UI样式定义
"""

from PyQt6.QtCore import QObject, pyqtSignal
from utils.logger import logger


class AntColors:
    """Ant Design 颜色系统 - 浅色主题"""

    # 主色系
    PRIMARY_1 = "#e6f7ff"  # 最浅蓝
    PRIMARY_2 = "#bae7ff"  # 浅蓝
    PRIMARY_3 = "#91d5ff"  # 较浅蓝
    PRIMARY_4 = "#69c0ff"  # 中浅蓝
    PRIMARY_5 = "#40a9ff"  # 中蓝
    PRIMARY_6 = "#1890ff"  # 主蓝色
    PRIMARY_7 = "#096dd9"  # 中深蓝
    PRIMARY_8 = "#0050b3"  # 深蓝
    PRIMARY_9 = "#003a8c"  # 较深蓝
    PRIMARY_10 = "#002766"  # 最深蓝

    # 成功色系
    SUCCESS_1 = "#f6ffed"  # 最浅绿
    SUCCESS_2 = "#d9f7be"  # 浅绿
    SUCCESS_3 = "#b7eb8f"  # 较浅绿
    SUCCESS_4 = "#95de64"  # 中浅绿
    SUCCESS_5 = "#73d13d"  # 中绿
    SUCCESS_6 = "#52c41a"  # 主绿色
    SUCCESS_7 = "#389e0d"  # 中深绿
    SUCCESS_8 = "#237804"  # 深绿
    SUCCESS_9 = "#135200"  # 较深绿
    SUCCESS_10 = "#092b00"  # 最深绿

    # 警告色系
    WARNING_1 = "#fffbe6"  # 最浅橙
    WARNING_2 = "#fff1b8"  # 浅橙
    WARNING_3 = "#ffe58f"  # 较浅橙
    WARNING_4 = "#ffd666"  # 中浅橙
    WARNING_5 = "#ffc53d"  # 中橙
    WARNING_6 = "#faad14"  # 主橙色
    WARNING_7 = "#d48806"  # 中深橙
    WARNING_8 = "#ad6800"  # 深橙
    WARNING_9 = "#874d00"  # 较深橙
    WARNING_10 = "#613400"  # 最深橙

    # 错误色系
    ERROR_1 = "#fff2f0"  # 最浅红
    ERROR_2 = "#ffccc7"  # 浅红
    ERROR_3 = "#ffa39e"  # 较浅红
    ERROR_4 = "#ff7875"  # 中浅红
    ERROR_5 = "#ff4d4f"  # 中红
    ERROR_6 = "#f5222d"  # 主红色
    ERROR_7 = "#cf1322"  # 中深红
    ERROR_8 = "#a8071a"  # 深红
    ERROR_9 = "#820014"  # 较深红
    ERROR_10 = "#5c0011"  # 最深红

    # 中性色系
    GRAY_1 = "#ffffff"  # 白色
    GRAY_2 = "#fafafa"  # 最浅灰
    GRAY_3 = "#f5f5f5"  # 浅灰
    GRAY_4 = "#f0f0f0"  # 较浅灰
    GRAY_5 = "#d9d9d9"  # 中浅灰
    GRAY_6 = "#bfbfbf"  # 中灰
    GRAY_7 = "#8c8c8c"  # 中深灰
    GRAY_8 = "#595959"  # 深灰
    GRAY_9 = "#434343"  # 较深灰
    GRAY_10 = "#262626"  # 最深灰
    GRAY_11 = "#1f1f1f"  # 近黑
    GRAY_12 = "#141414"  # 黑色
    GRAY_13 = "#000000"  # 纯黑


class AntColorsDark:
    """Ant Design 颜色系统 - 深色主题"""

    # 主色系 (保持相对一致，稍微调亮)
    PRIMARY_1 = "#111b26"  # 最深蓝背景
    PRIMARY_2 = "#112545"  # 深蓝背景
    PRIMARY_3 = "#15325b"  # 较深蓝背景
    PRIMARY_4 = "#1554ad"  # 中深蓝
    PRIMARY_5 = "#1668dc"  # 中蓝
    PRIMARY_6 = "#1890ff"  # 主蓝色 (保持)
    PRIMARY_7 = "#40a9ff"  # 较亮蓝
    PRIMARY_8 = "#69c0ff"  # 亮蓝
    PRIMARY_9 = "#91d5ff"  # 很亮蓝
    PRIMARY_10 = "#bae7ff"  # 最亮蓝

    # 成功色系
    SUCCESS_1 = "#162312"  # 最深绿背景
    SUCCESS_2 = "#1b2618"  # 深绿背景
    SUCCESS_3 = "#274b32"  # 较深绿背景
    SUCCESS_4 = "#389e0d"  # 中深绿
    SUCCESS_5 = "#52c41a"  # 主绿色 (保持)
    SUCCESS_6 = "#73d13d"  # 较亮绿
    SUCCESS_7 = "#95de64"  # 亮绿
    SUCCESS_8 = "#b7eb8f"  # 很亮绿
    SUCCESS_9 = "#d9f7be"  # 最亮绿
    SUCCESS_10 = "#f6ffed"  # 绿色高亮

    # 警告色系
    WARNING_1 = "#2b1d11"  # 最深橙背景
    WARNING_2 = "#342209"  # 深橙背景
    WARNING_3 = "#593716"  # 较深橙背景
    WARNING_4 = "#ad6800"  # 中深橙
    WARNING_5 = "#d48806"  # 中橙
    WARNING_6 = "#faad14"  # 主橙色 (保持)
    WARNING_7 = "#ffc53d"  # 较亮橙
    WARNING_8 = "#ffd666"  # 亮橙
    WARNING_9 = "#ffe58f"  # 很亮橙
    WARNING_10 = "#fff1b8"  # 最亮橙

    # 错误色系
    ERROR_1 = "#2a1215"  # 最深红背景
    ERROR_2 = "#431418"  # 深红背景
    ERROR_3 = "#58181c"  # 较深红背景
    ERROR_4 = "#a8071a"  # 中深红
    ERROR_5 = "#cf1322"  # 中红
    ERROR_6 = "#f5222d"  # 主红色 (保持)
    ERROR_7 = "#ff4d4f"  # 较亮红
    ERROR_8 = "#ff7875"  # 亮红
    ERROR_9 = "#ffa39e"  # 很亮红
    ERROR_10 = "#ffccc7"  # 最亮红

    # 中性色系 (反转)
    GRAY_1 = "#141414"  # 深色背景
    GRAY_2 = "#1f1f1f"  # 较深背景
    GRAY_3 = "#262626"  # 中深背景
    GRAY_4 = "#434343"  # 较浅背景
    GRAY_5 = "#595959"  # 中浅灰
    GRAY_6 = "#8c8c8c"  # 中灰
    GRAY_7 = "#bfbfbf"  # 中亮灰
    GRAY_8 = "#d9d9d9"  # 亮灰
    GRAY_9 = "#f0f0f0"  # 很亮灰
    GRAY_10 = "#f5f5f5"  # 最亮灰
    GRAY_11 = "#fafafa"  # 近白
    GRAY_12 = "#ffffff"  # 白色
    GRAY_13 = "#ffffff"  # 纯白


class ThemeManager(QObject):
    """主题管理器"""

    # 主题切换信号
    theme_changed = pyqtSignal(str)  # 发送新主题名称

    def __init__(self):
        super().__init__()
        self._current_theme = "light"
        self._light_stylesheet = None
        self._dark_stylesheet = None
        self._generate_stylesheets()

    def _generate_stylesheets(self):
        """预生成浅色和深色两套完整样式表"""
        # 生成浅色主题样式表
        self._light_stylesheet = self._build_complete_stylesheet(AntColors)

        # 生成深色主题样式表
        self._dark_stylesheet = self._build_complete_stylesheet(AntColorsDark)

    def _build_complete_stylesheet(self, colors):
        """构建完整的样式表"""
        return f"""
        /* === 全局样式 === */
        * {{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Segoe UI Variable', 'Microsoft YaHei UI', 'Microsoft YaHei', '微软雅黑', 'PingFang SC', 'Hiragino Sans GB', 'Source Han Sans SC', 'Noto Sans CJK SC', 'WenQuanYi Micro Hei', Ubuntu, Roboto, 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: 13px;  /* 全局基础字体大小 */
            font-weight: 400; /* 全局基础字体粗细 */
        }}

        /* === 基础组件样式 === */
        QGroupBox, QScrollArea, QFrame, QWidget {{
            background-color: transparent;
            color: {colors.GRAY_9};
        }}


        /* === 自定义标题栏 === */
        CustomTitleBar {{
            background-color: {colors.GRAY_1};
            border: none;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            border-bottom: 1px solid {colors.GRAY_4};
        }}
        
        CustomTitleBar QLabel {{
            font-size: 15px;  /* 标题栏字体稍大 */
            font-weight: 600; /* 保持中等粗细 */
            color: {colors.GRAY_9};
        }}
        
        /* === 按钮样式 === */
        QPushButton {{
            background-color: {colors.PRIMARY_6};
            color: {"#ffffff" if colors == AntColors else colors.GRAY_13};
            border: 1px solid {colors.PRIMARY_6};
            border-radius: 4px;
            padding: 4px 10px;
            font-weight: 500; /* 中等粗细，确保可读性 */
            font-size: 13px;  /* 稍大的字体提高可读性 */
            min-height: 28px; /* 增加高度以适应更大字体 */
            outline: none;
        }}
        
        QPushButton:hover {{
            background-color: {colors.PRIMARY_5};
            border-color: {colors.PRIMARY_5};
        }}
        
        QPushButton:pressed {{
            background-color: {colors.PRIMARY_7};
            border-color: {colors.PRIMARY_7};
        }}
        
        QPushButton:disabled {{
            background-color: {colors.GRAY_3};
            color: {colors.GRAY_6};
            border-color: {colors.GRAY_4};
        }}
        
        QPushButton:focus {{
            border-color: {colors.PRIMARY_6};
            border-width: 2px;
        }}
        
        /* 按钮变体 */
        QPushButton[buttonType="success"] {{
            background-color: {colors.SUCCESS_6};
            border-color: {colors.SUCCESS_6};
            color: {"#ffffff" if colors == AntColors else colors.GRAY_13};
        }}
        
        QPushButton[buttonType="success"]:hover {{
            background-color: {colors.SUCCESS_5};
            border-color: {colors.SUCCESS_5};
        }}
        
        QPushButton[buttonType="warning"] {{
            background-color: {colors.WARNING_6};
            border-color: {colors.WARNING_6};
            color: {"#ffffff" if colors == AntColors else colors.GRAY_13};
        }}
        
        QPushButton[buttonType="warning"]:hover {{
            background-color: {colors.WARNING_5};
            border-color: {colors.WARNING_5};
        }}
        
        QPushButton[buttonType="danger"] {{
            background-color: {colors.ERROR_6};
            border-color: {colors.ERROR_6};
            color: {"#ffffff" if colors == AntColors else colors.GRAY_13};
        }}
        
        QPushButton[buttonType="danger"]:hover {{
            background-color: {colors.ERROR_5};
            border-color: {colors.ERROR_5};
        }}
        
        QPushButton[buttonType="default"] {{
            background-color: {colors.GRAY_1};
            color: {colors.GRAY_9};
            border-color: {colors.GRAY_5};
        }}
        
        QPushButton[buttonType="default"]:hover {{
            background-color: {colors.GRAY_2};
            border-color: {colors.PRIMARY_5};
        }}
        
        /* 选中状态的按钮样式 */
        QPushButton[buttonType="selected"] {{
            background-color: {colors.PRIMARY_1};
            color: {colors.PRIMARY_7};
            border-color: {colors.PRIMARY_6};
            border-width: 2px;
            font-weight: 600; /* 选中状态保持较粗字体 */
            font-size: 13px;  /* 与普通按钮保持一致 */
        }}
        
        QPushButton[buttonType="selected"]:hover {{
            background-color: {colors.PRIMARY_2};
            border-color: {colors.PRIMARY_5};
        }}
        
        QPushButton[buttonType="selected"]:pressed {{
            background-color: {colors.PRIMARY_3};
            border-color: {colors.PRIMARY_7};
        }}
        
        /* === 输入框样式 === */
        QLineEdit {{
            background-color: {colors.GRAY_1};
            border: 1px solid {colors.GRAY_5};
            border-radius: 4px;
            padding: 4px 8px;
            font-size: 13px;  /* 与全局基础字体保持一致 */
            font-weight: 400; /* 正常粗细 */
            color: {colors.GRAY_9};
            min-height: 28px;  /* 增加高度以适应更大字体 */
        }}
        
        QLineEdit:hover {{
            border-color: {colors.PRIMARY_5};
        }}
        
        QLineEdit:focus {{
            border-color: {colors.PRIMARY_6};
            outline: none;
            border-width: 2px;
        }}
        
        QLineEdit:disabled {{
            background-color: {colors.GRAY_3};
            color: {colors.GRAY_6};
            border-color: {colors.GRAY_4};
        }}
        
        /* === 下拉框样式 === */
        QComboBox {{
            background-color: {colors.GRAY_1};
            border: 1px solid {colors.GRAY_5};
            border-radius: 4px;
            padding: 4px 8px;
            font-size: 13px;  /* 与全局基础字体保持一致 */
            font-weight: 400; /* 正常粗细 */
            color: {colors.GRAY_9};
            min-width: 100px;
            min-height: 28px;  /* 增加高度以适应更大字体 */
        }}
        
        QComboBox:hover {{
            border-color: {colors.PRIMARY_5};
        }}
        
        QComboBox:focus {{
            border-color: {colors.PRIMARY_6};
            outline: none;
            border-width: 1px;
        }}
        
        QComboBox::drop-down {{
            border: none;
            width: 20px;
            padding-right: 8px;
        }}
        
        QComboBox::down-arrow {{
            image: url(assets/icon/arrow-down.svg);
            width: 8px;
            height: 6px;
        }}
        
        QComboBox QAbstractItemView {{
            background-color: {colors.GRAY_1};
            border: 1px solid {colors.GRAY_4};
            border-radius: 4px;
            selection-background-color: {colors.PRIMARY_1};
            selection-color: {colors.PRIMARY_7};
            padding: 2px;
            outline: none;
        }}
        
        QComboBox QAbstractItemView::item {{
            height: 26px;
            padding: 4px 8px;
            border: none;
            border-radius: 3px;
            color: {colors.GRAY_9};
        }}
        
        QComboBox QAbstractItemView::item:hover {{
            background-color: {colors.GRAY_2};
        }}
        
        QComboBox QAbstractItemView::item:selected {{
            background-color: {colors.PRIMARY_1};
            color: {colors.PRIMARY_7};
        }}
        
        
        /* === 单选按钮样式 === */
        QRadioButton {{
            font-size: 13px;  /* 与全局基础字体保持一致 */
            font-weight: 400; /* 正常粗细 */
            color: {colors.GRAY_9};
            spacing: 6px;
            background-color: transparent;
        }}
        
        QRadioButton::indicator {{
            width: 12px;
            height: 12px;
            border-radius: 7px;
            border: 1px solid {colors.GRAY_5};
            background-color: {colors.GRAY_1};
        }}
        
        QRadioButton::indicator:hover {{
            border-color: {colors.PRIMARY_6};
        }}
        
        QRadioButton::indicator:checked {{
            width: 12px;
            height: 12px;
            border-radius: 7px;
            border: 2px solid {colors.PRIMARY_6};
            background-color: {colors.GRAY_1};
            /* 使用radial-gradient创建内部圆点 */
            background: qradialgradient(cx:0.5, cy:0.5, radius:0.45, fx:0.5, fy:0.5, 
                stop:0 {colors.PRIMARY_6}, 
                stop:0.5 {colors.PRIMARY_6}, 
                stop:0.6 {colors.GRAY_1}, 
                stop:1 {colors.GRAY_1});
        }}
        
        QRadioButton::indicator:checked:hover {{
            border-color: {colors.PRIMARY_5};
            background: qradialgradient(cx:0.5, cy:0.5, radius:0.45, fx:0.5, fy:0.5, 
                stop:0 {colors.PRIMARY_5}, 
                stop:0.5 {colors.PRIMARY_5}, 
                stop:0.6 {colors.GRAY_1}, 
                stop:1 {colors.GRAY_1});
        }}
        
        QRadioButton::indicator:disabled {{
            background-color: {colors.GRAY_3};
            border-color: {colors.GRAY_4};
        }}
        
        QRadioButton::indicator:checked:disabled {{
            border-color: {colors.GRAY_4};
            background: qradialgradient(cx:0.5, cy:0.5, radius:0.45, fx:0.5, fy:0.5, 
                stop:0 {colors.GRAY_6}, 
                stop:0.5 {colors.GRAY_6}, 
                stop:0.6 {colors.GRAY_3}, 
                stop:1 {colors.GRAY_3});
        }}
        
        /* === 进度条样式 === */
        QProgressBar {{
            border: none;
            border-radius: 3px;
            background-color: {colors.GRAY_3};
            text-align: center;
            font-size: 12px;  /* 稍大的字体提高可读性 */
            font-weight: 500; /* 中等粗细确保清晰 */
            color: {colors.GRAY_8};
            max-height: 18px;  /* 增加高度以适应更大字体 */
        }}
        
        QProgressBar::chunk {{
            border-radius: 3px;
            background-color: {colors.PRIMARY_6};
        }}
        
        /* 内存进度条变体 */
        QProgressBar[progressType="memory-low"]::chunk {{
            background-color: {colors.SUCCESS_6};
        }}
        
        QProgressBar[progressType="memory-medium"]::chunk {{
            background-color: {colors.WARNING_6};
        }}
        
        QProgressBar[progressType="memory-high"]::chunk {{
            background-color: {colors.ERROR_6};
        }}
        
        /* === 分组框样式 === */
        QGroupBox {{
            font-size: 14px;  /* 分组框标题稍大 */
            font-weight: 600; /* 保持较粗字体突出层次 */
            color: {colors.GRAY_9};
            background-color: {colors.GRAY_1};
            border: 1px solid {colors.GRAY_4};
            border-radius: 6px;
            margin-top: 8px;
            padding-top: 8px;
        }}
        
        QGroupBox::title {{
            subcontrol-origin: margin;
            subcontrol-position: top center;
            padding: 0px 5px;
            background-color: {colors.GRAY_1};
            color: {colors.GRAY_9};
        }}

        /* === 导航按钮样式 === */
        /* NavigationButton 基础样式 - Fluent Design风格 */

        NavigationButton {{
            border-radius: 6px;
            text-align: left;
            padding: 12px 16px 12px 22px;  /* 左侧留出更多指示器空间 */
            margin: 2px 4px 2px 10px;  /* 左侧留出更多指示器空间 */
            min-width: 50px;
            min-height: 30px;
            border: none;
            /* 字体样式移到QLabel中统一管理 */
        }}

        /* NavigationButton 未激活状态 */
        NavigationButton[buttonState="inactive"] {{
            background-color: transparent;
            color: {colors.GRAY_9};
        }}

        NavigationButton[buttonState="inactive"]:hover {{
            background-color: {colors.GRAY_3};
            color: {colors.GRAY_9};
        }}

        NavigationButton[buttonState="inactive"]:pressed {{
            background-color: {colors.GRAY_4};
        }}

        /* NavigationButton 激活状态 - 更柔和的Fluent风格 */
        NavigationButton[buttonState="active"] {{
            background-color: {colors.PRIMARY_1};
            color: {colors.PRIMARY_6};
            /* 字体粗细在QLabel中设置 */
        }}

        NavigationButton[buttonState="active"]:hover {{
            background-color: {colors.PRIMARY_2};
            color: {colors.PRIMARY_6};
        }}

        NavigationButton[buttonState="active"]:pressed {{
            background-color: {colors.PRIMARY_3};
        }}

        /* NavigationButton 内部标签样式 */
        NavigationButton QLabel {{
            background-color: transparent;
            border: none;
            font-size: 14px;  /* 导航按钮字体稍大提高可读性 */
            font-weight: 500; /* 中等粗细 */
        }}

        /* NavigationButton 激活状态的内部标签加粗 */
        NavigationButton[buttonState="active"] QLabel {{
            font-weight: 600; /* 激活状态更粗突出当前选择 */
            font-size: 14px;  /* 与未激活状态保持一致 */
        }}

        /* 导航容器样式 - Fluent Design风格 */
        QWidget[navType="vertical"] {{
            background-color: {colors.GRAY_1};
            border-radius: 8px;
            border: 1px solid {colors.GRAY_3};
        }}

        /* 导航内容区域样式 */
        QStackedWidget[contentType="navigation"] {{
            background-color: {colors.GRAY_1};
            border-radius: 8px;
            border: 1px solid {colors.GRAY_3};
        }}

        /* 导航滚动区域样式 */
        QScrollArea[contentType="navigation"] {{
            background-color: {colors.GRAY_1};
            border: none;
            border-radius: 8px;
        }}

        QScrollArea[contentType="navigation"] QScrollBar:vertical {{
            background-color: {colors.GRAY_2};
            width: 8px;
            border-radius: 4px;
            margin: 0px;
        }}

        QScrollArea[contentType="navigation"] QScrollBar::handle:vertical {{
            background-color: {colors.GRAY_5};
            border-radius: 4px;
            min-height: 20px;
        }}

        QScrollArea[contentType="navigation"] QScrollBar::handle:vertical:hover {{
            background-color: {colors.GRAY_6};
        }}

        QScrollArea[contentType="navigation"] QScrollBar::add-line:vertical,
        QScrollArea[contentType="navigation"] QScrollBar::sub-line:vertical {{
            height: 0px;
        }}

        /* Logo文字样式 */
        QLabel[objectName="logo_text_label"] {{
            font-size: 16px;  /* Logo文字稍大突出品牌 */
            font-weight: 700; /* 更粗的字体突出Logo */
            text-align: center;
            background-color: transparent;
        }}

        /* Logo图标样式 */
        QLabel[objectName="logo_icon_label"] {{
            background-color: {colors.PRIMARY_6};
            color: white;
            border-radius: 8px;  /* 正方形圆角遮罩，与代码中的8px保持一致 */
            font-size: 26px;  /* 图标字体稍大 */
            font-weight: 700; /* 更粗的字体 */
            text-align: center;
            qproperty-alignment: AlignCenter;
        }}

        /* Logo图标图片模式样式 */
        QLabel[objectName="logo_icon_label"][logoType="image"] {{
            background-color: transparent;
            border-radius: 0px;  /* 移除圆角，显示原始图片 */
        }}

        /* Logo容器样式 */
        QWidget[objectName="logo_wrapper"] {{
            background-color: transparent;
        }}

        /* Logo图标容器样式 */
        QWidget[objectName="logo_icon_container"] {{
            background-color: transparent;
        }}

        /* Logo文字容器样式 */
        QWidget[objectName="logo_text_container"] {{
            background-color: transparent;
        }}


        /* === 标签样式 === */
        QLabel {{
            background-color: transparent;
            color: {colors.GRAY_9};
            font-size: 13px;  /* 与全局基础字体保持一致 */
            font-weight: 400; /* 正常粗细 */
            line-height: 1.4;
        }}
        
        /* 标签变体 */
        QLabel[labelType="info"] {{
            color: {colors.GRAY_7};
            padding: 6px 8px;
            background-color: {colors.GRAY_2};
            border: 1px solid {colors.GRAY_4};
            border-radius: 4px;
            margin: 3px 0;
        }}
        
        QLabel[labelType="success"] {{
            color: {colors.SUCCESS_7};
            padding: 6px 8px;
            background-color: {colors.SUCCESS_1};
            border: 1px solid {colors.SUCCESS_3};
            border-radius: 4px;
            margin: 3px 0;
        }}
        
        QLabel[labelType="warning"] {{
            color: {colors.WARNING_7};
            padding: 6px 8px;
            background-color: {colors.WARNING_1};
            border: 1px solid {colors.WARNING_3};
            border-radius: 4px;
            margin: 3px 0;
        }}
        
        QLabel[labelType="error"] {{
            color: {colors.ERROR_7};
            padding: 6px 8px;
            background-color: {colors.ERROR_1};
            border: 1px solid {colors.ERROR_3};
            border-radius: 4px;
            margin: 3px 0;
        }}
        
        QLabel[labelType="secondary"] {{
            color: {colors.GRAY_7};
        }}
        
        QLabel[labelType="small"] {{
            color: {colors.GRAY_8};
            font-size: 11px;  /* 小标签字体稍大提高可读性 */
            font-weight: 400; /* 正常粗细 */
            line-height: 1.3;
        }}
        
        /* === 数字输入框样式 === */
        QSpinBox {{
            background-color: {colors.GRAY_1};
            border: 1px solid {colors.GRAY_5};
            border-radius: 4px;
            padding: 4px 8px;
            font-size: 13px;  /* 与全局基础字体保持一致 */
            font-weight: 400; /* 正常粗细 */
            color: {colors.GRAY_9};
            min-height: 28px;  /* 增加高度以适应更大字体 */
        }}
        
        QSpinBox:hover {{
            border-color: {colors.PRIMARY_5};
        }}
        
        QSpinBox:focus {{
            border-color: {colors.PRIMARY_6};
            outline: none;
            border-width: 2px;
        }}
        
        QSpinBox::up-button, QSpinBox::down-button {{
            border: none;
            width: 16px;
            background-color: transparent;
            border-radius: 2px;
        }}
        
        QSpinBox::up-button:hover, QSpinBox::down-button:hover {{
            background-color: {colors.GRAY_2};
        }}
        
        QSpinBox::up-arrow {{
            image: url(assets/icon/arrow-up.svg);
            width: 8px;
            height: 6px;
        }}
        
        QSpinBox::down-arrow {{
            image: url(assets/icon/arrow-down.svg);
            width: 8px;
            height: 6px;
        }}
        
        QSpinBox::up-arrow:hover {{
            image: url(assets/icon/arrow-up.svg);
        }}
        
        QSpinBox::down-arrow:hover {{
            image: url(assets/icon/arrow-down.svg);
        }}
        
        /* === 表格样式 === */
        QTableWidget {{
            background-color: {colors.GRAY_1};
            border: 1px solid {colors.GRAY_4};
            border-radius: 6px;
            gridline-color: {colors.GRAY_4};
            selection-background-color: {colors.PRIMARY_1};
            font-size: 13px;  /* 表格内容与全局基础字体保持一致 */
            font-weight: 400; /* 正常粗细 */
        }}
        
        QTableWidget::item {{
            padding: 8px 12px;
            border: none;
            border-bottom: 1px solid {colors.GRAY_3};
            color: {colors.GRAY_9};
        }}
        
        QTableWidget::item:selected {{
            background-color: {colors.PRIMARY_1};
            color: {colors.PRIMARY_7};
        }}
        
        QTableWidget::item:hover {{
            background-color: {colors.GRAY_2};
        }}
        
        QTableWidget::item:alternate {{
            background-color: {colors.GRAY_2};
        }}
        
        QHeaderView::section {{
            background-color: {colors.GRAY_2};
            color: {colors.GRAY_9};
            padding: 8px 12px;
            border: none;
            border-right: 1px solid {colors.GRAY_4};
            border-bottom: 1px solid {colors.GRAY_4};
            font-weight: 600; /* 表头保持较粗字体突出层次 */
            font-size: 13px;  /* 与表格内容保持一致 */
        }}
        
        QHeaderView::section:first {{
            border-top-left-radius: 6px;
        }}
        
        QHeaderView::section:last {{
            border-top-right-radius: 6px;
            border-right: none;
        }}
        
        QHeaderView::section:hover {{
            background-color: {colors.GRAY_3};
        }}
        
        /* === 滚动条样式 === */
        QScrollBar:vertical {{
            background: {colors.GRAY_3};
            width: 8px;
            border-radius: 4px;
            margin: 0px;
        }}
        
        QScrollBar::handle:vertical {{
            background: {colors.GRAY_6};
            border-radius: 4px;
            min-height: 20px;
        }}
        
        QScrollBar::handle:vertical:hover {{
            background: {colors.GRAY_7};
        }}
        
        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {{
            border: none;
            background: none;
        }}
        
        QScrollBar:horizontal {{
            background: {colors.GRAY_3};
            height: 8px;
            border-radius: 4px;
            margin: 0px;
        }}
        
        QScrollBar::handle:horizontal {{
            background: {colors.GRAY_6};
            border-radius: 4px;
            min-width: 20px;
        }}
        
        QScrollBar::handle:horizontal:hover {{
            background: {colors.GRAY_7};
        }}
        
        QScrollBar::add-line:horizontal,
        QScrollBar::sub-line:horizontal {{
            border: none;
            background: none;
        }}
        
        /* === 消息框和对话框样式 === */
        QMessageBox, QDialog {{
            background-color: {colors.GRAY_1};
            border-radius: 8px;
        }}

        /* === 菜单样式 === */
        QMenuBar {{
            background-color: {colors.GRAY_1};
            border-bottom: 1px solid {colors.GRAY_4};
            color: {colors.GRAY_9};
        }}
        
        QMenu {{
            background-color: {colors.GRAY_1};
            border: 1px solid {colors.GRAY_4};
            border-radius: 6px;
            padding: 4px;
        }}
        
        QMenu::item {{
            padding: 8px 16px;
            border-radius: 4px;
        }}
        
        QMenu::item:selected {{
            background-color: {colors.PRIMARY_1};
            color: {colors.PRIMARY_7};
        }}
        
        /* === 工具提示样式 === */
        QToolTip {{
            background-color: {colors.GRAY_10};
            color: {colors.GRAY_1};
            border: 1px solid {colors.GRAY_8};
            border-radius: 6px;
            padding: 8px;
            font-size: 12px;  /* 工具提示保持较小字体 */
            font-weight: 400; /* 正常粗细 */
        }}
        """

    def set_theme(self, theme: str):
        """设置主题并发送信号"""
        if theme != self._current_theme:
            self._current_theme = theme
            self.theme_changed.emit(theme)

    def get_current_theme(self) -> str:
        """获取当前主题"""
        return self._current_theme

    def get_stylesheet(self, theme: str = None) -> str:
        """获取指定主题的样式表"""
        if theme is None:
            theme = self._current_theme

        if theme == "dark":
            return self._dark_stylesheet
        else:
            return self._light_stylesheet

    def is_dark_theme(self, theme: str = None) -> bool:
        """判断是否为深色主题"""
        if theme is None:
            theme = self._current_theme
        return theme == "dark"


# 全局主题管理器实例
theme_manager = ThemeManager()


class StyleHelper:
    """样式辅助类"""

    @staticmethod
    def set_frameless_window_properties(window):
        """设置无边框窗口属性

        Args:
            window: QWidget实例
        """
        try:
            # 设置主窗口属性
            window.setProperty("windowType", "frameless")

            # 刷新样式
            window.style().unpolish(window)
            window.style().polish(window)
        except Exception as e:
            logger.error(f"设置无边框窗口属性失败: {e}")

    @staticmethod
    def set_button_type(button, button_type: str):
        """设置按钮类型

        Args:
            button: QPushButton实例
            button_type: 按钮类型 ('primary', 'success', 'warning', 'danger', 'default')
        """
        button.setProperty("buttonType", button_type)
        button.style().unpolish(button)
        button.style().polish(button)

    @staticmethod
    def set_label_type(label, label_type: str):
        """设置标签类型

        Args:
            label: QLabel实例
            label_type: 标签类型 ('info', 'success', 'warning', 'error', 'secondary', 'small')
        """
        label.setProperty("labelType", label_type)
        label.style().unpolish(label)
        label.style().polish(label)

    @staticmethod
    def set_progress_type(progressbar, progress_type: str):
        """设置进度条类型

        Args:
            progressbar: QProgressBar实例
            progress_type: 进度条类型 ('memory-low', 'memory-medium', 'memory-high')
        """
        progressbar.setProperty("progressType", progress_type)
        progressbar.style().unpolish(progressbar)
        progressbar.style().polish(progressbar)

    @staticmethod
    def set_checkbox_style(checkbox, check_style: str = "default"):
        """设置复选框勾选样式

        Args:
            checkbox: QCheckBox实例
            check_style: 勾选样式 ('default', 'unicode', 'simple')
                - default: 使用SVG图标文件 (推荐)
                - unicode: 使用Unicode字符 ✓
                - simple: 使用CSS绘制简单勾选标记
        """
        if check_style != "default":
            checkbox.setProperty("checkStyle", check_style)
        else:
            checkbox.setProperty("checkStyle", None)
        checkbox.style().unpolish(checkbox)
        checkbox.style().polish(checkbox)


class StatusHTMLGenerator:
    """状态HTML生成器"""

    @staticmethod
    def get_html_style(theme: str = None) -> str:
        """获取状态HTML的CSS样式"""
        if theme is None:
            theme = theme_manager.get_current_theme()

        colors = AntColorsDark if theme == "dark" else AntColors

        return f"""
        <style>
            .card {{
                margin: 5px 0;
                padding: 5px;
                border-radius: 8px;
                background-color: {colors.GRAY_1};
                border: 1px solid {colors.GRAY_4};
            }}
            .section-title {{
                font-size: 15px;  /* 状态标题稍大 */
                font-weight: 600; /* 保持较粗字体 */
                margin-bottom: 5px;
                color: {colors.GRAY_10};
                line-height: 1.5;
            }}
            .status-success {{
                color: {colors.SUCCESS_6};
                font-weight: 500;
            }}
            .status-warning {{
                color: {colors.WARNING_6};
                font-weight: 500;
            }}
            .status-error {{
                color: {colors.ERROR_6};
                font-weight: 500;
            }}
            .status-normal {{
                color: {colors.GRAY_8};
                font-weight: 500;
            }}
            .status-disabled {{
                color: {colors.GRAY_6};
                font-weight: 400;
            }}
            .status-item {{
                margin: 2px 0;
                line-height: 1.5;
                font-size: 12px;
            }}
            .update-time {{
                font-size: 12px;
                color: {colors.GRAY_7};
                text-align: right;
                margin-top: 12px;
                font-style: italic;
            }}
        </style>
        """


# === 颜色方案和辅助类 ===


class ColorScheme:
    """颜色方案 - 动态获取当前主题颜色"""

    @staticmethod
    def _get_colors():
        theme = theme_manager.get_current_theme()
        return AntColorsDark if theme == "dark" else AntColors

    @classmethod
    def SUCCESS(cls):
        return cls._get_colors().SUCCESS_6

    @classmethod
    def WARNING(cls):
        return cls._get_colors().WARNING_6

    @classmethod
    def ERROR(cls):
        return cls._get_colors().ERROR_6

    @classmethod
    def NORMAL(cls):
        return cls._get_colors().GRAY_9

    @classmethod
    def DISABLED(cls):
        return cls._get_colors().GRAY_6

    @classmethod
    def INFO(cls):
        return cls._get_colors().PRIMARY_6

    @classmethod
    def PRIMARY(cls):
        return cls._get_colors().PRIMARY_6

    @classmethod
    def SUCCESS_BTN(cls):
        return cls._get_colors().SUCCESS_6

    @classmethod
    def DANGER(cls):
        return cls._get_colors().ERROR_6

    @classmethod
    def WARNING_BTN(cls):
        return cls._get_colors().WARNING_6

    @classmethod
    def SECONDARY(cls):
        return cls._get_colors().GRAY_6

    @classmethod
    def MEMORY_LOW(cls):
        return cls._get_colors().SUCCESS_6

    @classmethod
    def MEMORY_MEDIUM(cls):
        return cls._get_colors().WARNING_6

    @classmethod
    def MEMORY_HIGH(cls):
        return cls._get_colors().ERROR_6

    @classmethod
    def PROCESS_RUNNING(cls):
        return cls._get_colors().SUCCESS_6

    @classmethod
    def PROCESS_SYSTEM(cls):
        return cls._get_colors().GRAY_7

    @classmethod
    def PROCESS_USER(cls):
        return cls._get_colors().GRAY_9

    @classmethod
    def PROCESS_SYSTEM_USER(cls):
        return cls._get_colors().ERROR_6

    @classmethod
    def TEXT_PRIMARY(cls):
        return cls._get_colors().GRAY_9

    @classmethod
    def TEXT_SECONDARY(cls):
        return cls._get_colors().GRAY_7

    @classmethod
    def TEXT_DISABLED(cls):
        return cls._get_colors().GRAY_6

    @classmethod
    def BG_PRIMARY(cls):
        return cls._get_colors().GRAY_1

    @classmethod
    def BG_SECONDARY(cls):
        return cls._get_colors().GRAY_2

    @classmethod
    def BG_DISABLED(cls):
        return cls._get_colors().GRAY_3

    @classmethod
    def BORDER_PRIMARY(cls):
        return cls._get_colors().GRAY_5

    @classmethod
    def BORDER_SECONDARY(cls):
        return cls._get_colors().GRAY_4

    @classmethod
    def BORDER_LIGHT(cls):
        return cls._get_colors().GRAY_3


class StyleApplier:
    """样式应用器"""

    @staticmethod
    def apply_ant_design_theme(app):
        """应用Ant Design主题到整个应用"""
        stylesheet = theme_manager.get_stylesheet()
        app.setStyleSheet(stylesheet)

        # 连接主题变化信号
        theme_manager.theme_changed.connect(lambda theme: app.setStyleSheet(theme_manager.get_stylesheet(theme)))


class TitleHelper:
    """标题样式助手类

    提供创建一致样式标题QLabel的工具方法
    """

    # 预定义的标题样式
    STYLES = {
        "main": {
            "font_size": "24px",
            "font_weight": "bold",
            "margin_bottom": "16px",
            "color": None,  # 使用主题默认颜色
        },
        "section": {"font_size": "18px", "font_weight": "bold", "margin_bottom": "12px", "color": None},
        "subsection": {"font_size": "16px", "font_weight": "600", "margin_bottom": "8px", "color": None},
        "card": {"font_size": "14px", "font_weight": "600", "margin_bottom": "0px", "color": None},
    }

    @classmethod
    def create_title(cls, text, style_type="section", custom_style=None):
        """创建标题QLabel

        Args:
            text (str): 标题文本
            style_type (str): 样式类型，可选值: "main", "section", "subsection", "card"
            custom_style (dict): 自定义样式属性，会覆盖预定义样式

        Returns:
            QLabel: 配置好样式的标题标签
        """
        from PyQt6.QtWidgets import QLabel

        label = QLabel(text)

        # 获取基础样式
        if style_type in cls.STYLES:
            style = cls.STYLES[style_type].copy()
        else:
            style = cls.STYLES["section"].copy()

        # 应用自定义样式
        if custom_style:
            style.update(custom_style)

        # 构建样式字符串
        style_parts = []

        if style.get("font_size"):
            style_parts.append(f"font-size: {style['font_size']}")

        if style.get("font_weight"):
            style_parts.append(f"font-weight: {style['font_weight']}")

        if style.get("margin_bottom"):
            style_parts.append(f"margin-bottom: {style['margin_bottom']}")

        if style.get("margin_top"):
            style_parts.append(f"margin-top: {style['margin_top']}")

        if style.get("color"):
            style_parts.append(f"color: {style['color']}")

        if style.get("text_align"):
            style_parts.append(f"text-align: {style['text_align']}")

        # 应用样式
        if style_parts:
            label.setStyleSheet("; ".join(style_parts) + ";")

        return label

    @classmethod
    def create_main_title(cls, text, custom_style=None):
        """创建主标题

        Args:
            text (str): 标题文本
            custom_style (dict): 自定义样式属性

        Returns:
            QLabel: 主标题标签
        """
        return cls.create_title(text, "main", custom_style)

    @classmethod
    def create_section_title(cls, text, custom_style=None):
        """创建章节标题

        Args:
            text (str): 标题文本
            custom_style (dict): 自定义样式属性

        Returns:
            QLabel: 章节标题标签
        """
        return cls.create_title(text, "section", custom_style)

    @classmethod
    def create_subsection_title(cls, text, custom_style=None):
        """创建子章节标题

        Args:
            text (str): 标题文本
            custom_style (dict): 自定义样式属性

        Returns:
            QLabel: 子章节标题标签
        """
        return cls.create_title(text, "subsection", custom_style)

    @classmethod
    def create_card_title(cls, text, custom_style=None):
        """创建卡片标题

        Args:
            text (str): 标题文本
            custom_style (dict): 自定义样式属性

        Returns:
            QLabel: 卡片标题标签
        """
        return cls.create_title(text, "card", custom_style)
