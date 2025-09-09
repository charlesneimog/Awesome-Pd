# Logic

<div class="grid cards" markdown>

- :material-tune: [__greaterthaneq~__](../../objects/greaterthaneq~.md) The `greaterthaneq~` (or `>=~`) object performs a signal-rate comparison, outputting a 1 signal when the left inlet's signal is greater than or equal to the right inlet's signal or argument.
- :material-tune: [__schmitt~__](../../objects/schmitt~.md) The `schmitt~` object implements a Schmitt trigger, converting an input signal into a binary output (1 or 0) based on two distinct threshold levels.
- :material-tune: [__op__](../../objects/op.md) The `op` object in Pure Data performs a wide range of arithmetic, comparative, logical, and bitwise operations.
- :material-tune: [__equal__](../../objects/equal.md) The `equal` object compares two lists.
- :material-tune: [__bitxor~__](../../objects/bitxor~.md) The `bitxor~` object performs a bitwise exclusive OR (XOR) operation on two input signals, or a signal and a given bitmask.
- :material-tune: [__changed__](../../objects/changed.md) The `changed` object outputs its input only when the incoming message differs from the previously received message, effectively filtering out redundant data.
- :material-tune: [__equals~__](../../objects/equals~.md) The `equals~` (or `==~`) object performs a signal-level comparison.
- :material-tune: [__peak__](../../objects/peak.md) The `peak` object compares incoming numbers to a stored "peak" (maximum) value.
- :material-tune: [__match~__](../../objects/match~.md) The `match~` object compares an incoming signal to a list of numerical arguments.
- :material-tune: [__mono~__](../../objects/mono~.md) The `mono~` object acts as a monophonic signal voice manager, emulating monophonic synthesizer behavior.
- :material-tune: [__schmitt__](../../objects/schmitt.md) The `schmitt` object implements a Schmitt trigger, a comparator with hysteresis.
- :material-tune: [__regex__](../../objects/regex.md) The `regex` object checks if an input symbol matches a given regular expression.
- :material-tune: [__notequals~__](../../objects/notequals~.md) The `notequals~` (or `!=~`) object performs a signal-level "not equal to" comparison.
- :material-tune: [__above__](../../objects/above.md) The `above` object detects when an incoming float value crosses a specified threshold.
- :material-tune: [__bitnot~__](../../objects/bitnot~.md) The `bitnot~` object performs a bitwise NOT operation (one's complement) on an incoming audio signal, inverting all bits of its 32-bit representation.
- :material-tune: [__togedge__](../../objects/togedge.md) The `togedge` object detects transitions in numerical input.
- :material-tune: [__0x3e0x7e__](../../objects/0x3e0x7e.md) The `>~` object compares two incoming audio signals, outputting a signal that is true (non-zero) when the first inlet's signal is greater than the second.
- :material-tune: [__nmess__](../../objects/nmess.md) The `nmess` object acts as a message gate, allowing a specified number of messages (`n`) to pass through its left outlet.
- :material-tune: [__thresh~__](../../objects/thresh~.md) `thresh~` is a Schmitt trigger for audio signals.
- :material-tune: [__strcmp__](../../objects/strcmp.md) The `strcmp` object compares two lists as if they were strings, similar to the `strcmp` function in C programming.
- :material-tune: [__matchbox__](../../objects/matchbox.md) The `matchbox` object stores a collection of lists and retrieves them based on various matching algorithms.
- :material-tune: [__routeall__](../../objects/routeall.md) The `routeall` object routes incoming messages to different outlets based on matching arguments, similar to `route` but with enhanced capabilities.
- :material-tune: [__bitand~__](../../objects/bitand~.md) The `cyclone/bitand~` object performs a bitwise AND operation on two incoming signals or a signal and a given bitmask.
- :material-tune: [__&&~__](../../objects/&&~.md) The `&&~` object performs a logical AND operation on two input signals.
- :material-tune: [__bitor~__](../../objects/bitor~.md) The `bitor~` object performs a bitwise OR operation on two audio signals or a signal and a 32-bit integer bitmask.
- :material-tune: [__split__](../../objects/split.md) The `split` object separates incoming float numbers into two outlets based on whether they fall within a specified minimum and maximum range.
- :material-tune: [__zigbinops__](../../objects/zigbinops.md) The `zigbinops` help patch describes a collection of signal-rate Pure Data objects from the zexy library.
- :material-tune: [__cyclone__](../../objects/cyclone.md) The `cyclone` library for Pure Data provides a comprehensive set of mathematical and comparative operators, many of which are direct aliases for common Max/MSP objects.
- :material-tune: [__0x7c0x7c0x7e__](../../objects/0x7c0x7c0x7e.md) The Pure Data object `||~` performs a logical OR operation on two incoming audio signals.
- :material-tune: [__gaterelease~__](../../objects/gaterelease~.md) The `gaterelease~` object releases an audio-rate gate signal after a specified time in milliseconds, allowing for timed gate control even when other gates are held.
- :material-tune: [__tSphere3D__](../../objects/tSphere3D.md) The `tSphere3D` object performs a spherical test to determine if a "mass" (likely a point or object) is located within a defined 3D spherical region.
- :material-tune: [__tCube3D__](../../objects/tCube3D.md) The `tCube3D` object determines if a given 3D point (referred to as a "mass") is located within a user-defined 3D bounding box.
- :material-tune: [__status~__](../../objects/status~.md) The `status~` object is a signal-rate version of `status` that detects transitions in its input signal.
- :material-tune: [__edge~__](../../objects/edge~.md) The `edge~` object detects transitions in an audio signal.
- :material-tune: [__match__](../../objects/match.md) The `match` object outputs incoming data when it matches a predefined pattern.
- :material-tune: [__mono__](../../objects/mono.md) The `else/mono` object manages incoming MIDI note messages to enforce monophonic behavior, allowing only one note to sound at a time based on configurable priority modes (last, high, or low note).
- :material-tune: [__==~__](../../objects/==~.md) The `==~` object compares two incoming audio signals for equality, outputting a signal that indicates whether they are identical.
- :material-tune: [__onebang__](../../objects/onebang.md) The `onebang` object acts as a conditional gate for bang messages.
- :material-tune: [__0x3c0x7e__](../../objects/0x3c0x7e.md) This Pure Data object, `0x3c0x7e`, is an abstraction for the signal comparison object `<~`.
- :material-tune: [__lessthaneq~__](../../objects/lessthaneq~.md) The `lessthaneq~` (or `<=~`) object performs a signal-rate comparison.
- :material-tune: [__greaterthan~__](../../objects/greaterthan~.md) The `greaterthan~` (or `>~`) object in Pure Data performs a signal comparison.
- :material-tune: [__op~__](../../objects/op~.md) The `op~` object performs various signal-rate operations, including comparative (e.g., `==`, `>`), logical (`&&`, `||`, `!`), bitwise (`&`, `|`, `~`, `^`, `<<`, `>>`), and modulus (`%`) calculations.
- :material-tune: [__lessthan~__](../../objects/lessthan~.md) The `lessthan~` (or `<~`) object performs a "less than" comparison on incoming audio signals.
- :material-tune: [__bitshift~__](../../objects/bitshift~.md) `bitshift~` performs bitwise shifting on an incoming signal, moving its bit values to the left or right.

</div>