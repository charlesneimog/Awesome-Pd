# Patching

<div class="grid cards" markdown>

- :material-tune: [__universal__](../../objects/universal.md) The `universal` object sends messages to all instances of a specified object type within the current Pure Data patch.
- :material-tune: [__properties__](../../objects/properties.md) The `properties` object in Pure Data sends a bang when its parent patch's properties are accessed, typically via a right-click menu.
- :material-tune: [__canvas.setname__](../../objects/canvas.setname.md) `canvas.setname` assigns a symbolic name to a Pure Data canvas, enabling it to receive messages.
- :material-tune: [__funnel__](../../objects/funnel.md) The `funnel` object receives data from multiple inlets and outputs it through a single outlet, tagging the incoming data with its inlet number.
- :material-tune: [__canvas.zoom__](../../objects/canvas.zoom.md) The `canvas.zoom` object reports the zoom status of a Pure Data patch window.
- :material-tune: [__retrieve__](../../objects/retrieve.md) The `retrieve` object in Pure Data fetches data from named receive objects (`r`, `else/receiver`) or GUI elements that have built-in receive names.
- :material-tune: [__route2__](../../objects/route2.md) The `route2` object functions similarly to `route`, but it preserves the list selector in its output messages and supports both float and symbol arguments for routing.
- :material-tune: [__buddy__](../../objects/buddy.md) The `buddy` object synchronizes incoming messages from its inlets.
- :material-tune: [__canvas.gop__](../../objects/canvas.gop.md) The `canvas.gop` object retrieves information about a "graph on parent" (GOP), which is a subpatch displayed graphically within its parent patch.
- :material-tune: [__canvas.active__](../../objects/canvas.active.md) The `canvas.active` object reports the activity status of a Pure Data canvas, outputting 1 when active (front-most window) and 0 when inactive.
- :material-tune: [__synth~__](../../objects/synth~.md) `synth~` is a Pure Data object that serves as a wrapper for loading and managing monophonic or polyphonic synthesizer abstractions.
- :material-tune: [__canvas.name__](../../objects/canvas.name.md) The `canvas.name` object outputs the symbolic name of the Pure Data canvas it resides in.
- :material-tune: [__args__](../../objects/args.md) The `args` object in Pure Data manages and manipulates arguments passed to an abstraction.
- :material-tune: [__loadbanger__](../../objects/loadbanger.md) The `loadbanger` (or `lb`) object in Pure Data sends "bang" messages when a patch is loaded, when it receives any message, or when clicked.
- :material-tune: [__canvas.edit__](../../objects/canvas.edit.md) The `canvas.edit` object reports the edit status of a Pure Data canvas, outputting 1 when in edit mode and 0 in run mode.
- :material-tune: [__message__](../../objects/message.md) The `message` object in Pure Data serves as a versatile container for storing and outputting any type of message, functioning similarly to a message box but as an object.
- :material-tune: [__dollsym__](../../objects/dollsym.md) The `dollsym` object in Pure Data expands dollar-prefixed symbols like `$0-x` or `$1-y` into their corresponding values within a patch.
- :material-tune: [__loadmess__](../../objects/loadmess.md) The `loadmess` object sends a predefined message automatically when its containing patch is loaded, or when it receives a `bang` message.
- :material-tune: [__click__](../../objects/click.md) The `click` object sends a `bang` message when its parent patch (abstraction or subpatch) is clicked.
- :material-tune: [__active__](../../objects/active.md) The `active` object reports the activity status of a Pure Data patch window.
- :material-tune: [__pv__](../../objects/pv.md) The `pv` object in Pure Data functions as a private variable, storing any type of message.

</div>