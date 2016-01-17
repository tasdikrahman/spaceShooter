## Space Shooter

The classic retro game recreated using `Pygame` and `python`

## Demo

[![Space Shooter Demo - Youtube](http://i.imgur.com/bHjlJfG.jpg)](https://www.youtube.com/watch?v=o99zpLsM-ZI)

## Screenshots

| ![Screen 1](http://i.imgur.com/I5mTBFB.png) | ![Screen 2](http://i.imgur.com/4OgIByR.png) |
|---------------------------------------------|---------------------------------------------|

## Installation

### For `Windows`

- Download the prebuilt `zip file` [from here](https://github.com/prodicus/spaceShooter/releases/download/v0.0.1/windows_exe.zip)
- Unzip it and run the executable named `spaceShooter`

### For `MAC OS X` and `Linux/Debian` based systems

#### Option 1: Download the Executable file

Download the [latest Executable file](https://github.com/prodicus/vocabulary/releases/latest) 

#### Option 2: Run the source

You need to have `pygame` installed for this option

##### Ubuntu/Debian

```bash
$ sudo apt-get install python-pygame
```

##### OS X

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

Enjoy the game :smile:

## To-do:

- [x] Add the windows executable file
- [ ] Add main menu for the game
- [ ] Fix bug which stops the background music from looping 

## Contributing

Please refer [Contributing page for details](https://github.com/prodicus/spaceShooter/blob/master/CONTRIBUTING.rst)

## Issues

Please report the bugs at the [issue tracker](https://github.com/prodicus/spaceShooter/issues)

## License

[MIT License](http://prodicus.mit-license.org) © [Tasdik Rahman](http://tasdikrahman.me)

You can find a copy of the License at http://prodicus.mit-license.org/

The images used in the game are taken from [http://opengameart.org/](http://opengameart.org/), more particulary from the [Space shooter content pack](http://opengameart.org/content/space-shooter-redux) from [@kenney](http://opengameart.org/users/kenney).

License for them is in `Public Domain`

The game sounds were again taken from [http://opengameart.org/](http://opengameart.org/)

- The game music, [Frozen Jam](http://opengameart.org/content/frozen-jam-seamless-loop) by [tgfcoder](https://twitter.com/tgfcoder) licensed under [CC-BY-3](http://creativecommons.org/licenses/by/3.0/)
