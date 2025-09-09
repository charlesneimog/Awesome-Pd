<div class="grid cards" markdown>
- :material-tune: [__presets__](../objects/presets.md) `presets` manages presets for patches and abstractions and has interpolation and morphing features.

- :material-tune: [__midi__](../objects/midi.md) `midi` plays/records raw MIDI streams and can save/read MIDI files or import/export to txt files.
.

- :material-tune: [__gran.player~__](../objects/gran.player~.md) `gran.player~` is like `player~` but provides independent time stretching and pitch shifting via granulation (just like `pvoc.player~`).

- :material-tune: [__sfont~__](../objects/sfont~.md) `sfont~` is a sampler synthesizer that plays SoundFont files.

- :material-tune: [__buffer~__](../objects/buffer~.md) `buffer~` stores audio in a memory buffer (an array).

- :material-tune: [__play.file~__](../objects/play.file~.md) `play.file~` reads/plays files from your computer similarly to Vanilla's `readsf~`, but it supports more file formats (officialy AAC, AIF, CAF, FLAC, MP3, OGG, OPUS & WAV).

- :material-tune: [__sample~__](../objects/sample~.md) `sample~` is an abstraction that creates an audio buffer which you can use to load a sample or record into.

- :material-tune: [__format__](../objects/format.md) `format` formats symbols similarly to `makefilename`, but it accepts more than one '%' variable, where each corresponds to an inlet.
.

- :material-tune: [__pic__](../objects/pic.md) `pic` loads image pictures that you can interact with.

- :material-tune: [__dir__](../objects/dir.md) The `dir` object in Pure Data is used to access and manage files from directories.

- :material-tune: [__loadbanger__](../objects/loadbanger.md) `loadbanger` works with both kinds of bangs.

- :material-tune: [__sfinfo__](../objects/sfinfo.md) `sfinfo` supports all files that `sfload` and `play.file~` support and can be used to query file sample information but so far only channels and 'inst' info for aif files (this object is still very experimental).
.

- :material-tune: [__player~__](../objects/player~.md) `player~` is a convenient abstraction based on `sfload` (so it supports the same file formats, check it's help file) and `tabplayer~`.

</div>