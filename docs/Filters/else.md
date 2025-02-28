# else

## Allpass Filters

### allpass.2nd~ 
`allpass.2nd~` is a 2nd order allpass filter.

### allpass.filt~ 
`allpass.filt~` is an allpass filter that you can set its order with the first argument (needs to be a multiple of 2). This abstraction stacks `allpass.2nd~` objects in cascade.

---

## Lowpass Filters

### lop.bw~ 
Lowpass Butterworth filter abstraction. Specify cutoff frequency and order (2nd to 100th).

### brickwall~ 
10th-order Butterworth lowpass with steep cutoff (60 dB/octave).

### lowpass~ 
2nd-order resonant lowpass filter.

### lop2~ 
1st-order lowpass filter (1-pole, 1-zero).

### mov.avg~ 
Moving average over `n` samples, acting as a lowpass filter.

---

## Highpass Filters

### hip.bw~ 
Highpass Butterworth filter abstraction. Specify cutoff frequency and order (2nd to 100th).

### highpass~ 
2nd-order resonant highpass filter.

---

## Bandpass/Bandstop Filters

### bandpass~ 
2nd-order bandpass filter.

### bandstop~ 
2nd-order band reject/notch filter.

### bpbank~ 
Bank of `bandpass~` objects. Configure via frequency list with multichannel output.

---

## Shelving Filters

### highshelf~ 
2nd-order highshelf filter.

### lowshelf~ 
2nd-order lowshelf filter.

---

## Resonators & Comb Filters

### resonant~ 
2nd-order bandpass resonator with decay/Q control. Gain increases with Q.

### resonant2~ 
Like `resonant~` but adds attack time control.

### resonbank~ 
Bank of `resonant~` objects. Configure via parameter lists.

### resonbank2~ 
Bank of `resonant2~` objects with multichannel support.

### comb.filt~ 
Resonator comb filter.

### vcf2~ 
Complex one-pole resonant filter optimized for impulse excitation. Basis of `damp.osc~`.

---

## State-Variable Filters

### svfilter~ 
Chamberlin's state-variable filter. Outputs **lowpass, highpass, bandpass, bandstop** in parallel.

---

## Crossover Filters

### crossover~ 
3rd-order Butterworth crossover filter.

---

## Parametric EQ

### eq~ 
2nd-order parametric equalizer (peak/notch).

---

## Biquad Filters

### biquads~ 
Cascaded biquad sections (up to 50 stages). Configure via coefficient lists.

### bicoeff2 
Generates coefficients for Pd Vanilla's `biquad~`. All inlets are hot.

---

## Utility & Miscellaneous

### bitnormal~ 

Replaces NaN/infinity/denormals with zero. Supports multichannel signals.
