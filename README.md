# Club

![club banner](https://github.com/jesus-333/club/blob/main/images/club_banner_chatGPT.png)

CLI wrapper for the [caveman_compression](https://github.com/wilpel/caveman-compression) by wilpel. 
The name of the tool (club) is a kinda of a joke since this wrapper is a CLI tool and the club was one of the caveman's main tools.

This project was born simply from my curiosity in trying to develop a tool for the CLI. 
I made some small updates to the original scripts (see [updates](#updates) sections) but all credit for the original code goes to original authors.

## List of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#example)
- [Updates](#updates)

## Installation

To install `club` you will first need [pipx](https://github.com/pypa/pipx) (you can easily install it through `brew`, `pip` or `scoop` based on your system/preferences)

<details>

<summary>How to install pipx</summary>

### pipx installation

#### MacOs (brew)
```sh
brew install pipx
```

#### Python (pip)
```sh
pip install pipx
```

#### Windows
```sh
scoop install pipx
```

#### Check installation
To check if `pipx` has been installed correctly you can run the following command :
```sh
pipx ensurepath
```

</details>

After installing `pipx` you can simply install `club` using the command
```sh
pipx install caveman-club
```

(Don't ask me why but when I upload the packet on Pypi the name `club` was not allowed for a package, although I couldn't find anyone else using it)

## Usage
Club offers the same functionality as the base package but wrapped in a command for CLI. It basically allows you to compress/decompress text through 3 techniques: NLP, MLM and LLM (see [here](https://github.com/wilpel/caveman-compression?tab=readme-ov-file#llm-based-caveman_compresspy) for details about the three methods).

The structure of a command is the following :
```
club TYPE MODALITY FLAG
```

Where :
- `TYPE` is on the 3 techniques implemented (`llm`, `mlm` and `nlp`).
- `MODALITY` can be `compress` or `decompress`
- `FLAG` are optional flags. Some flags are common between all 3 `TYPE` while others are specific to some of them (see flags sections below for more details).

E.g. if you want to compress your text with `nlp` then you can run
```sh
club nlp compress "your verbose text"
```

E.g. if you want to decompress your text with `nlp` then you can run
```sh
club nlp decompress "your verbose text"
```
For more examples see the [dedicated section](#examples) below.

Note that if you do not specify `TYPE` and write directly the `MODALITY`, then `club` will default to `nlp`. 
I.e. running `club compress "your verbose text"` is equivalent to running `club nlp compress "your verbose text"`

### Common Flag

### nlp Flag

### mlp Flag

## Examples

## Updates
This is a list of small changes/updates from the original scripts
- Add support for `metal` (MacOs) for the `mlm` method
- Changed `spacy` models import to make it automated the first time the tool is used

### TODO
- [ ] Add support for other LLMs providers.
