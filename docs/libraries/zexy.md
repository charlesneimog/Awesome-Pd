---
search:
    exclude: true
---

# zexy

<h2>Contributors</h2>

<div id="libcontributors"></div>

<p align="center">
<i>People who contribute to this project.</i>
</p>


<script>
async function updateList() {
    const repoOwner = 'pd';
    const repoName = 'zexy';
    try {
        const res = await fetch(`https://api.github.com/repos/${repoOwner}/${repoName}/contributors`);
        const contributors = await res.json();
        const container = document.getElementById('libcontributors');
        contributors.forEach(user => {
            const link = document.createElement('a');
            link.href = `https://github.com/${user.login}`;
            link.target = '_blank';
            const img = document.createElement('img');
            img.src = `https://github.com/${user.login}.png?size=100`;
            img.alt = user.login;
            img.className = 'libavatar';
            link.appendChild(img);
            container.appendChild(link);
        });
    } catch(err) {
        console.error(err);
    }
}
updateList();
</script>


<h2>Objects</h2>

<div class="grid cards" markdown>
- :material-tune: [__&&~__](../objects/&&~.md) The `&&~` object performs a logical AND operation on two input signals.
- :material-tune: [__0x3c0x7e__](../objects/0x3c0x7e.md) This Pure Data object, `0x3c0x7e`, is an abstraction for the signal comparison object `<~`.
- :material-tune: [__0x3e0x7e__](../objects/0x3e0x7e.md) The `>~` object compares two incoming audio signals, outputting a signal that is true (non-zero) when the first inlet's signal is greater than the second.
- :material-tune: [__0x7c0x7c0x7e__](../objects/0x7c0x7c0x7e.md) The Pure Data object `||~` performs a logical OR operation on two incoming audio signals.
- :material-tune: [__==~__](../objects/==~.md) The `==~` object compares two incoming audio signals for equality, outputting a signal that indicates whether they are identical.
- :material-tune: [__a2l__](../objects/a2l.md) The `a2l` object converts any incoming message into a list, providing a unified data format for further processing.
- :material-tune: [__absgn~__](../objects/absgn~.md) The `absgn~` object calculates the absolute value and the signum of an incoming audio signal.
- :material-tune: [__abs~__](../objects/abs~.md) The `abs~` object calculates the absolute value of an incoming audio signal.
- :material-tune: [__any2list__](../objects/any2list.md) The `any2list` object converts any incoming message into a list, standardizing various message types into a list format for further processing.
- :material-tune: [__atof__](../objects/atof.md) The `atof` object converts an ASCII symbol (text) into a floating-point number.
- :material-tune: [__atoi__](../objects/atoi.md) The `atoi` object converts an incoming symbol (string) into a numerical representation.
- :material-tune: [__avg~__](../objects/avg~.md) The `avg~` object calculates the arithmetic mean of an incoming audio signal.
- :material-tune: [__blockmirror~__](../objects/blockmirror~.md) The `blockmirror~` object reverses an incoming audio signal in time, processing it in fixed-size blocks (signal vectors).
- :material-tune: [__blockswap~__](../objects/blockswap~.md) The `blockswap~` object swaps the upper and lower halves of an incoming audio signal vector.
- :material-tune: [__cart2pol__](../objects/cart2pol.md) The `cart2pol` object converts 3D Cartesian coordinates (x, y, z) into 3D polar coordinates.
- :material-tune: [__cart2sph__](../objects/cart2sph.md) The `cart2sph` object converts 3D Cartesian coordinates (x, y, z) into spherical coordinates (radius, azimuth, elevation).
- :material-tune: [__coordinates__](../objects/coordinates.md) The `cart2pol`, `pol2sph`, `sph2cart`, `cart2sph`, `pol2cart`, and `sph2pol` objects convert between Cartesian, Polar, and Spherical coordinate systems.
- :material-tune: [__date__](../objects/date.md) The `date` object retrieves the current system date and time.
- :material-tune: [__deg2rad__](../objects/deg2rad.md) The `deg2rad` object converts a float value from degrees to radians.
- :material-tune: [__demultiplex__](../objects/demultiplex.md) The `demultiplex` object routes data from its left inlet to one of its outlets.
- :material-tune: [__demultiplex~__](../objects/demultiplex~.md) The `demultiplex~` (or `demux~`) object takes a single audio or control signal and routes it to one of its multiple outlets.
- :material-tune: [__demux__](../objects/demux.md) The `demux` object acts as a demultiplexer, routing data from its left inlet to one of its multiple outlets.
- :material-tune: [__demux~__](../objects/demux~.md) The `demux~` object acts as a signal demultiplexer, routing a single audio signal from its inlet to one of its multiple outlets.
- :material-tune: [__dfreq~__](../objects/dfreq~.md) The `dfreq~` object is a computationally efficient frequency detector that estimates the frequency of an incoming audio signal by counting zero-crossings.
- :material-tune: [__digidistort__](../objects/digidistort.md) The `digidistort` object provides digital distortion effects for audio signals.
- :material-tune: [__dirac~__](../objects/dirac~.md) The `dirac~` object generates a single unit sample (a unit impulse) as an audio signal.
- :material-tune: [__drip__](../objects/drip.md) The `drip` object unfolds a package (list) into a sequence of individual elements, outputting them one by one with a configurable delay in milliseconds.
- :material-tune: [__envrms~__](../objects/envrms~.md) The `envrms~` object is an envelope follower designed for audio signals.
- :material-tune: [__fifop__](../objects/fifop.md) The `fifop` object implements a First-In-First-Out (FIFO) queue system that manages multiple internal queues, each capable of being assigned a floating-point priority.
- :material-tune: [__freadln__](../objects/freadln.md) The `freadln` object reads text files line by line, outputting each line as a list.
- :material-tune: [__fwriteln__](../objects/fwriteln.md) The `fwriteln` object writes text files line by line, serving as a simplified version of `textfile`.
- :material-tune: [__glue__](../objects/glue.md) The `glue` object combines two "packages" or messages, typically by appending or prepending one to the other.
- :material-tune: [__index__](../objects/index.md) The `index` object creates and manages a symbol-to-integer map, allowing you to associate unique symbols with numerical indices.
- :material-tune: [__l__](../objects/l.md) The `l` object (an alias for `list`) is used to store and manipulate lists in Pure Data.
- :material-tune: [__l2i__](../objects/l2i.md) The `l2i` object converts all floating-point numbers within an incoming list to integers.
- :material-tune: [__l2s__](../objects/l2s.md) The `list2symbol` (or `l2s`) object converts an incoming list into a single symbol.
- :material-tune: [__length__](../objects/length.md) The `length` object, part of the `zexy` external library, determines the number of elements in an incoming list.
- :material-tune: [__lifop__](../objects/lifop.md) The `lifop` object manages multiple Last-In-First-Out (LIFO) stacks, each assigned a floating-point priority.
- :material-tune: [__limiter~__](../objects/limiter~.md) The `limiter~` object in Pure Data functions as an audio dynamics processor, preventing signals from exceeding a specified output level to avoid clipping.
- :material-tune: [__list2int__](../objects/list2int.md) The `list2int` object converts all floating-point numbers within an incoming list to integers.
- :material-tune: [__list2lists__](../objects/list2lists.md) The `list2lists` object splits an incoming list into multiple sublists.
- :material-tune: [__list2symbol__](../objects/list2symbol.md) The `list2symbol` object converts an incoming list into a single symbol.
- :material-tune: [__lister__](../objects/lister.md) The `lister` object (alias `l`) stores and outputs lists, and can also append one list to another.
- :material-tune: [__listfind__](../objects/listfind.md) The `listfind` object searches for occurrences of a sublist within a larger list.
- :material-tune: [__longload__](../objects/longload.md) The `longload` object is an experimental utility designed to simulate a long loading time within a Pure Data patch.
- :material-tune: [__lpt__](../objects/lpt.md) The `lpt` object in Pure Data allows writing and reading data to and from a computer's parallel port.
- :material-tune: [__makesymbol__](../objects/makesymbol.md) The `makesymbol` object converts an incoming list (up to 10 members) into a single symbol.
- :material-tune: [__matchbox__](../objects/matchbox.md) The `matchbox` object stores a collection of lists and retrieves them based on various matching algorithms.
- :material-tune: [__mavg__](../objects/mavg.md) The `mavg` object implements a moving average filter, smoothing incoming float values by averaging a specified number of recent samples.
- :material-tune: [__mean__](../objects/mean.md) The `mean` object calculates the arithmetic mean (average) of a list of floating-point numbers.
- :material-tune: [__minmax__](../objects/minmax.md) The `minmax` object takes a list of floating-point numbers as input.
- :material-tune: [__msgfile__](../objects/msgfile.md) The `msgfile` object reads and writes messages to text files, extending the functionality of `textfile`.
- :material-tune: [__multiline~__](../objects/multiline~.md) The `multiline~` object performs line-interpolated multiplication of multiple input signals.
- :material-tune: [__multiplex__](../objects/multiplex.md) The `multiplex` object routes data from one of its multiple inlets to a single outlet.
- :material-tune: [__multiplex~__](../objects/multiplex~.md) The `multiplex~` object functions as a signal multiplexer, allowing you to select one signal from multiple inputs to be passed to a single output.
- :material-tune: [__multireceive__](../objects/multireceive.md) The `multireceive` object allows a single outlet to receive messages from multiple `send` objects.
- :material-tune: [__mux__](../objects/mux.md) The `mux` object functions as a multiplexer, directing the signal from one of its multiple input inlets to its single outlet.
- :material-tune: [__mux~__](../objects/mux~.md) The `mux~` object acts as a signal multiplexer, routing one of its multiple signal inlets to a single signal outlet.
- :material-tune: [__niagara__](../objects/niagara.md) The `niagara` object divides an incoming message or list into two sub-packages.
- :material-tune: [__noish~__](../objects/noish~.md) The `noish~` object generates bandlimited noise by drawing a random number every `n` samples and interpolating between these values.
- :material-tune: [__noisi~__](../objects/noisi~.md) The `noisi~` object generates bandlimited noise by drawing random numbers at a specified rate in Hz and interpolating between them.
- :material-tune: [__nop__](../objects/nop.md) The `nop` object in Pure Data acts as a "no operation" pass-through.
- :material-tune: [__nop~__](../objects/nop~.md) The `nop~` object is a signal-level no-operation (NOP) utility from the zexy library.
- :material-tune: [__operating_system__](../objects/operating_system.md) The `operating_system` object outputs a symbol representing the operating system Pure Data is currently running on.
- :material-tune: [__pack__](../objects/pack.md) The `pack` object combines multiple incoming atoms (numbers, symbols, or pointers) from its inlets into a single list message.
- :material-tune: [__packel__](../objects/packel.md) The `packel` object extracts elements from a list, referred to as a "package." It can retrieve a specific element by its index (positive for from the beginning, negative for from the end), or the entire list if the index is 0.
- :material-tune: [__pack~__](../objects/pack~.md) The `pack~` object converts incoming audio signals into lists of floating-point numbers.
- :material-tune: [__pdf~__](../objects/pdf~.md) The `pdf~` object calculates the probability density function of an incoming signal.
- :material-tune: [__pol2cart__](../objects/pol2cart.md) The `pol2cart` object converts 3D polar coordinates (radius `r`, azimuthal angle `phi`, and polar angle `theta`) into Cartesian coordinates (x, y, z).
- :material-tune: [__pol2sph__](../objects/pol2sph.md) The `pol2sph` object converts 2D polar coordinates (radius, angle, and height) into 3D spherical coordinates.
- :material-tune: [__polyfun__](../objects/polyfun.md) The `polyfun` object evaluates a polynomial function.
- :material-tune: [__prime__](../objects/prime.md) The `prime` object detects if an input number is prime.
- :material-tune: [__quantize~__](../objects/quantize~.md) The `quantize~` object quantizes an incoming audio signal to a variable number of steps.
- :material-tune: [__rad2deg__](../objects/rad2deg.md) The `rad2deg` object converts radian values to degrees.
- :material-tune: [__rawprint__](../objects/rawprint.md) The `rawprint` object, part of the `zexy` external library, provides a raw message printing functionality.
- :material-tune: [__regex__](../objects/regex.md) The `regex` object checks if an input symbol matches a given regular expression.
- :material-tune: [__regex-help__](../objects/regex-help.md) The `regex` object checks if an incoming symbol matches a specified regular expression.
- :material-tune: [__relay__](../objects/relay.md) The `relay` object routes incoming messages based on their first element.
- :material-tune: [__repack__](../objects/repack.md) The `repack` object in Pure Data is used to (re)pack various data types—floats, symbols, or pointers—into fixed-size packages.
- :material-tune: [__repeat__](../objects/repeat.md) The `repeat` object in Pure Data outputs any incoming message a specified number of times.
- :material-tune: [__route~__](../objects/route~.md) The `route~` object, part of the zexy library, separates incoming audio signals from control messages.
- :material-tune: [__s2l__](../objects/s2l.md) The `s2l` object converts an input symbol into a list.
- :material-tune: [__scalarmult__](../objects/scalarmult.md) The `scalarmult` object performs scalar multiplication, also known as a "dot product," on incoming lists of numbers.
- :material-tune: [__segregate__](../objects/segregate.md) The `segregate` object sorts incoming messages by their data type, sending them to dedicated outlets.
- :material-tune: [__sf-play_record__](../objects/sf-play_record.md) The `sf-play_record` object provides a hard disk recording and playback system for Pure Data, enabling multi-track audio recordings.
- :material-tune: [__sgn~__](../objects/sgn~.md) The `sgn~` object calculates the signum of an incoming audio signal, outputting `1` for positive values, `-1` for negative values, and `0` for zero.
- :material-tune: [__sigzero~__](../objects/sigzero~.md) The `sigzero~` object detects the presence or absence of an audio signal.
- :material-tune: [__sort__](../objects/sort.md) The `sort` object sorts a list of floating-point numbers using a shell sort algorithm.
- :material-tune: [__sph2cart__](../objects/sph2cart.md) The `sph2cart` object converts spherical coordinates (radius, azimuth, elevation) to Cartesian coordinates (x, y, z).
- :material-tune: [__sph2pol__](../objects/sph2pol.md) The `sph2pol` object converts spherical coordinates (radius R, azimuthal angle phi, and polar angle theta) into polar coordinates.
- :material-tune: [__step~__](../objects/step~.md) The `step~` object generates an audio signal that is either a unit step sequence or a rectangular window.
- :material-tune: [__strcmp__](../objects/strcmp.md) The `strcmp` object compares two lists as if they were strings, similar to the `strcmp` function in C programming.
- :material-tune: [__sum__](../objects/sum.md) The `sum` object takes a list of numbers as its input.
- :material-tune: [__swap~__](../objects/swap~.md) The `swap~` object processes incoming audio signals by first converting them to a 16-bit format.
- :material-tune: [__symbol2list__](../objects/symbol2list.md) The `symbol2list` object converts an incoming symbol into a list.
- :material-tune: [__tabdump__](../objects/tabdump.md) The `tabdump` object outputs the entire contents of a Pure Data table as a list.
- :material-tune: [__tabminmax__](../objects/tabminmax.md) The `tabminmax` object finds the minimum and maximum values within a Pure Data table.
- :material-tune: [__tabset__](../objects/tabset.md) The `tabset` object from the `zexy` library allows users to set the contents of a Pure Data table.
- :material-tune: [__tavg~__](../objects/tavg~.md) The `tavg~` object calculates the arithmetic mean of an incoming audio signal.
- :material-tune: [__time__](../objects/time.md) The `time` object outputs the current system time in milliseconds, seconds, minutes, and hours when triggered by a `bang`.
- :material-tune: [__uniqsym__](../objects/uniqsym.md) The `uniqsym` object removes duplicate symbols from a list or stream, maintaining a unique set of values.
- :material-tune: [__unpack__](../objects/unpack.md) The `unpack` object splits an incoming message or list into its individual atoms, sending each atom to a separate outlet.
- :material-tune: [__unpack~__](../objects/unpack~.md) The `unpack~` object converts a list of floating-point numbers into an audio signal.
- :material-tune: [__urn__](../objects/urn.md) The `urn` object is a unique random number generator.
- :material-tune: [__wrap__](../objects/wrap.md) The `wrap` object functions as a float-capable modulo, constraining an input float value within specified limits.
- :material-tune: [__zigbinops__](../objects/zigbinops.md) The `zigbinops` help patch describes a collection of signal-rate Pure Data objects from the zexy library.
- :material-tune: [__z~__](../objects/z~.md) The `z~` object provides a sample-wise delay for audio signals, effectively implementing a `z^-N` delay.
</div>