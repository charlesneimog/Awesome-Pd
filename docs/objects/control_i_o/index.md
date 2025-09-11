# Control I/O

<div class="grid cards" markdown>

- :material-tune: [__keyboard__](keyboard.md) The `keyboard` object provides a graphical piano keyboard interface for Pure Data.
- :material-tune: [__gemmouse__](gemmouse.md) The `gemmouse` object captures and outputs mouse events occurring within a GEM (Graphics Environment for Multimedia) window.
- :material-tune: [__touch.in__](touch.in.md) The `touch.in` object extracts MIDI Aftertouch (channel pressure) information from either a connected MIDI device or an external raw MIDI data stream.
- :material-tune: [__midi.in__](midi.in.md) The `midi.in` object processes incoming MIDI data, converting raw MIDI streams into "cooked" data with type symbols, values, and channel information.
- :material-tune: [__bend.in__](bend.in.md) The `bend.in` object extracts MIDI Pitch Bend messages from connected MIDI devices or raw MIDI data streams.
- :material-tune: [__gemtablet__](gemtablet.md) The `gemtablet` object in Pure Data interfaces with and responds to events from a graphics tablet.
- :material-tune: [__keypress__](keypress.md) The `keypress` object detects presses of a single computer keyboard key, outputting a bang or a toggle (1 for pressed, 0 for released).
- :material-tune: [__pix_video__](pix_video.md) The `pix_video` object captures live video input from various cameras (USB, FireWire, capture cards) supported by the operating system.
- :material-tune: [__mousestate__](mousestate.md) The `mousestate` object reports the current state of the mouse, including click status, cursor X and Y positions, and delta movement.
- :material-tune: [__pad__](pad.md) The `pad` object is a graphical user interface (GUI) element that reports mouse coordinates and click status within its area.
- :material-tune: [__canvas.mouse__](canvas.mouse.md) The `canvas.mouse` object captures mouse click status and coordinates within a Pure Data canvas.
- :material-tune: [__gemorb__](gemorb.md) The `gemorb` object connects to a SpaceOrb 3D controller via a specified serial port (comport).
- :material-tune: [__numbox~__](numbox~.md) The `numbox~` object is a graphical user interface element in Pure Data designed to display and generate audio signal values.
- :material-tune: [__mouse__](mouse.md) The `mouse` object captures global mouse interaction within Pure Data.
- :material-tune: [__gemw32window__](gemw32window.md) The `gemw32window` object is a GEM (Graphics Environment for Multimedia) object specific to Microsoft Windows, used for creating and managing a graphical output window.
- :material-tune: [__mousefilter__](mousefilter.md) The `mousefilter` object acts as a gate, preventing messages from passing through while a mouse button is held down.
- :material-tune: [__ctl.in__](ctl.in.md) The `ctl.in` object extracts MIDI Control Change (CC) messages from either a connected MIDI device or an external raw MIDI data stream.
- :material-tune: [__gemkeyboard__](gemkeyboard.md) The `gemkeyboard` object captures keyboard events occurring within a GEM window.
- :material-tune: [__gemsdl2window__](gemsdl2window.md) The `gemsdl2window` object creates and manages a graphical window using the SDL2 toolkit, providing an OpenGL context for rendering.
- :material-tune: [__suspedal__](suspedal.md) The `suspedal` object emulates a MIDI sustain pedal, holding `Note Off` messages when active and releasing them when deactivated.
- :material-tune: [__knob__](knob.md) The `knob` object is a graphical user interface (GUI) element in Pure Data that functions as a rotary control.
- :material-tune: [__mpe.in__](mpe.in.md) The `mpe.in` object processes MIDI Polyphonic Expression (MPE) data, converting raw MIDI input from either an internal device or an external source into structured MPE messages.
- :material-tune: [__midi.learn__](midi.learn.md) The `midi.learn` object is a Pure Data abstraction designed to learn and store incoming MIDI data, such as control changes, program changes, notes, and bends.
- :material-tune: [__ptouch.in__](ptouch.in.md) `ptouch.in` extracts MIDI polyphonic aftertouch messages from raw MIDI input, such as from a connected MIDI device or an external MIDI data stream.
- :material-tune: [__click__](click.md) The `click` object sends a `bang` message when its parent patch (abstraction or subpatch) is clicked.
- :material-tune: [__keymap__](keymap.md) The `keymap` object translates computer keyboard presses into MIDI note on/off messages, effectively turning your QWERTY keyboard into a musical input device.
- :material-tune: [__gemkeyname__](gemkeyname.md) The `gemkeyname` object captures keyboard events occurring within the GEM window.
- :material-tune: [__keycode__](keycode.md) The `keycode` object provides layout-independent keyboard input, outputting a numerical key code based on the physical key location.
- :material-tune: [__lpt__](lpt.md) The `lpt` object in Pure Data allows writing and reading data to and from a computer's parallel port.

</div>