<div class="grid cards" markdown>
- :material-tune: [__smooth~__](../objects/smooth~.md) `smooth~` smoothens a signal transition with linear interpolation by default, at a given time in ms.

- :material-tune: [__envgen~__](../objects/envgen~.md) `envgen~` is an envelope (and an all purpose line) generator (here it creates a 1000 ms line to 1 and then a 500 ms line to 0).

- :material-tune: [__slew~__](../objects/slew~.md) `slew~` takes an amplitude limit per second and an incoming value to be 'slew limited'.

- :material-tune: [__float2sig~__](../objects/float2sig~.md) `float2sig~` (or `f2s~` for short) is an abstraction based on `vline~` that converts floats to signals or lists to multichannel signals.

- :material-tune: [__vocoder~__](../objects/vocoder~.md) `vocoder~` is classic cross synthesis channel vocoder abstraction.
.

- :material-tune: [__autofade.mc~__](../objects/autofade.mc~.md) `autofade.mc~` is an automatic fade in/out for multichanne inputs.

- :material-tune: [__autofade2.mc~__](../objects/autofade2.mc~.md) `autofade2.mc~` is an automatic fade in/out for multichanne inputs.

- :material-tune: [__slew2~__](../objects/slew2~.md) `slew2~` is like `slew~` but has independent values for upwards & downwards ramps.

- :material-tune: [__rampsmooth~__](../objects/rampsmooth~.md) `rampsmooth~` smooths a signal across 'n' samples.

- :material-tune: [__autofade2~__](../objects/autofade2~.md) `autofade2~` is an automatic fade in/out for multi inputs.

- :material-tune: [__asr~__](../objects/asr~.md) The `asr~` object in Pure Data is an attack/sustain/release envelope generator, simplified compared to `adsr~`.

- :material-tune: [__smooth2~__](../objects/smooth2~.md) `smooth2~` is just like `smooth~` but has distinct ramp times for both up and down.
.

- :material-tune: [__adsr~__](../objects/adsr~.md) `adsr~` is an attack/decay/sustain/release gated envelope.

- :material-tune: [__function__](../objects/function.md) `function` is a breakpoints function GUI, mainly used with `function~` or `envgen~`.

- :material-tune: [__gaterelease__](../objects/gaterelease.md) `gaterelease` allows you to release one gate in your patch while you still hold another.

- :material-tune: [__envelope~__](../objects/envelope~.md) `envelope~` provides 6 different envelopes, which are generated via a phase input.
.

- :material-tune: [__glide~__](../objects/glide~.md) `glide~` generates a glide/portamento from its signal input changes.

- :material-tune: [__gatehold__](../objects/gatehold.md) `gatehold` holds a gate value for a certain amount of time (specified in ms) after the gate has closed.

- :material-tune: [__lag2~__](../objects/lag2~.md) `lag2~` is like `lag~` but has a different time for ramp up and ramp down.

- :material-tune: [__gatehold~__](../objects/gatehold~.md) `gatehold~` holds a gate value for a certain amount of time (specified in ms) after the gate has closed.

- :material-tune: [__compress~__](../objects/compress~.md) `compress~` is an abstraction that performs compression.

- :material-tune: [__gain2~__](../objects/gain2~.md) `gain2~` is a convenient stereo gain abstraction, so you can adjust a stereo signal's gain.

- :material-tune: [__decay~__](../objects/decay~.md) `decay~` is based on SuperCollider's "Decay" UGEN.

- :material-tune: [__speed__](../objects/speed.md) `speed` is somewhat related to `line`.

- :material-tune: [__pimp~__](../objects/pimp~.md) `pimp~` is very convenient for both driving a process with its phase output (such as reading a sample or envelope) and also triggering at period transitions other objects or processes (such as with `sh~` below).
.

- :material-tune: [__rms~__](../objects/rms~.md) `rms~` is similar to Pd Vanilla's `env~`, but it reports the RMS value in linear amplitude (default) or in dBFS.
.

</div>