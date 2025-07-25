.. index:: Spawns; MissileSpawn on buildings

=======================================
:captiontag:`MissileSpawn` on Buildings
=======================================

Buildings were able to use :tag:`Spawns` logic only as long as the spawned
:type:`AircraftType`  was not listed in :tag:`V3RocketType` or :tag:`DMislType` or :tag:`CMislType`, thus could only spawn
aircraft like the Destroyer and the Aircraft Carrier. If a building were to
spawn a missile, the game would crash. :game:`Ares` fixed the missile handling
and thus it no longer crashes the game.

.. versionadded:: 1.0
