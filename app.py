from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Story dictionary
story = {
    "start": {
        "text": "You wake up in a dark forest. Three paths lie ahead.",
        "choices": {
            "Take the left path": "wolf",
            "Take the right path": "river",
            "Climb a tree": "treehouse"
        }
    },
    "wolf": {
        "text": "You encounter a hungry wolf! What do you do?",
        "choices": {
            "Fight the wolf": "fight",
            "Offer it your sandwich": "friend_wolf",
            "Run away": "start"
        }
    },
    "fight": {
        "text": "You bravely fight the wolf and win! You see a treasure chest.",
        "choices": {
            "Open the chest": "chest",
            "Leave it": "cave"
        }
    },
    "friend_wolf": {
        "text": "The wolf loves your sandwich and becomes your companion!",
        "choices": {
            "Take wolf with you": "wolf_joins",
            "Say goodbye": "start"
        }
    },
    "wolf_joins": {
        "text": "With your new wolf friend, you explore deeper and find a wizard's hut.",
        "choices": {
            "Enter the hut": "wizard",
            "Walk past it": "trap"
        }
    },
    "wizard": {
        "text": "The wizard challenges you to a rap battle!",
        "choices": {
            "Accept the battle": "win_rap",
            "Decline politely": "teleported"
        }
    },
    "win_rap": {
        "text": "You drop hot bars! The wizard gives you a glowing gem.",
        "choices": {
            "Take gem and continue": "cave",
            "Refuse and leave": "village"
        }
    },
    "teleported": {
        "text": "The wizard respects your humility and teleports you to a peaceful village. You win!",
        "choices": {}
    },
    "trap": {
        "text": "You fall into a trap and get stuck. Game Over.",
        "choices": {}
    },
    "chest": {
        "text": "Inside the chest, you find a healing potion and a map.",
        "choices": {
            "Take the map": "cave",
            "Take the potion": "village"
        }
    },
    "cave": {
        "text": "You enter a mysterious cave. It's dark. Light a torch?",
        "choices": {
            "Yes": "dragon",
            "No": "fall"
        }
    },
    "fall": {
        "text": "You stumble in the dark and fall. Game Over.",
        "choices": {}
    },
    "dragon": {
        "text": "You find a sleeping dragon. Steal treasure or sneak out?",
        "choices": {
            "Steal": "burned",
            "Sneak": "village"
        }
    },
    "burned": {
        "text": "The dragon wakes up and burns you. Game Over.",
        "choices": {}
    },
    "village": {
        "text": "You reach a peaceful village. You win!",
        "choices": {}
    },
    "river": {
        "text": "You reach a wild river. Try to swim or build a raft?",
        "choices": {
            "Swim": "drowned",
            "Build a raft": "raft"
        }
    },
    "drowned": {
        "text": "The river sweeps you away. Game Over.",
        "choices": {}
    },
    "raft": {
        "text": "You successfully build a raft, but a banana-shaped alien lands next to you.",
        "choices": {
            "Invite alien aboard": "alien_party",
            "Ignore alien": "village"
        }
    },
    "alien_party": {
        "text": "The alien throws a surprise party on the raft! You dance into the sunset. You win!",
        "choices": {}
    },
    "treehouse": {
        "text": "You climb a tree and discover a hidden treehouse full of squirrels playing chess.",
        "choices": {
            "Join their game": "squirrel_game",
            "Climb back down": "start"
        }
    },
    "squirrel_game": {
        "text": "The squirrels teach you their secrets. You gain +100 wisdom!",
        "choices": {
            "Use wisdom to find the best path": "village",
            "Write a book about them": "famous_author"
        }
    },
    "famous_author": {
        "text": "Your book about squirrel chess becomes a bestseller. You win... intellectually!",
        "choices": {}
    }
}


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/story', methods=['POST'])
def get_story():
    current_node = request.json.get('node', 'start')
    node = story.get(current_node, {})
    return jsonify(node)

if __name__ == '__main__':
    app.run(debug=True)
