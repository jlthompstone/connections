# connections
Recreate the New York Times "Connections" game.

## Minimum Viable Product

- **Player Story 1:** Ability to click 4 squares, press submit and find out if I'm right or wrong.
- **Player Story 2:** Ability to tell which difficulty (1-4) a correct selection of squares is based on colour (yellow is 1, green is 2, blue is 3 and purple is 4)
- **Player Story 3:** Have 4 lives and lose if they run out.
- **Player Story 4:** Subtract a life if a selection is wrong and deselect options.

## Stack

| Layer | Technology |
| --- | --- |
| Frontend | Python |
| Backend | Python |
| Database | MySQL |

## Development Plan

- [x] **Phase 1: Database Setup**
    - [x] Create JSON database, initialise tables for puzzles, groups and words
    - [x] Sample puzzle stored in database
    - [x] Python link to retrieve data for a particular puzzle  from the database

- [ ] **Phase 2: Game UI & Selection [Player Story 1]**
    - [ ] Display a 4x4 grid of the words in a puzzle randomised
    - [ ] Allow select/deselect of up to 4 words
    - [ ] Submit button & check if selection is correct

- [ ] **Phase 3: Game State [Player Story 3 & 4]**
    - [ ] User has 4 lives
    - [ ] If a selection is submitted and incorrect, subtract a life
    - [ ] If no lives left, game over
    - [ ] If all four categories are sorted, player wins

- [ ] **Phase 4: Styles & Extras**
    - [ ] Colours for difficulty in sorted groups
    - [ ] Shuffle button
    - [ ] Deselect all button
