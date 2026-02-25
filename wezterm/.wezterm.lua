-- Pull in the wezterm API
local wezterm = require 'wezterm'

-- This will hold the configuration.
local config = wezterm.config_builder()

-- This is where you actually apply your config choices.

-- For example, changing the initial geometry for new windows:
config.initial_cols = 120
config.initial_rows = 40

-- set opacity
config.window_background_opacity = 0.4
config.text_background_opacity = 0.7

-- or, changing the font size and color scheme.
config.font_size = 14
-- config.color_scheme = 'AdventureTime'
config.color_scheme = 'Dark+'
config.font = wezterm.font {
    family = 'Sarasa Term SC',
    harfbuzz_features = { 'calt=1', 'clig=1', 'liga=1' },
}
config.freetype_load_target = 'Normal'

-- Finally, return the configuration to wezterm:
return config
