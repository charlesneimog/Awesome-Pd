# Procedures

<div class="grid cards" markdown>

- :material-tune: [__l.readsvg__](../../objects/l.readsvg.md) `l.readsvg` is a `pdlua` object designed to read SVG files created or edited in Inkscape.
- :material-tune: [__chance~__](../../objects/chance~.md) The `chance~` object probabilistically routes an incoming bang to one of its outlets based on a set of weighted chances.
- :material-tune: [__segregate__](../../objects/segregate.md) The `segregate` object sorts incoming messages by their data type, sending them to dedicated outlets.
- :material-tune: [__drunkard__](../../objects/drunkard.md) The `drunkard` object generates a sequence of pseudo-random numbers based on a drunkard's walk algorithm.
- :material-tune: [__loop__](../../objects/loop.md) The `loop` object in Pure Data provides a flexible iteration mechanism, functioning as a counter that can increment or decrement through a specified range.
- :material-tune: [__rec__](../../objects/rec.md) The `rec` object records incoming messages across multiple tracks and plays them back.
- :material-tune: [__drip__](../../objects/drip.md) The `drip` object unfolds a package (list) into a sequence of individual elements, outputting them one by one with a configurable delay in milliseconds.
- :material-tune: [__l.attrfilter__](../../objects/l.attrfilter.md) The `l.attrfilter` object in Pure Data (using `pdlua`) filters elements from an SVG file loaded with [`l.readsvg`](l.readsvg.md) based on attributes such as stroke, fill, or ID.
- :material-tune: [__mono~__](../../objects/mono~.md) The `mono~` object acts as a monophonic signal voice manager, emulating monophonic synthesizer behavior.
- :material-tune: [__niagara__](../../objects/niagara.md) The `niagara` object divides an incoming message or list into two sub-packages.
- :material-tune: [__speedlim__](../../objects/speedlim.md) The `speedlim` object controls the rate at which messages are passed through.
- :material-tune: [__count__](../../objects/count.md) The `count` object in Pure Data generates a sequence of numbers, incrementing or decrementing between a defined minimum and maximum value.
- :material-tune: [__nmess__](../../objects/nmess.md) The `nmess` object acts as a message gate, allowing a specified number of messages (`n`) to pass through its left outlet.
- :material-tune: [__euclid__](../../objects/euclid.md) The `euclid` object implements the Euclidean rhythm algorithm, which distributes a given number of "hits" as evenly as possible over a specified number of "steps".
- :material-tune: [__abs.pd~__](../../objects/abs.pd~.md) The `abs.pd~` object loads a Pure Data patch as a subprocess, making it easier to manage complex patches.
- :material-tune: [__counter__](../../objects/counter.md) The `counter` object in Pure Data increments or decrements an integer value within a specified range.
- :material-tune: [__timed.gate~__](../../objects/timed.gate~.md) The `timed.gate~` object generates a timed gate signal or control output.
- :material-tune: [__loadbanger__](../../objects/loadbanger.md) The `loadbanger` (or `lb`) object in Pure Data sends "bang" messages when a patch is loaded, when it receives any message, or when clicked.
- :material-tune: [__repeat__](../../objects/repeat.md) The `repeat` object in Pure Data outputs any incoming message a specified number of times.
- :material-tune: [__tempo__](../../objects/tempo.md) The `tempo` object functions as a versatile metronome, sending bangs at a specified rate in BPM, milliseconds, or Hertz.
- :material-tune: [__speed__](../../objects/speed.md) The `speed` object facilitates gradual changes in tempo, enabling accelerando or ritardando effects.
- :material-tune: [__loadmess__](../../objects/loadmess.md) The `loadmess` object sends a predefined message automatically when its containing patch is loaded, or when it receives a `bang` message.
- :material-tune: [__limit__](../../objects/limit.md) The `limit` object controls the rate of messages, ensuring a minimum time interval between outputs.
- :material-tune: [__mono__](../../objects/mono.md) The `else/mono` object manages incoming MIDI note messages to enforce monophonic behavior, allowing only one note to sound at a time based on configurable priority modes (last, high, or low note).
- :material-tune: [__chrono__](../../objects/chrono.md) The `chrono` object functions as a versatile stopwatch or timer.
- :material-tune: [__voices__](../../objects/voices.md) The `voices` object manages voice allocation for polyphonic synthesizers, offering advanced features beyond `poly`.
- :material-tune: [__uzi__](../../objects/uzi.md) The `uzi` object generates a sequence of bangs and corresponding counter values, useful for iterating through a specified number of steps.
- :material-tune: [__clock__](../../objects/clock.md) The `clock` object generates bangs at a regular tempo, functioning as either a "main" or "synced" clock.
- :material-tune: [__sequencer~__](../../objects/sequencer~.md) The `sequencer~` object outputs values from a predefined sequence when triggered by a signal (0 to non-0 transition) or a bang.

</div>