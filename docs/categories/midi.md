<div class="grid cards" markdown>
- :material-tune: [__keyboard__](../objects/keyboard.md) `keyboard` takes MIDI notes and also generates them via clicking.
.

- :material-tune: [__midi__](../objects/midi.md) `midi` plays/records raw MIDI streams and can save/read MIDI files or import/export to txt files.
.

- :material-tune: [__retune__](../objects/retune.md) `retune` receives a scale as a list of steps in cents and a base MIDI pitch value (default 60).

- :material-tune: [__pluck~__](../objects/pluck~.md) `pluck~` is a Karplus-Strong algorithm with a 1st order lowpass filter in the feedback loop.

- :material-tune: [__bl.tri~__](../objects/bl.tri~.md) `bl.tri~` is a triangle oscillator like `else/tri~`, but it is bandlimited.

- :material-tune: [__touch.in__](../objects/touch.in.md) `touch.in` extracts MIDI Aftertouch information from raw MIDI input or a connected MIDI device.
.

- :material-tune: [__scales__](../objects/scales.md) `scales` generates scales as note names (default) or MIDI pitches.

- :material-tune: [__midi.in__](../objects/midi.in.md) `midi.in` sends "cooked" MIDI data instead of "raw" data like `midiin` with MIDI data type symbol, values and channel (but a note output is sent as a simple numeric list).

- :material-tune: [__midi.out__](../objects/midi.out.md) `midi.out` sends MIDI data from "cooked" data, instead of "raw" data like `midiout`.

- :material-tune: [__bend.in__](../objects/bend.in.md) The `bend.in` object in Pure Data extracts MIDI Pitch Bend information from either a connected MIDI device (internal source) or raw MIDI input (external source).

- :material-tune: [__note.out__](../objects/note.out.md) `note.out` formats and sends raw MIDI pitch messages to Pd's MIDI output and its outlet.

- :material-tune: [__damp.osc~__](../objects/damp.osc~.md) `damp.osc~` is an abstraction based `reonant2~` and also very very similar to it (to the point I think it wasn't worth having two objects with such subtle differences).

- :material-tune: [__drum.seq__](../objects/drum.seq.md) `drum.seq` provides a drum grid so you can activate cells to represent attacks.
.

- :material-tune: [__score__](../objects/score.md) `score` has a 'tempo' syntax where 'tempo 60' internally sets the bpm to 60! The 'tempo' messages are output in the mid 'data' outlet.
.

- :material-tune: [__ctl.out__](../objects/ctl.out.md) `ctl.out` formats and sends raw MIDI control messages to Pd's MIDI output and its outlet.

- :material-tune: [__bl.saw2~__](../objects/bl.saw2~.md) `bl.saw2~` is a sawtooth oscillator like `else/saw2~`, but it is bandlimited.

- :material-tune: [__ptouch.out__](../objects/ptouch.out.md) `ptouch.out` formats and sends raw MIDI polyphonic aftertouch messages to Pd's MIDI output and its outlet..

- :material-tune: [__ctl.in__](../objects/ctl.in.md) `ctl.in` extracts MIDI CC information from raw MIDI input or a connected MIDI device.
.

- :material-tune: [__bl.vsaw~__](../objects/bl.vsaw~.md) `bl.vsaw~` is a variable sawtooth waveform oscillator that also becomes a triangular osccilator just like `else/vsaw~`, but it is bandlimited.

- :material-tune: [__midi2note__](../objects/midi2note.md) `midi2note` converts a MIDI pitch value to note names (such as Eb3).

- :material-tune: [__note.in__](../objects/note.in.md) `note.in` extracts MIDI Pitch information from external "raw" MIDI data or an internally connected device.

- :material-tune: [__bl.square~__](../objects/bl.square~.md) `bl.square~` is a square oscillator like `else/square~`, but it is bandlimited.

- :material-tune: [__suspedal__](../objects/suspedal.md) `suspedal` holds MIDI Note Off messages when on and sends them out when it's switched off.

- :material-tune: [__knob__](../objects/knob.md) `knob` has an exponential and log feature just like the `rescale` object.

- :material-tune: [__histogram__](../objects/histogram.md) `histogram` records into a table how many times it received a positive integer number (treated as indexes, floats are truncated).

- :material-tune: [__mpe.in__](../objects/mpe.in.md) `mpe.in` sends "cooked" MPE data from external "raw" MIDI data or an internally connected device.

- :material-tune: [__sequencer__](../objects/sequencer.md) `sequencer` sends an element from a given sequence when banged.

- :material-tune: [__mono__](../objects/mono.md) `mono` takes note messages and handles them to emulate monophonic synth behaviour.

- :material-tune: [__voices__](../objects/voices.md) `voices` outputs a list with voice index, pitch, velocity and optional extra stuff.

- :material-tune: [__touch.out__](../objects/touch.out.md) `touch.out` formats and sends raw MIDI aftertouch messages to Pd's MIDI output and its outlet.

- :material-tune: [__midi.learn__](../objects/midi.learn.md) `midi.learn` is an abstraction based on `savestate` that learns and saves any MIDI input data.

- :material-tune: [__ptouch.in__](../objects/ptouch.in.md) `ptouch.in` extracts MIDI polyphonic aftertouch information from raw MIDI input (such as from `midiin`).
.

- :material-tune: [__keymap__](../objects/keymap.md) `keymap` maps your computer keyboard to MIDI pitches and generates note on/off messages when keys get pressed and released.

- :material-tune: [__note2midi__](../objects/note2midi.md) `note2midi` converts note names (such as 'C4') to MIDI pitch values.

- :material-tune: [__bend.out__](../objects/bend.out.md) `bend.out` formats and sends raw MIDI pitch bend messages to Pd's MIDI output and its outlet.

- :material-tune: [__autotune__](../objects/autotune.md) `autotune` receives a scale as a list of steps in cents and a base MIDI pitch value (default 60).

</div>