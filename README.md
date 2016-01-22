## Space Shooter

The classic retro game recreated using `Pygame` and `python`.

## Demo

Follow the youtube video to see how I fared on ``spaceShooter``

[![Space Shooter Demo - Youtube](http://i.imgur.com/bHjlJfG.jpg)](https://www.youtube.com/watch?v=o99zpLsM-ZI)

## Screenshots

| ![Screen 1](http://i.imgur.com/3MzfmbT.jpg) | ![Screen 2](http://i.imgur.com/4OgIByR.png) |
|---------------------------------------------|---------------------------------------------|
| ![Screen 3](http://i.imgur.com/PFQJjE8.png) | ![Screen 4](http://i.imgur.com/lV4aIur.png) |

## Game Features

- Health bar for the space ship
- Score board to show how you are faring so far
- Power ups like
  - shield: increases the space ships life
  - bolt: increases the shooting capability of the ship by firing 2 to 3 bullets instead of one at time.
- Custom sounds and sprite animation for things like
  - meteorite explosion
  - bullet shoots
  - player explosion
- 3 lives per game
- Fun to play :)

## Controls

|              | Button              |
|--------------|---------------------|
| Move Left    | <kbd>left</kbd>     |
| Move right   | <kbd>right</kbd>    |
| Fire bullets | <kbd>spacebar</kbd> |
| Quit game    | <kbd>Esc</kbd>      |

## Installation

### For `Windows`

- Download the prebuilt `zip file` [from here](https://github.com/prodicus/spaceShooter/releases/download/v0.0.2/spaceShooter-v0.0.2_windows.zip) and extract the file to your preferred destination by using [7-zip](http://www.7-zip.org/download.html) or [winzip](http://www.winzip.com/prod_down.html) or any other similar program of your choice.
- Run the executable named `spaceShooter` inside the extracted file.

### For `MAC OS X` 

You have to build from source to get it up and running on `OS X`. Reason?
I don't have an `OS X` system to build the executable! So I would love for a Pull request on that one.

[Building from source will do the trick though](https://github.com/prodicus/spaceShooter#os-x)


```bash
$ pip3 install hg+http://bitbucket.org/pygame/pygame
```

Install Pygame specific dependencies

```bash
$ brew install sdl sdl_image sdl_ttf portmidi libogg libvorbis
$ brew install sdl_mixer --with-libvorbis
```

##### Clone the repo

```bash
$ git clone https://github.com/prodicus/spaceShooter.git
$ cd spaceShooter/ 
$ python spaceShooter.py
```

### `Linux/Debian` based systems

#### Option 1: Download the zipped executable file

- Download the [latest zip file](https://github.com/prodicus/spaceShooter/releases/download/v0.0.2/spaceShooter-v0.0.2_linux.zip)
- Unzip the file

If your download was saved on the `~/Downloads` folder

Press <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> to open the shell if you are on `GNU/Linux` based systems and type

```bash
$ unzip ~/Downloads/SpaceShooter-0.0.1.Linux.zip -d ~/Desktop
$ cd ~/Desktop
$ ## navigate to the unzipped file and change the file permissions for the executable
~/Desktop $ chmod +x spaceShooter
~/Desktop $ ./spaceShooter
```

This will unzip the file on your `Desktop`, you can replace it with the directory of your choice

**NOTE** : If it gives you an error, you probably don't have `unzip` installed in your system.

```bash
$ sudo apt-get install unzip
```
That should fix the error.

- Run the executable named `spaceShooter`

A Similar process would be followed for `OS X`

#### Option 2: Build from source

You need to have `pygame` installed for this option. 

##### Ubuntu/Debian

```bash
$ sudo apt-get install python-pygame
```

##### Clone the repo

```bash
$ git clone https://github.com/prodicus/spaceShooter.git
$ cd spaceShooter/ 
$ python spaceShooter.py
```

Enjoy the game!

## Known issues

- The game music doesn't play on `OS X` as described in [#1](https://github.com/prodicus/spaceShooter/issues/1)

## Contributers:

- [@bardlean86](https://github.com/bardlean86/) for adding the third missile powerup and the main menu

## To-do:

- [x] Add the `windows` executable file
- [ ] Add `OS X` executable file as the `Debian` based one fails to execute on it
- [x] Add main menu for the game
- [x] Fix [bug](https://github.com/prodicus/spaceShooter/blob/master/spaceShooter.py#L372) which stops the background music from looping 
- [ ] Add support for `WAV` game music file as `ogg` format is not playable as described in [#1](https://github.com/prodicus/spaceShooter/issues/1)
- [ ] add feature to replay the game after all players die

## Contributing

This game was written in one day, so the coding standards might not be up the mark. Don't be shy to make a Pull request :)

For details, please refer [the Contributing page](https://github.com/prodicus/spaceShooter/blob/master/CONTRIBUTING.rst)

## Issues

You can report the bugs at the [issue tracker](https://github.com/prodicus/spaceShooter/issues)

**OR**

You can [tweet me](https://twitter.com/tasdikrahman) if you can't get it to work. In fact, you should tweet me anyway.

## Similar

- [Bullethell.py ](https://github.com/Frederikxyz/bullethell.py) : A fork of [prodicus/spaceShooter](https://github.com/prodicus/spaceShooter) which adds fancy shooting capabilities

## License

[MIT License](http://prodicus.mit-license.org) © [Tasdik Rahman](http://tasdikrahman.me)

You can find a copy of the License at http://prodicus.mit-license.org/

- The images used in the game are taken from [http://opengameart.org/](http://opengameart.org/), more particulary from the [Space shooter content pack](http://opengameart.org/content/space-shooter-redux) from [@kenney](http://opengameart.org/users/kenney).

License for them is in `Public Domain`

- The game sounds were again taken from [http://opengameart.org/](http://opengameart.org/). The game music, [Frozen Jam](http://opengameart.org/content/frozen-jam-seamless-loop) by [tgfcoder](https://twitter.com/tgfcoder) licensed under [CC-BY-3](http://creativecommons.org/licenses/by/3.0/)
