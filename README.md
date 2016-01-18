## Space Shooter

The classic retro game recreated using `Pygame` and `python`.

## Demo

Follow the youtube video to see how I fared on ``spaceShooter``

[![Space Shooter Demo - Youtube](http://i.imgur.com/bHjlJfG.jpg)](https://www.youtube.com/watch?v=o99zpLsM-ZI)

## Screenshots

| ![Screen 1](http://i.imgur.com/I5mTBFB.png) | ![Screen 2](http://i.imgur.com/4OgIByR.png) |
|---------------------------------------------|---------------------------------------------|

## Game Features

- Health bar for the space ship
- Score board to show how you are faring so far
- Power ups like
  - shield: increases the space ships life
  - bolt: increases the shooting capability of the ship by firing 2 bullets instead of one at time.
- Custom sounds and sprite animation for things like
  - meteorite explosion
  - bullet shoots
  - player explosion
- 3 lives per game
- Fun to play :)

## Controls

- To move the spaceship 
  - To left : <kbd>left</kbd>
  - to right : <kbd>right</kbd>
- To fire the bullets : <kbd>spacebar</kbd>

## Installation

### For `Windows`

- Download the prebuilt `zip file` [from here](https://github.com/prodicus/spaceShooter/releases/download/v0.0.1/spaceShooter-0.0.1-windows.zip) and extract the file to your preferred destination by using [7-zip](http://www.7-zip.org/download.html) or [winzip](http://www.winzip.com/prod_down.html) or any other similar program of your choice.
- Run the executable named `spaceShooter` inside the extracted file.

### For `MAC OS X` and `Linux/Debian` based systems

#### Option 1: Download the zipped executable file

- Download the [latest zip file](https://github.com/prodicus/spaceShooter/releases/download/v0.0.1/SpaceShooter-0.0.1.Linux.zip)
- Unzip the file

If your download was saved on the `~/Downloads` folder

Press <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> to open the shell if you are on `GNU/Linux` based systems and type

```bash
$ unzip SpaceShooter-0.0.1.Linux.zip -d ~/Desktop
$ cd ~/Desktop
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

Enjoy the game!

## To-do:

- [x] Add the windows executable file
- [ ] Add main menu for the game
- [ ] Fix [bug](https://github.com/prodicus/spaceShooter/blob/master/spaceShooter.py#L372) which stops the background music from looping 
- [ ] add feature to replay the game after all players die

## Contributing

This game was written in one day, so the coding standards might not be up the mark. Don't be shy to make a Pull request :)

For details, please refer [the Contributing page](https://github.com/prodicus/spaceShooter/blob/master/CONTRIBUTING.rst)

## Issues

You can report the bugs at the [issue tracker](https://github.com/prodicus/spaceShooter/issues)

## License

[MIT License](http://prodicus.mit-license.org) © [Tasdik Rahman](http://tasdikrahman.me)

You can find a copy of the License at http://prodicus.mit-license.org/

- The images used in the game are taken from [http://opengameart.org/](http://opengameart.org/), more particulary from the [Space shooter content pack](http://opengameart.org/content/space-shooter-redux) from [@kenney](http://opengameart.org/users/kenney).

License for them is in `Public Domain`

- The game sounds were again taken from [http://opengameart.org/](http://opengameart.org/). The game music, [Frozen Jam](http://opengameart.org/content/frozen-jam-seamless-loop) by [tgfcoder](https://twitter.com/tgfcoder) licensed under [CC-BY-3](http://creativecommons.org/licenses/by/3.0/)
