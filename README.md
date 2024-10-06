# Personal Latex Suite Shortcuts

[snippets.txt](./snippets.txt) is a collection of Latex snippets that I use with the [Obsidian Latex Suite](https://github.com/artisticat1/obsidian-latex-suite) extension. I have created these snippets to make it easier to write Latex in Obsidian. I have also included some snippets that are not part of the Latex Suite extension, but are useful for writing vector calculus and certain electromagnetics equations.

## Installation

1. Download and install [Obsidian](https://obsidian.md/download).
2. Install the Latex Suite plugin by going to `Settings > Community plugins > Browse` and searching for "Latex Suite". Alternatively, you can click [here](https://obsidian.md/plugins?search=latex%20suite#).
3. In settings, go to `Latex Suite` and in the `Snippets` section. Copy and paste the contents of [snippets.txt](./snippets.txt) into the text box. Alternatively, you can download the [snippets.txt](./snippets.txt) file, place it in your Obsidian vault, enable "Load snippets from file or folder" and select the file.

## Usage
Refer to the [Obsidian Latex Suite documentation](https://github.com/artisticat1/obsidian-latex-suite) for more information on how to use the extension. The cheatsheet of my personal snippets are shown below.

# LaTeX Snippets Cheatsheet

## Math mode

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `mk` | `$$0$` | `tA` |  |
| `dm` | `$$\n$0\n$$` | `tAw` |  |
| `beg` | `\\begin{$0}\n$1\n\\end{$0}` | `mA` |  |

---

## Greek letters

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `@a` | `\\alpha` | `mA` |  |
| `@b` | `\\beta` | `mA` |  |
| `@c` | `\\psi` | `mA` |  |
| `@C` | `\\Psi` | `mA` |  |
| `@d` | `\\delta` | `mA` |  |
| `@D` | `\\Delta` | `mA` |  |
| `@e` | `\\epsilon` | `mA` |  |
| `:e` | `\\varepsilon` | `mA` |  |
| `@f` | `\\phi` | `mA` |  |
| `@F` | `\\Phi` | `mA` |  |
| `@g` | `\\gamma` | `mA` |  |
| `@G` | `\\Gamma` | `mA` |  |
| `@h` | `\\eta` | `mA` |  |
| `@i` | `\\iota` | `mA` |  |
| `@j` | `\\xi` | `mA` |  |
| `@J` | `\\Xi` | `mA` |  |
| `@k` | `\\kappa` | `mA` |  |
| `@k` | `\\kappa` | `mA` |  |
| `@l` | `\\lambda` | `mA` |  |
| `@L` | `\\Lambda` | `mA` |  |
| `@m` | `\\mu` | `mA` |  |
| `@n` | `\\nu` | `mA` |  |
| `@p` | `\\pi` | `mA` |  |
| `@P` | `\\Pi` | `mA` |  |
| `@r` | `\\rho` | `mA` |  |
| `@s` | `\\sigma` | `mA` |  |
| `@S` | `\\Sigma` | `mA` |  |
| `:s` | `\\varsigma` | `mA` |  |
| `@t` | `\\tau` | `mA` |  |
| `@u` | `\\theta` | `mA` |  |
| `@U` | `\\Theta` | `mA` |  |
| `:u` | `\\vartheta` | `mA` |  |
| `@w` | `\\omega` | `mA` |  |
| `@W` | `\\Omega` | `mA` |  |
| `@x` | `\\chi` | `mA` |  |
| `@x` | `\\Chi` | `mA` |  |
| `@y` | `\\upsilon` | `mA` |  |
| `@Y` | `\\Upsilon` | `mA` |  |
| `@z` | `\\zeta` | `mA` |  |
| `sig` | `\\sigma` | `mA` |  |
| `eps` | `\\varepsilon` | `mA` |  |
| `ow` | `\\omega` | `mA` |  |

---

## Text environment

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `text` | `\\text{$0}$1` | `mA` |  |
| `\` | `\\text{$0}$1` | `mA` |  |

---

## Basic operations

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `sr` | `^{2}` | `mA` |  |
| `cb` | `^{3}` | `mA` |  |
| `rd` | `^{$0}$1` | `mA` |  |
| `__` | `_{$0}$1` | `mA` |  |
| `sts` | `_\\text{$0}` | `mA` |  |
| `sq` | `\\sqrt{ $0 }$1` | `mA` |  |
| `` | `\\frac{$0}{$1}$2` | `mA` |  |
| `ee` | `e^{\\Huge $0 }$1` | `mA` |  |
| `ej` | `e^{\\Huge j $0 }$1` | `mA` |  |
| `en` | `e^{\\Huge -j $0 }$1` | `mA` |  |
| `sn` | `^{-}$1` | `mA` |  |
| `sp` | `^{+}$1` | `mA` |  |
| `invs` | `^{-1}` | `mA` |  |
| `([^\\])(exp\|log\|ln)` | `[[0]]\\[[1]]` | `rmA` |  |
| `conj` | `^{*}` | `mA` |  |
| `Re` | `\\mathrm{Re}\\{$0\\}` | `mA` |  |
| `Im` | `\\mathrm{Im}\\{$0\\}` | `mA` |  |
| `bf` | `\\mathbf{$0}` | `mA` |  |
| `rm` | `\\mathrm{$0}$1` | `mA` |  |

---

## Linear algebra

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `([^\\])(det)` | `[[0]]\\[[1]]` | `rmA` |  |
| `trace` | `\\mathrm{Tr}` | `mA` |  |

---

## Derivatives

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `ddt` | `\\frac{d}{dt} ` | `mA` |  |
| `par` | `\\frac{ \\partial ${0:y} }{ \\partial ${1:x} } $2` | `m` |  |
| `dpar` | `\\frac{ \\partial^2 ${0:y} }{ \\partial ${1:x}^2 } $2` | `m` |  |
| `grad` | `\\nabla ` | `mA` |  |
| `curl` | `\\nabla \\times ` | `mA` |  |
| `dcurl` | `\\nabla \\times \\nabla \\times ` | `mA` |  |
| `div` | `\\nabla \\cdot ` | `mA` |  |
| `lapl` | `\\nabla^2 ` | `mA` |  |
| `pa([A-Za-z])([A-Za-z])` | `\\frac{ \\partial [[0]] }{ \\partial [[1]] } ` | `rm` |  |

---

## Integrals

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `\\int` | `\\int $0 \\, d${1:x} $2` | `m` |  |
| `dint` | `\\int_{${0:0}}^{${1:1}} $3 \\, d${2:x} $4` | `mA` |  |
| `oint` | `\\oint` | `mA` |  |
| `iint` | `\\iint` | `mA` |  |
| `iiint` | `\\iiint` | `mA` |  |
| `cint` | `\\oint_{${0:C}} $1 \\cdot d${2:\\mathbf{l}}` | `mA` |  |
| `Sint` | `\\iint_{${0:S}} $1 \\cdot d${2:\\mathbf{s}}` | `mA` |  |
| `oSint` | `{\\huge∯}_{${0:S}} $1 \\cdot d${2:\\mathbf{s}}` | `mA` |  |
| `vint` | `\\iiint_{${0:V}} $1 \ d${2:v}` | `mA` |  |
| `uint` | `\\int_{0}^{\\infty} $0 \\, d${1:x} $2` | `mA` |  |
| `tint` | `\\int_{-\\infty}^{\\infty} $0 \\, d${1:x} $2` | `mA` |  |

---

## Electromagnetics

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `jw` | `j\\omega ` | `mA` |  |
| `er` | `\\varepsilon_{r}` | `rmA` |  |
| `mr` | `\\mu_{r}` | `rmA` |  |
| `E([xyz])\\1` | `E_[[0]] ` | `rmA` |  |
| `H([xyz])\\1` | `H_[[0]] ` | `rmA` |  |
| `k([xyz])\\1` | `k_[[0]] ` | `rmA` |  |
| `E([itr])\\1` | `\\mathbf{E}^[[0]] ` | `rmA` |  |
| `H([itr])\\1` | `\\mathbf{H}^[[0]] ` | `rmA` |  |
| `k([itr])\\1` | `\\mathbf{k}^[[0]] ` | `rmA` |  |
| `E([itr])([xyz])` | `E_[[1]]^[[0]] ` | `rmA` |  |
| `H([itr])([xyz])` | `H_[[1]]^[[0]] ` | `rmA` |  |
| `k([itr])([xyz])` | `k_[[1]]^[[0]] ` | `rmA` |  |

---

## Special Functions

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `Jbes(\d\|n\|m\|p)` | `J_[[0]] ($0) $1` | `rmA` |  |
| `Ybes(\d\|n\|m\|p)` | `Y_[[0]] ($0) $1` | `rmA` |  |
| `jbes(\d\|n\|m\|p)` | `j_[[0]] ($0) $1` | `rmA` |  |
| `ybes(\d\|n\|m\|p)` | `y_[[0]] ($0) $1` | `rmA` |  |
| `Ibes(\d\|n\|m\|p)` | `I_[[0]] ($0) $1` | `rmA` |  |
| `Kbes(\d\|n\|m\|p)` | `K_[[0]] ($0) $1` | `rmA` |  |
| `Pleg(\d\|n\|m\|p)` | `P_[[0]] ($0) $1` | `rmA` |  |
| `Qleg(\d\|n\|m\|p)` | `Q_[[0]] ($0) $1` | `rmA` |  |
| `2Hank(\d\|n\|m\|p)` | `H_[[0]]^{(2)} ($0) $1` | `rmA` |  |
| `1Hank(\d\|n\|m\|p)` | `H_[[0]]^{(1)} ($0) $1` | `rmA` |  |
| `2hank(\d\|n\|m\|p)` | `h_[[0]]^{(2)} ($0) $1` | `rmA` |  |
| `1hank(\d\|n\|m\|p)` | `h_[[0]]^{(1)} ($0) $1` | `rmA` |  |

---

## More operations

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `([a-zA-Z])bas` | `\\hat{\\mathbf{[[0]]}}` | `rmA` |  |
| `([a-zA-Z])bss` | `\\hat{\\mathbf{a}}_[[0]] ` | `rmA` |  |
| `([a-zA-Z])tens` | `\\overline{\\overline{[[0]]}}` | `rmA` |  |
| `([a-zA-Z])hat` | `\\hat{[[0]]}` | `rmA` |  |
| `([a-zA-Z])bar` | `\\bar{[[0]]}` | `rmA` |  |
| `([a-zA-Z])tilde` | `\\tilde{[[0]]}` | `rmA` |  |
| `([a-zA-Z])und` | `\\underline{[[0]]}` | `rmA` |  |
| `([a-zA-Z])vec` | `\\vec{[[0]]}` | `rmA` |  |
| `([a-zA-Z]),\\.` | `\\mathbf{[[0]]}` | `rmA` |  |
| `([a-zA-Z])\\.,` | `\\mathbf{[[0]]}` | `rmA` |  |
| `\\\\(${GREEK}),\\.` | `\\boldsymbol{\\[[0]]}` | `rmA` |  |
| `\\\\(${GREEK})\\.,` | `\\boldsymbol{\\[[0]]}` | `rmA` |  |
| `bas` | `\\hat{\\mathbf{$0}}$1` | `mA` |  |
| `bss` | `\\hat{\\mathbf{a}}_{$0}$1` | `mA` |  |
| `tens` | `\\overline{\\overline{$0}}$1` | `mA` |  |
| `hat` | `\\hat{$0}$1` | `mA` |  |
| `bar` | `\\bar{$0}$1` | `mA` |  |
| `ddot` | `\\ddot{$0}$1` | `mA` |  |
| `cdot` | `\\cdot` | `mA` |  |
| `tilde` | `\\tilde{$0}$1` | `mA` |  |
| `und` | `\\underline{$0}$1` | `mA` |  |
| `vec` | `\\vec{$0}$1` | `mA` |  |

---

## Insert space after Greek letters and symbols

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `\\\\(${GREEK}\|${SYMBOL}\|${MORE_SYMBOLS})([A-Za-z])` | `\\[[0]] [[1]]` | `rmA` |  |
| `\\\\(${GREEK}\|${SYMBOL}) sr` | `\\[[0]]^{2}` | `rmA` |  |
| `\\\\(${GREEK}\|${SYMBOL}) cb` | `\\[[0]]^{3}` | `rmA` |  |
| `\\\\(${GREEK}\|${SYMBOL}) rd` | `\\[[0]]^{$0}$1` | `rmA` |  |
| `\\\\(${GREEK}\|${SYMBOL}) bas` | `\\hat{\\mathbf{\\[[0]]}}` | `rmA` |  |
| `\\\\(${GREEK}\|${SYMBOL}) bss` | `\\hat{\\mathbf{a}}_{\\[[0]]}` | `rmA` |  |
| `\\\\(${GREEK}\|${SYMBOL}) tens` | `\\overline{\\overline{\\[[0]]}}` | `rmA` |  |
| `\\\\(${GREEK}\|${SYMBOL}) hat` | `\\hat{\\[[0]]}` | `rmA` |  |
| `\\\\(${GREEK}\|${SYMBOL}) dot` | `\\dot{\\[[0]]}` | `rmA` |  |
| `\\\\(${GREEK}\|${SYMBOL}) bar` | `\\bar{\\[[0]]}` | `rmA` |  |
| `\\\\(${GREEK}\|${SYMBOL}) vec` | `\\vec{\\[[0]]}` | `rmA` |  |
| `\\\\(${GREEK}\|${SYMBOL}) tilde` | `\\tilde{\\[[0]]}` | `rmA` |  |
| `\\\\(${GREEK}\|${SYMBOL}) und` | `\\underline{\\[[0]]}` | `rmA` |  |

---

## More auto letter subscript

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `([A-Za-z])_(\d\d)` | `[[0]]_{[[1]]}` | `rmA` |  |
| `\\hat{([A-Za-z])}(\d)` | `\\hat{[[0]]}_{[[1]]}` | `rmA` |  |
| `\\vec{([A-Za-z])}(\d)` | `\\vec{[[0]]}_{[[1]]}` | `rmA` |  |
| `\\mathbf{([A-Za-z])}(\d)` | `\\mathbf{[[0]]}_{[[1]]}` | `rmA` |  |
| `xnn` | `x_{n}` | `mA` |  |
| `xii` | `x_{i}` | `mA` |  |
| `xjj` | `x_{j}` | `mA` |  |
| `xm2` | `x_{n-2}` | `mA` |  |
| `xm1` | `x_{n-1}` | `mA` |  |
| `xp1` | `x_{n+1}` | `mA` |  |
| `xp2` | `x_{n+2}` | `mA` |  |
| `ynn` | `y_{n}` | `mA` |  |
| `yii` | `y_{i}` | `mA` |  |
| `yjj` | `y_{j}` | `mA` |  |

---

## Symbols

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `inf` | `\\infty` | `mA` |  |
| `sum` | `\\sum` | `mA` |  |
| `prod` | `\\prod` | `mA` |  |
| `\\sum` | `\\sum_{${0:i}=${1:1}}^{${2:N}} $3` | `m` |  |
| `\\prod` | `\\prod_{${0:i}=${1:1}}^{${2:N}} $3` | `m` |  |
| `lim` | `\\lim_{ ${0:n} \\to ${1:\\infty} } $2` | `mA` |  |
| `+-` | `\\pm` | `mA` |  |
| `-+` | `\\mp` | `mA` |  |
| `...` | `\\dots` | `mA` |  |

---

## {trigger: "del", replacement: "\\nabla", options: "mA"},

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `xx` | `\\times` | `mA` |  |
| `**` | `\\cdot` | `mA` |  |
| `para` | `\\parallel` | `mA` |  |
| `perp` | `\\perp` | `mA` |  |
| `===` | `\\equiv` | `mA` |  |
| `!=` | `\\neq` | `mA` |  |
| `>=` | `\\geq` | `mA` |  |
| `<=` | `\\leq` | `mA` |  |
| `>>` | `\\gg` | `mA` |  |
| `<<` | `\\ll` | `mA` |  |
| `simm` | `\\sim` | `mA` |  |
| `sim=` | `\\simeq` | `mA` |  |
| `simas` | `\\overset{$0}{\\simeq} $1` | `mA` |  |
| `prop` | `\\propto` | `mA` |  |
| `<->` | `\\leftrightarrow ` | `mA` |  |
| `->` | `\\to` | `mA` |  |
| `!>` | `\\mapsto` | `mA` |  |
| `=>` | `\\implies` | `mA` |  |
| `=<` | `\\impliedby` | `mA` |  |
| `and` | `\\cap` | `mA` |  |
| `orr` | `\\cup` | `mA` |  |
| `inn` | `\\in` | `mA` |  |
| `att` | `\|_{$0} $1` | `mA` |  |
| `notin` | `\\not\\in` | `mA` |  |
| `\\\\\\` | `\\setminus` | `mA` |  |
| `sub=` | `\\subseteq` | `mA` |  |
| `sup=` | `\\supseteq` | `mA` |  |
| `eset` | `\\emptyset` | `mA` |  |
| `set` | `\\{ $0 \\}$1` | `mA` |  |
| `LL` | `\\mathcal{L}` | `mA` |  |
| `HH` | `\\mathcal{H}` | `mA` |  |
| `CC` | `\\mathbb{C}` | `mA` |  |
| `RR` | `\\mathbb{R}` | `mA` |  |
| `ZZ` | `\\mathbb{Z}` | `mA` |  |
| `NN` | `\\mathbb{N}` | `mA` |  |

---

## You can edit snippet variables under the Advanced snippet settings section.

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `([^\\\\])(${GREEK})` | `[[0]]\\[[1]]` | `rmA` | Add backslash before Greek letters |
| `([^\\\\])(${SYMBOL})` | `[[0]]\\[[1]]` | `rmA` | Add backslash before symbols |

---

## Trigonometry

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `([^\\])(arcsin\|sin\|arccos\|cos\|arctan\|tan\|csc\|sec\|cot)` | `[[0]]\\[[1]]` | `rmA` | Add backslash before trig funcs |

---

## Replace the first occurrence of '=' with '&=' in the selected text

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `U` | `\\underbrace{ ${VISUAL} }_{ $0 }` | `mA` |  |
| `O` | `\\overbrace{ ${VISUAL} }^{ $0 }` | `mA` |  |
| `B` | `\\underset{ $0 }{ ${VISUAL} }` | `mA` |  |
| `C` | `\\cancel{ ${VISUAL} }` | `mA` |  |
| `K` | `\\cancelto{ $0 }{ ${VISUAL} }` | `mA` |  |
| `S` | `\\sqrt{ ${VISUAL} }` | `mA` |  |

---

## Physics

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `kbt` | `k_{B}T` | `mA` |  |
| `msun` | `M_{\\odot}` | `mA` |  |

---

## Quantum mechanics

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `dag` | `^{\\dagger}` | `mA` |  |
| `o+` | `\\oplus ` | `mA` |  |
| `ox` | `\\otimes ` | `mA` |  |
| `bra` | `\\bra{$0} $1` | `mA` |  |
| `ket` | `\\ket{$0} $1` | `mA` |  |
| `brk` | `\\braket{ $0 \| $1 } $2` | `mA` |  |
| `outer` | `\\ket{${0:\\psi}} \\bra{${0:\\psi}} $1` | `mA` |  |

---

## Chemistry

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `pu` | `\\pu{ $0 }` | `mA` |  |
| `cee` | `\\ce{ $0 }` | `mA` |  |
| `he4` | `{}^{4}_{2}He ` | `mA` |  |
| `he3` | `{}^{3}_{2}He ` | `mA` |  |
| `iso` | `{}^{${0:4}}_{${1:2}}${2:He}` | `mA` |  |

---

## Environments

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `pmat` | `\\begin{pmatrix}\n$0\n\\end{pmatrix}` | `MA` |  |
| `bmat` | `\\begin{bmatrix}\n$0\n\\end{bmatrix}` | `MA` |  |
| `Bmat` | `\\begin{Bmatrix}\n$0\n\\end{Bmatrix}` | `MA` |  |
| `vmat` | `\\begin{vmatrix}\n$0\n\\end{vmatrix}` | `MA` |  |
| `Vmat` | `\\begin{Vmatrix}\n$0\n\\end{Vmatrix}` | `MA` |  |
| `matrix` | `\\begin{matrix}\n$0\n\\end{matrix}` | `MA` |  |
| `pmat` | `\\begin{pmatrix}$0\\end{pmatrix}` | `nA` |  |
| `bmat` | `\\begin{bmatrix}$0\\end{bmatrix}` | `nA` |  |
| `Bmat` | `\\begin{Bmatrix}$0\\end{Bmatrix}` | `nA` |  |
| `vmat` | `\\begin{vmatrix}$0\\end{vmatrix}` | `nA` |  |
| `Vmat` | `\\begin{Vmatrix}$0\\end{Vmatrix}` | `nA` |  |
| `matrix` | `\\begin{matrix}$0\\end{matrix}` | `nA` |  |
| `cases` | `\\begin{cases}\n$0\n\\end{cases}` | `mA` |  |
| `align` | `\\begin{align}\n$0\n\\end{align}` | `mA` |  |
| `array` | `\\begin{array}\n$0\n\\end{array}` | `mA` |  |

---

## Brackets

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `avg` | `\\langle $0 \\rangle $1` | `mA` |  |
| `abs` | `\\left\| $0 \\right\| $1` | `mA` |  |
| `ceil` | `\\lceil $0 \\rceil $1` | `mA` |  |
| `floor` | `\\lfloor $0 \\rfloor $1` | `mA` |  |
| `\|` | `\\left\|${VISUAL} \\right\|` | `mA` |  |
| `(` | `(${VISUAL})` | `mA` |  |
| `[` | `[${VISUAL}]` | `mA` |  |
| `{` | `{${VISUAL}}` | `mA` |  |
| `(` | `($0)$1` | `mA` |  |
| `{` | `{$0}$1` | `mA` |  |
| `[` | `[$0]$1` | `mA` |  |
| `lr(` | `\\left( $0 \\right) $1` | `mA` |  |
| `lr{` | `\\left\\{ $0 \\right\\} $1` | `mA` |  |
| `lr[` | `\\left[ $0 \\right] $1` | `mA` |  |
| `lr\|` | `\\left\| $0 \\right\| $1` | `mA` |  |
| `lra` | `\\left< $0 \\right> $1` | `mA` |  |

---

## Snippet replacements can have placeholders.

| **Trigger** | **Replacement** | **Options** | **Description** |
|-------------|-----------------|-------------|-----------------|
| `tayl` | `${0:f}(${1:x} + ${2:h}) = ${0:f}(${1:x}) + ${0:f}'(${1:x})${2:h} + ${0:f}''(${1:x}) \\frac{${2:h}^{2}}{2!} + \\dots$3` | `mA` | Taylor expansion |

---

