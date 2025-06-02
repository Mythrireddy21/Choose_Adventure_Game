# Choose Your Own Adventure Game

An interactive adventure game where players navigate a branching story by making choices at each step.
Each decision leads to different story paths and multiple possible endings, creating a unique experience every time.

## Features

- Dynamic story progression with multiple branches and endings  
- Simple and clean UI for immersive storytelling  
- Choices update the story in real-time using Flask API  
- Easy to extend the story by editing the backend `story` dictionary  
- Runs locally in your browser with Flask backend

## Project Structure

```
Choose-Adventure-Game/
│
├── app.py                  # Flask backend with story logic
├── templates/
│   └── index.html          # Frontend HTML game UI
├── static/
│   └── style.css           # CSS styles for UI
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/Mythrireddy21/Choose_Adventure_Game.git
cd Choose_Adventure_Game
````

2. **Create a virtual environment (optional but recommended)**

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Flask app**

```bash
python app.py
```

5. **Open your browser**

Go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to start playing!

---


## How to Play

1. The story text appears on the screen.
2. Choose from the available options by clicking buttons.
3. Your choice leads you to a new story scene.
4. Explore different choices to unlock all story endings!

## How to Extend the Story

The story data is stored in the `story` dictionary inside `app.py`.

* Each key is a scene ID.
* Each scene contains:

  * `text`: narrative description
  * `choices`: dictionary of choice text → next scene ID

To add new scenes, just add new entries like this:

```python
"new_scene": {
    "text": "You find a mysterious door. What do you do?",
    "choices": {
        "Open the door": "treasure_room",
        "Walk away": "forest"
    }
}
```

## Dependencies

* Python 3.7 or higher
* Flask (installed via `requirements.txt`)


## Customization

* Change the CSS in `static/style.css` to update the look and feel.
* Modify `index.html` to adjust frontend layout and design.
* Add more scenes and choices in `app.py` to expand the story.

## License

This project is licensed under the MIT License.


Have fun exploring your story world! 🌲✨

