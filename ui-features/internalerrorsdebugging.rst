.. index::
  调试；改进了 Internal Error 处理
  调试；用于协助调试 mod 与 Ares 的日志

内部错误／调试
~~~~~~~~~~~~~~~~~~~~~~~~~~~

当发生一个 Internal Error 时所生成的 :file:`except.txt` 文件现已被修改以便输出更多与 mod 作者相关以及对我们这些开发者在调试 :game:`Ares` 引入的更改与新增内容时有用的信息。

:file:`except.txt` 可能会在文件名中包含时间戳以防止现有的 :file:`except.txt` 文件被覆盖。

:game:`Ares` 将会为你提供一个生成崩溃转储文件的选项以辅助确定错误原因。该文件将存储在游戏根目录的 Debug 文件夹中。注意崩溃转储文件体积非常庞大并且或许仅可由 :game:`Ares` 开发者解读。与 :file:`except.txt` 类似，该文件的文件名中将会包含时间戳。

如果你已经启用了调试日志记录（见 :doc:`命令行参数</ui-features/commandlinearguments>` 与 :ref:`调试日志记录 <debug-logging>`）那么游戏将会在上述 Debug 文件夹中生成一个 :file:`debug.log` 文件。与 :file:`except.txt` 类似，该文件的文件名中将会包含时间戳。日志文件可能包含有助于诊断你的 mod 或 :game:`Ares` 自身问题的有用信息。

当发生一个 Internal Error 时，:game:`Ares` 有时可以告诉你错误的原因。例如：

.. image:: /images/crash0.png
  :alt: 一个显示了原因的 Ares Internal Error 对话框的截图，显示 Internal Error 的原因
  :align: center

这里，:game:`Ares` 可以确定错误的原因。

.. image:: /images/crash1.png
  :alt: Ares Internal Error 对话框的截图，显示未解决的 Internal Error
  :align: center

这里，无法确定错误的原因——:game:`Ares` 提议创建一个完整的崩溃报告。

.. image:: /images/crash2.png
  :alt: Ares Internal Error 对话框的截图，在记录 Internal Error 后
  :align: center

崩溃报告已经生成。:game:`Ares` 将在显示这条消息后关闭。

现在一些潜在的错误可以在加载时即被触发而非等到游戏内再突然出现。严重的错误总是会出现，不那么严重的错误只有在你使用了 :doc:`-STRICT 命令行参数</ui-features/commandlinearguments>` 时才会出现。

.. versionadded:: 0.1
