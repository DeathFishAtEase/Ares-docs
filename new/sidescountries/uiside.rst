User Interface and Loading Theme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index::
  Sides; Sidebar
  Interface; Sidebar for sides

Sidebar
-------

:tagdef:`[Side]Sidebar.MixFileIndex=integer`
  The MIX file number to use for the sidebar (e.g. :value:`1` for the Allied
  sidec01.mix, :value:`2` for the Soviet sidec02.mix).
:tagdef:`[Side]Sidebar.YuriFileNames=boolean`
  Whether or not to use the Yuri sidebar file names (file naming rule similar to the original Yuri's :file:`sidec02md.mix`).

.. note:: This feature primarily serves independent palettes. You could also place :file:`radary.shp` directly into :file:`sidec0#.mix` without creating an additional :file:`sidec0#md.mix`.

File Name Comparison Table
`````````````````````````````
  .. table::

    ================================  ==================================================================  ================================================
    File Purpose                      Original Naming Rule                                                Yuri-style Naming Rule
    ================================  ==================================================================  ================================================
    :value:`Radar Animation`          :file:`radar.shp`                                                   :file:`radar`:value:`y`:file:`.shp`
    :value:`Radar Palette`            :file:`sidebar.pal` (Many other files also share this palette)      :value:`radaryuri.pal`
    :value:`Background - Large`       :file:`bkgdlg.shp`                                                  :file:`bkgdlg`:value:`y`:file:`.shp`
    :value:`Background - Medium`      :file:`bkgdmd.shp`                                                  :file:`bkgdmd`:value:`y`:file:`.shp`
    :value:`Background - Small`       :file:`bkgdsm.shp`                                                  :file:`bkgdsm`:value:`y`:file:`.shp`
    :value:`Background Palette`       :file:`uibkgd.pal`                                                  :file:`uibkgd`:value:`y`:file:`.pal`
    ================================  ==================================================================  ================================================

.. versionadded:: 0.1


.. index::
  Sides; Tooltip and message text colors
  Interface; Tooltip and message text colors for sides

Text Colors
-----------

:tagdef:`[Side]ToolTipColor=R,G,B`
  Interface text and border color for tool tips, the credits counter, and other
  UI elements. Defaults to :value:`255,255,0` for sides :value:`Nod` and
  :value:`ThirdSide`, otherwise to :value:`164,210,255`.
:tagdef:`[Side]MessageTextColor=Color scheme`
  The color scheme used for printing ingame messages triggered by map action 11.
  Defaults to the 6th color scheme for side :value:`Nod`, the 13th color scheme
  for side :value:`ThirdSide`, to 11th color scheme otherwise. In the unmodified
  game, the colors are :value:`DarkRed`, :value:`DarkSky` and :value:`DarkBlue`
  respectively.

.. versionadded:: 0.4



.. index::
  Sides; Dialog menu backgrounds
  Interface; Dialog menu backgrounds for sides

Dialogs
-------

The side specific dialog background is used when a Reconnection error occurs or
while loading or saving a game.

:tagdef:`[Side]DialogBackground.Image=filename, *including* the .shp extension`
The shp file used as background for dialog boxes for this side. Should be
452x326; the image is aligned on the top left corner of the dialog. Defaults to
:value:`PUDLGBGA.SHP`, :value:`PUDLGBGS.SHP`, and :value:`PUDLGBGY.SHP` for
sides 1, 2 and all others respectively. Requires :tag:`DialogBackground.Palette`
to be set.

:tagdef:`[Side]DialogBackground.Palette=filename, *including* the .pal extension`
The palette used to draw the background of dialog boxes for this side. Defaults
to :value:`DIALOG.PAL` for sides 1 and 2, to :value:`DIALOG.PAL` otherwise.
Requires :tag:`DialogBackground.Image` to be set.

.. versionadded:: 0.7


.. index::
  Sides; Loading theme
  Themes; Loading theme for sides

Loading Theme
-------------

:tagdef:`[Side]LoadingTheme=theme id`
  The theme playing for a player of this side while the multiplayer match is
  loading. Defaults to :value:`LOADING`.

.. versionadded:: 0.7


.. _sides-evatag:

.. index::
  Sides; EVA announcer
  EVA; Set announcer for side

EVA
---

:tagdef:`[Side]EVA.Tag=EVA Type`
  Name of the EVA Type tag to load from :file:`evamd.ini` for this side's EVA
  announcer. Use :value:`none` to disable EVA. Defaults to :value:`Russian` for
  side :value:`Nod`, to :value:`Yuri` for side :value:`ThirdSide`, to
  :value:`Allied` otherwise.

  See :doc:`EVA Types </new/evatypes>` on how to define values that can be used
  here.

.. versionadded:: 0.4
