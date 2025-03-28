.. index:: 建筑发射导弹子机

=======================================
建筑发射导弹子机
=======================================

原先建筑可以使用 :tag:`Spawns` 逻辑发射没有设置为 :tag:`Locomotor=Rocket` 的
:type:`AircraftType`，就像驱逐舰和舰载机子机那种，
否则会导致游戏崩溃。:game:`Ares` 修复了对导弹类的处理，
因此 :tag:`Locomotor=Rocket` 不再会导致游戏崩溃。

.. versionadded:: 1.0
