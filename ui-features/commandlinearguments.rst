.. index:: 命令行参数；不需要《尤里的复仇》游戏光碟
.. index:: 命令行参数；不播放艺电/西木的 Logo 视频

命令行参数
~~~~~~~~~~~~~~~~~~~~~~

:-CD: 允许游戏在没有 :game:`Yuri's Revenge` CD 的情况下运行。首先需要将 :game:`Yuri's Revenge` CD 的内容复制到 :game:`Red Alert 2` 目录中。十周年典藏版（:game:`The First Decade`）用户已经安装了所有必要的文件，因此无需执行额外操作。
:-NOLOGO: 阻止游戏在开始加载前播放 EA Logo 视频。
:-LOG: 初始打开 :file:`debug.log` 文件的写入。参见 :doc:`内部错误／调试</ui-features/internalerrorsdebugging>`。
:-LOG-CSF: 将所有在语言文件中找不到的 CSF 标签输出到 :file:`debug.log` 中。每个标签只记录一次。并以 :value:`[CSFLoader]` 作为前缀。
:-STRICT: 在游戏加载时检测到不一定严重的错误也抛出一个 Internal Error。例如你为一个语句设置了一个无法解析的非空值。

  .. note:: 一些原始规则中就已存在的错误也会触发这个所以你需要在使用它前清理掉它们。
:-AI-CONTROL: 启用 AI Control 功能。在打开 :game:`Yuri's Revenge` 前于命令行中输入此命令可允许玩家分配一个快捷键来允许 AI 代理控制。

  .. warning:: 此功能主要设计用于离线测试和 AI 编写测试目的、由于功能复杂、缺乏兴趣以及人员变动，特此说明：该功能 **不** 受官方支持。
:-AFFINITY\:N: 控制游戏运行在哪些处理器上。:value:`N` 是一个对应每个对于第一个开始为 :value:`1`、对于第二个开始为 :value:`2`、对于第三个为 :value:`4` 并以此类推的处理器的位掩码。如果未设置则使用 :value:`1`，意为游戏将仅在第一个处理器上运行。使用 :value:`0` 以禁用该功能。

  .. warning:: 可以组合多个位，例如 :value:`3` 代表前两个处理器。通常游戏仅应运行在单个处理器上（即 :value:`N` 是 2 的幂），因为游戏并未设计为能够利用多个处理器。

.. versionadded:: 0.1
