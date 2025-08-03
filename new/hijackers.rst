.. index::
  Vehicle Thief; Enter and exit sounds
  Vehicle Thief; Works with mind control
  Vehicle Thief; Make units immune
  Vehicles; Make units immune to hijacking
  Mind Control; Works with hijackers
  single: Infantry; Expanded VehicleThief hijacker logic

Hijackers
~~~~~~~~~

偷车贼可以偷走敌方单位，在战场上有效地劫持它们。如果你通过在一个 :type:`InfantryType` 上设置 :tag:`VehicleThief=yes` 来启用了偷车贼逻辑，你可以通过多种方式对其自定义：

:tagdef:`[InfantryType]VehicleThief.EnterSound=Sound name`
  指定偷车贼劫持敌方载具时播放的声音。这也会在拥有 :tag:`CanDrive=yes` 的步兵重启瘫痪单位时使用。默认 :value:`none`。
:tagdef:`[InfantryType]VehicleThief.LeaveSound=Sound name`
  指定偷车贼在载具被摧毁并从中从中逃离时播放的声音。默认 :value:`none`。
:tagdef:`[InfantryType]VehicleThief.BreakMindControl=boolean`
  偷车贼是否可以劫持处于心灵控制中的单位。当偷车贼进入时心控双方之间的链接将被切断。否则偷车贼无法偷走单位。默认 :value:`yes`。
:tagdef:`[InfantryType]VehicleThief.OneTime=boolean`
  偷车贼是否会在劫持单位的过程中被消耗掉。否则当劫持的单位被摧毁时偷车贼会出现。在任何情况下档单位被回收时偷车贼都会被返还。默认 :tag:`no`。
:tagdef:`[InfantryType]VehicleThief.KillPilots=integer`
  偷车贼进入一个单位时杀死的乘员数量。这些乘员在单位被摧毁时将十死无生。使用 :value:`-1` 以杀死所有成员。在 :game:`Tiberian Sun` 中，偷车贼会阻止任何乘员从被摧毁的在剧中逃生。默认 :value:`0`。

在 :game:`Tiberian Sun` 中偷车贼无法劫持设置了 :tag:`NonVehicle=yes` 的单位。 :game:`Ares` 不使用 :tag:`NonVehicle`，因为它会影响许多其他功能，这可能是不得人心的。因此，你必须使用新的专用语句 :tag:`VehicleThief.Allowed` 来更改单位是否可以被劫持。

:tagdef:`[TechnoType]VehicleThief.Allowed=boolean`
  这个 :type:`VehicleType` 或 :type:`AircraftType` 是否可以被偷车贼劫持。默认 :value:`yes`。

.. note::
  \ 默认情况下偷车贼无法驾驶瘫痪了的载具，但你可以通过将 :tag:`VehicleThief=yes` 与 :tag:`CanDrive=yes` 组合使用来实现。

劫持后，归属于人类玩家的单位将会进入 Guard 任务，由 AI 控制的单位将会进入 Hunt 任务。

偷车贼会记录它们的血量与先前的等级。当他们偷取的载具被摧毁时，他们会以旧有的等级以及最大为旧有血量折半的随机血量重生。

现在偷车贼与心灵控制配合得不错。如果一个处于心灵控制中的单位被劫持，它与控制者的链接将被切断并且不会留下虚假的链接线。同样的，被心灵控制的偷车贼会劫持载具给原本所有者的所属方而不是心控它的所属方。如果不能免疫心灵控制那么心灵控制链接会移交给被心灵控制的载具上。否则心灵控制将失去对偷车贼与被偷的车的控制。相仿的情况也是：如果一个偷车贼和一个被心灵控制的载具被摧毁，并且它不免疫心灵控制，那心灵控制链接会移交给重生后的偷车贼。

偷车贼不能劫持友方单位或被击杀乘客弹头瘫痪的载具。参见 :doc:`KillDriver and CanDrive </new/killingdrivers>`。

参见 :doc:`Mouse Cursors </new/mousecursors>` 以了解如何通过 :value:`TakeVehicle` 定义指示目标载具可被劫持的光标。

.. versionadded:: 0.2
