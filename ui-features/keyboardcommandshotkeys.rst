键盘命令（快捷键）
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:game:`Ares` 包含了几个可以通过键盘快捷键在游戏中发出的新命令。注意这些快捷键键的标签目前是硬编码的，与标准《尤里的复仇》快捷键（使用字符串表）不同。


.. index:: 键盘命令；保存当前地图快照为 YRM

地图快照
````````````

可以分配一个按键用于保存当前游戏的快照为一个 YRM 地图文件，该文件可以在 FinalAlert 2 YR 中编辑。

.. note:: 在游戏中加载生成的地图文件会引发一个 Internal Error，因为雷达预览图没有被保存。若要解决这个问题则在地图文件中添加
  \ :tag:`[Preview]Size=0,0,1,1`。

.. note:: 该键盘命令可以在你 mod 的发布版本中禁用。参见
  \ :ref:`禁用键盘命令<disable-commands>`。

.. versionadded:: 0.1


.. _`debug-logging`:

调试日志记录
`````````````

可以分配一个按键用于切换 :file:`debug.log` 写入的开启与关闭。参见 :doc:`内部错误／调试</ui-features/internalerrorsdebugging>`。

.. versionadded:: 0.1



.. index:: single: 键盘命令；转储类型信息至日志文件，包括 AI 触发权重

类型数据转储
`````````````````

可以分配一个按键用于输出一些额外信息到 :file:`debug.log` 文件（见上）中。额外信息会在每次按下时写入日志。这包括例如 AI 触发权重等信息，以此 mod 作者们可以理解 AI 在整个游戏过程中是如何表现的。注意 :file:`debug.log` 文件的写入必须被开启否则数据将无法写入文件。

.. note:: 该键盘命令可以在你 mod 的发布版本中禁用。参见
  \ :ref:`禁用键盘命令<disable-commands>`。

.. versionadded:: 0.1


.. index:: 键盘命令；转储 AI 计划建造什么基地建筑

AI 基地计划转储
````````````````````

要输出当前 AI 玩家的基地计划用于调试目的，你可以使用这一键盘命令。每个 AI 玩家的基地计划会转储到 :file:`debug.log` 中。这可以协助诊断 AI 选择建筑物时出现的问题。注意 :file:`debug.log` 文件的写入必须被开启否则数据将无法写入文件。

.. note:: 该键盘命令可以在你 mod 的发布版本中禁用。参见
  \ :ref:`禁用键盘命令<disable-commands>`。

.. versionadded:: 0.1


AI 接管控制
`````````````````

请参阅 :doc:`命令行参数</ui-features/commandlinearguments>` 下的标签：

:-AI-CONTROL：

.. note:: 该键盘命令可以在你 mod 的发布版本中禁用。参见
  \ :ref:`禁用键盘命令<disable-commands>`。

.. versionadded:: 0.1



.. index:: 键盘命令；在屏幕上显示当前及平均帧率

FPS 计数器
```````````

这一键盘命令允许玩家显示当前游戏进程每秒的帧数，以及它们的总体平均值。文本会在屏幕左下角以白色显示。再次按下该按键可隐藏 FPS 计数器。

.. versionadded:: 0.3


切换电源
````````````

现在可以通过键盘命令使用这个在 :game:`Tiberian Sun` 中广为人知的功能。参见 :doc:`切换电源</new/buildings/togglepower>`。

.. versionadded:: 0.8


.. _`disable-commands`:

.. index:: 键盘命令；在公开发布版本禁用调试键盘命令

禁用键盘命令
~~~~~~~~~~~~~~~~~~~~~~~~~~~

对于 mod 的发布版本可以在 :file:`rulesmd.ini` 中禁用某些调试键盘命令。受影响的键盘命令为 AI 控制、类型数据转储、地图快照与转储 AI 基地计划。

:tagdef:`[GlobalControls]DebugKeysEnabled=boolean` 是否启用调试键盘命令。默认 :value:`yes`。如果设为 :value:`no`，执行一个被禁用的键盘命令将会换为显示一条白色的文本消息。

显示给玩家的这条消息字符串可以由 :value:`TXT_COMMAND_DISABLED` 进行定义。你可以在你的语言文件中覆盖该字符串。你还能包含（至多）一个「%s」占位符，它将被替换为被禁用的键盘命令的名称。

.. warning:: 请注意这并不是一个安保功能也不是任何真正的防破解保护。该功能仅仅是为了便捷地防止从游戏中提取某些文件的行为不要过于简便。

.. versionadded:: 0.2
