图形／曲面的绘制
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning:: 这仅适用于高级用户！

在 :file:`ares.ini` 中你可以添加该节：

::

    [Graphics.Advanced]
    DirectX.Force= (hardware|emulation)

虽然默认为 :value:`hardware`，但 :value:`emulation` 拥有与特殊版本 :file:`ddraw.dll` 相同的效果，后者通过不绘制软件模拟不支持的效果来使游戏速度更快。

.. note:: \ :value:`emulation` 无法用于 Windows Vista 及更高版本的系统。
  \ :game:`Ares` 在这些系统上默认使用 :value:`hardware`。

.. note:: \ :game:`Ares.ini` 并未涉及为由 mod 包含或编辑，因为该文件在未来可能包含终端用户希望由他们自行设置的各种其他项目。

  Launch Base 不允许 mod 包含
  \ :file:`ares.ini`，并提供了一个它自己的界面来允许用户修改上述图形设置。

.. versionadded:: 0.1
