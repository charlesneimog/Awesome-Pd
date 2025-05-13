# PureData Objects

## czero~

`czero~` filters a complex audio signal (first two inlets) via a raw one-zero (non-recursive) filter, whose coefficients are controlled by creation arguments or by another complex audio signal (remaining two inlets).

## rpole~

`rpole~` filters an audio signal (left inlet) via a raw one-pole (recursive) real filter, whose coefficient is controlled by a creation argument or by an audio signal (right inlet).

## cpole~

`cpole~` filters a complex audio signal (first two inlets) via a raw one-pole (recursive) filter, whose coefficients are controlled by creation arguments or by another complex audio signal (remaining two inlets).

## rzero~

`rzero~` filters an audio signal (left inlet) via a raw one-zero (non-recursive) real filter, whose coefficient is controlled by a creation argument or by an audio signal (right inlet).
