### Updates

**29 October 2024**
* Replaced flite with gTTS (a bit slow tho)
* added multilingual support (check config.json) [only works in gTTS]

**27 October 2024**
- Added a new configuration file you might wanna check out??
- Added music modules and controls through vlc (tested)

### TODOs

- [ ] Set flite as fallback and gTTS when online
- [ ] Do something with all the spotify I cooked
- [-] Check out if gTTS works better than flite
- [ ] Finetune Gemini through AI Studio (Personal)
- [ ] Start a Documentation (mkdocs??) for the Configuration
- [ ] Make Friday do it's own Pushing (I am too lazy)

### Setting Up for Dev

Install following in GNU/Linux:

```bash
flite vlc
```

Setup [Poetry](https://python-poetry.org/docs/), Clone Project and Do:

```bash
poetry install
poetry run ash
```
