# ConsoleCapture

An early-loading Sublime Text package that mirrors Python plugin `stdout` and
`stderr` to `Data/Log/ConsoleCapture.log` in a portable installation. It keeps
five files of up to 2 MiB each by default: the current `.log` and `.log.1`
through `.log.4`. It rotates at startup and when the current file reaches the
size limit. A single output message larger than the limit may temporarily make
one file larger than 2 MiB.

Build with `python build.py 00_ConsoleCapture.sublime-package` and place the
result in `Data/Installed Packages`. The `00_` name loads the logger before
other installed packages. The `.python-version` value `3.8` selects Python
3.8 on older Sublime Text builds and Python 3.14 on build 4205 or newer; older
builds use Python 3.3.

To change the limits, create `Data/Packages/User/ConsoleCapture.json`:

```json
{"max_files": 5, "max_bytes": 2097152}
```

`max_files` includes the current file. Changes take effect when Sublime Text
reloads the package or restarts. The logger captures output from its Python
plugin host after it loads. It cannot recover earlier output or capture native
messages written directly by the Sublime Text process.
