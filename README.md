# Rocknix RG ARC RK3566 Yabadabadoo Compatibility List
A compatibility list for the Sega Saturn libretro core **Yabadabadoo** (a fork of Yabuse) as tested on an **Anbernic RG Arc D**. 

Most of these games have only been tested briefly. If you encounter any problems that haven't been mentioned then report an issue and I'll update the list. I'd be particularly grateful if anyone can report full playthroughs of longer games.

**Settings:** 
- LVL3 undervolt was enabled along with overclocking in Rocknix system settings.
- Disable V-Sync, you don't get any tearing without it.
- I use the GL video driver with Threaded Video disabled for input latency reasons.
- Threaded video crashes RetroArch under GL with this core so when I needed extra performance I switched to Vulkan to enable it.
- Max Swapchain Images was set to 2 to reduce input latency. You can increase it if you're getting the occasional stutter.

<!-- COMPATIBILITY_TABLE_START -->

| Game Name | Region | Playable | Glitches/Notes |
| --- | --- | --- | --- |
| Astal | NTSC | ❌ | Black screen freeze. |
| Albert Odyssey | NTSC | ❌ | A flicker of glitched tiles appear when text boxes close. When you enter menu it fades in twice instead of once. |
| Alien Trilogy | NTSC | ✅ | Mission brief text displays incorrectly. The first letter of each word flickers and then turns invisible when loading has completed. |
| Alone in the Dark One Eyed Jack’s Revenge | NTSC | ❌ | Intro doesn’t animate, only a couple of frames are shown. You can pause and enter inventory which works but in-game you just see that frozen frame from the intro while music plays. |
| Amok | NTSC-J | ✅ |  |
| Astra Superstars | NTSC-J | ❌ | Background graphics are badly glitched. |
| Batman Forever the Arcade Game | NTSC-J | ❌ | Slow-motion gameplay (not fps drop). |
| Batsugun | NTSC-J | ❌ | Inputs are massively delayed and/or dropped completely. |
| Battle Arena Toshinden Remix | NTSC | ✅ | Use Vulkan and enable threaded video for full-speed. |
| Battle Garegga | NTSC-J | ❌ | Inputs are massively delayed and/or dropped completely. |
| Blast Wind | NTSC-J | ✅ | Runs at 30fps instead of 60fps unless VDP1 Draw Timing is set to ‘Every Frame’ |
| Bubble Symphony | NTSC-J | ✅ |  |
| Bug | NTSC | ❌ | Freezes at Sega Away Team logo. PAL also. |
| Bug Too | NTSC | ✅ |  |
| Bulk Slash | NTSC-J | ✅ |  |
| Burning Rangers | NTSC | ❌ | Poor performance and audio is sometimes too quiet. |
| Bust-a-Move 3 | NTSC | ✅ |  |
| Chou Aniki | NTSC-J | ❌ | No sound effects. |
| Clockwork Knight | NTSC | ✅ |  |
| Clockwork Knight 2 | PAL | ✅ | Main menu displays incorrectly. Menu items that should be obscured by the logo display in front of it and vice versa. |
| Contra Legacy of War | NTSC | ❌ | Player character warps around the gameplay area randomly. |
| Cyberbots: Fullmetal Madness | NTSC-J | ❌ | Black screen freeze. |
| D&D Collection | NTSC-J | ❌ | Sprite corruption glitch similar to Rockman X3 (also Capcom) |
| Darius Gaiden | NTSC | ❌ | No sound effects. |
| Darius II | NTSC-J | ❌ | No sound effects. |
| Dark Savior | NTSC | ❌ | Sound doesn’t work on start menu until you exit the sound test. Crashes RA when selecting new game. |
| Daytona USA C.C.E Netlink | NTSC | ✅ |  |
| Die Hard Arcade | NTSC | ❌ | Set frameskip to an interval of 1 to fix performance and bad glitches. Some sound issues still remain such as missing music/quiet sound effects. |
| DoDonPachi | NTSC-J | ❌ | Movement, background graphics, enemies all broken. |
| DonPachi | NTSC-J | ❌ | Crashes before gameplay begins. |
| Earthworm Jim 2 | NTSC | ✅ |  |
| Elevator Action Returns | NTSC-J | ✅ | Minor glitch with the fade-in effect during the opening Ving logo and when each mission title is displayed. |
| Exhumed | PAL | ✅ | Loading screen top 3rd of screen glitchy. |
| Fighters Megamix | PAL | ❌ | Works unlike NTSC (black screen freeze) but poor performance. |
| Fighting Vipers | PAL | ❌ | Works unlike NTSC (black screen freeze) but poor performance. |
| Final Fight Revenge | NTSC-J | ✅ |  |
| Galactic Attack | NTSC | ✅ |  |
| Galaxy Fight | NTSC-J | ❌ | No sound. Selecting an option from the main menu reboots to Sega licensing screen and then the bios music player. |
| Gex | NTSC | ❌ | Ground/wall tiles constantly flicker between correct and glitched when the game is scrolling. |
| Golden Axe: The Duel | NTSC | ✅ |  |
| Guardian Force | NTSC | ❌ | Explosion sound effects are much too loud. |
| Guardian Heroes | NTSC | ✅ |  |
| Gunbird | NTSC-J | ❌ | Movement, background graphics, enemies all broken. |
| Herc’s Adventures | NTSC | ❌ | Boots straight to bios music player. |
| House of the Dead, The | NTSC | ✅ | Use Vulkan and enable threaded video for full-speed. |
| In the Hunt | PAL | ❌ | Black screen freeze before first FMV. NTSC-J version plays the FMV then black screen freeze. |
| Keio Flying Squadron 2 | PAL | ✅ |  |
| King of Fighters 97, The | NTSC | ✅ |  |
| Kingdom Grand Prix | NTSC-J | ✅ |  |
| Last Bronx | NTSC | ❌ | Very slow and there are all-black copies of the fighters in the air. |
| Layer Section 2 | NTSC-J | ✅ | Visual glitch shown outside the borders of the game screen. |
| Legend of Oasis, The | NTSC | ✅ |  |
| Loaded | NTSC | ✅ | Pausing makes graphical glitches appear. |
| Magical Night Dreams: Cotton 2 | NTSC-J | ✅ |  |
| Magical Night Dreams: Cotton Boomerang | NTSC-J | ✅ | Main menu runs in high-res mode so use auto frameskip to avoid stuttering music. In-game is full-speed without frameskip. |
| Manx TT SuperBike | NTSC | ❌ | Full-speed in 3rd person but camera “skips” upwards frequently. 1st person needs Vulkan/Threaded Video/Frameskip for full-speed. |
| Marvel Super Heroes | NTSC | ✅ |  |
| Megaman 8 | NTSC | ✅ |  |
| Megaman X4 | NTSC | ✅ |  |
| Mortal Kombat Trilogy | NTSC | ❌ | Opening crawl text is glitched and then it transitions to a black screen while music plays. |
| Need for Speed | NTSC | ❌ | Loading screen’s colours are wrong. Steering wheel invisible. Skybox glitched. |
| Nekketsu Oyako | NTSC-J | ❌ | Black screen freeze. |
| Night Warriors Darkstalker’s Revenge | NTSC | ❌ | Black screen freeze. |
| NiGHTS into Dreams | NTSC | ✅ |  |
| Ninpen Manmaru | NTSC-J | ❌ | Every screen transition takes an eternity. You’ll think the game has frozen but it will eventually load and gameplay seems fine. |
| Pandemonium | NTSC | ❌ | Slow-motion gameplay (not fps drop). |
| Panzer Dragoon | NTSC | ✅ | Use Vulkan and enable threaded video for full-speed. |
| Panzer Dragoon Zwei | NTSC | ❌ | Occasionally the ground texture briefly glitches and a grid of brightly coloured squares appear briefly at the start of missions. |
| Pocket Fighter | NTSC-J | ✅ |  |
| Policenauts | NTSC-J | ✅ | [T-En by JunkerHQ v1.0.1] |
| Princess Kurara | NTSC-J | ✅ |  |
| Quake | NTSC | ✅ | Loading screen top 3rd of screen glitchy. |
| Radiant Silvergun | NTSC-J | ✅ |  |
| Rayman | NTSC | ❌ | Background graphics glitches. Part of the shattering image effect before 1st mission is missing. |
| Real Bout Garou Densetsu | NTSC-J | ❌ | Colours and transparency of sprites are completely wrong. |
| Road Rash | NTSC | ❌ | Road markings are glitched. |
| Rockman X3 | NTSC-J | ❌ | Sprite corruption glitch similar to D&D Collection (also Capcom) |
| Saturn Bomberman | NTSC | ✅ |  |
| Sega Ages – Galaxy Force II | NTSC | ✅ | Use Vulkan and enable threaded video for full-speed. |
| Sega Rally Championship | NTSC | ✅ |  |
| Shinobi Legions | NTSC | ✅ |  |
| Shinrei Jusatsushi Taroumaru | NTSC-J | ✅ |  |
| Sonic 3D Blast | NTSC | ✅ | No video during opening FMV |
| Sonic Jam – Original Games | NTSC | ❌ | Menu is squished into top half of screen. Games run in slow motion with full-speed music. |
| Sonic Jam – Sonic World | NTSC | ✅ | Use Vulkan and enable threaded video for full-speed. |
| Sonic R | NTSC | ✅ | Use Vulkan and enable threaded video for full-speed. |
| Sonic Wings Special | NTSC-J | ❌ | Slow-motion gameplay (not fps drop). |
| Soukyuu Gurentai (Terra Driver) | NTSC-J | ✅ |  |
| Street Fighter Zero 3 | NTSC-J | ✅ | Sometimes the intro has no sound. |
| Street Fighter: The Movie | NTSC | ✅ |  |
| Super Puzzle Fighter 2 Turbo | NTSC | ✅ |  |
| Super Tempo | NTSC-J | ❌ | Black screen freeze. |
| Swagman | PAL | ❌ | Black screen freeze at 50hz. In-game graphics are completely broken at 60hz. |
| Thunder Force V | NTSC-J | ✅ | Use Vulkan and enable threaded video for full-speed. |
| Twinkle Star Sprites | NTSC-J | ✅ |  |
| Vampire Savior | NTSC-J | ❌ | Black screen freeze. |
| Virtua Cop | NTSC | ✅ | Sound effects are too quiet and can barely be heard over music. |
| Virtua Cop 2 | NTSC | ✅ | Sound effects are too quiet and can barely be heard over music. |
| Virtua Fighter | NTSC | ❌ | Slow sometimes even with Vulkan/threaded video/frameskip. Fighters sometimes get knocked back really far, really fast resulting in ring out. |
| Virtua Fighter 2 | NTSC | ❌ | Announcer voice broken. Use Vulkan and enable threaded video and frameskip for full-speed. Frameskip breaks menus. |
| Virtua Fighter Remix  | NTSC | ❌ | Slow sometimes even with Vulkan/threaded video/frameskip. |
| WarCraft 2 | NTSC | ✅ |  |
| X-Men Children of the Atom | NTSC | ❌ | Returns to bios music player after Capcom logo. |
| X-Men vs. Street Fighter | NTSC | ❌ | Black screen freeze. |
| Z | PAL | ✅ |  |

<!-- COMPATIBILITY_TABLE_END -->
