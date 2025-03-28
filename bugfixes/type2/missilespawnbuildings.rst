.. index:: Spawns; MissileSpawn on buildings

=======================================
:captiontag:`MissileSpawn` on Buildings
=======================================

Buildings were able to use :tag:`Spawns` logic only as long as the spawned
:type:`AircraftType` had :tag:`Locomotor≠{B7B49766-E576-11d3-9BD9-00104B972FE8}` set, thus could only spawn
aircraft like the Destroyer and the Aircraft Carrier. If a building were to
spawn a missile, the game would crash. :game:`Ares` fixed the missile handling
and thus :tag:`Locomotor={B7B49766-E576-11d3-9BD9-00104B972FE8}` no longer crashes the game.

.. versionadded:: 1.0
