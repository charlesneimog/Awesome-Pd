# else

## `allpass.rev~`

Use `allpass.rev~` as a reverberator, allpass filter and delay. By default, you can set a delay time and a reverberation/decay time in ms ("t60"), which is the time the impulse takes to fall 60dB in energy (but you can change this parameter to a gain coefficient).

## `comb.rev~`

Use `ecomb.rev~` as a reverberator, comb filter and delay.

## `echo.rev~` 

`echo.rev~` is an echo/reverb abstraction. It only contains feedforward lines and can be used to produce early reflections in a reverb algorithm. But it can also be used on its own.

You can set the number of echo stages with the first argument and the room size with the second argument/inlet. A typical value is the default. The number of stages are up to 20, but you can see how that generates extreme results.

## `mono.rev~` 

`mono.rev~` is a reverb abstraction with mono input but stereo output. It's based on a feedback delay network like vanilla's `rev3~` object, but it offers a "room size" parameter whose typical value is around 0.5, values closer to 0 and 1 may create unusual results. Changing size values may generates unusual artifacts (you can clear the delay buffers when you do it to prevent it, but you may get clicks).

## `stereo.rev~` 

## `free.rev~` 

## `giga.rev~` 

## `plate.rev~` 

## `fdn.rev~`