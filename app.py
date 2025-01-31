from flask import Flask, render_template, request

app = Flask(__name__)

dream_keywords = {
    "falling": "A sign of insecurity, loss of control, or anxiety.",
    "flying": "Represents a sense of freedom, success, or escaping limitations.",
    "chased": "You might be avoiding something important in life.",
    "teeth": "Could symbolize stress, fear of aging, or loss of confidence.",
    "water": "Symbolizes emotions—calm water means peace, stormy water means turmoil.",
    "lost": "Feeling directionless in life or uncertain about a decision.",
    "death": "Not literal, but often means transformation or major life changes.",
    "naked": "Feeling exposed, vulnerable, or judged in a situation.",
    "money": "Represents self-worth, success, or financial concerns.",
    "snake": "Symbolizes transformation, fear, or hidden threats.",
    "spider": "Could indicate feeling trapped or entangled in a situation.",
    "house": "Represents the self—different rooms symbolize different aspects of your life.",
    "car": "Symbolizes your life's direction or how you navigate challenges.",
    "fire": "Represents passion, destruction, or transformation.",
    "rain": "Symbolizes cleansing, renewal, or emotional release.",
    "mirror": "Reflects self-awareness, identity, or how you see yourself.",
    "baby": "Represents new beginnings, innocence, or vulnerability.",
    "wedding": "Symbolizes commitment, union, or a new phase in life.",
    "school": "Indicates learning, self-evaluation, or unresolved issues from the past.",
    "train": "Represents life's journey, direction, or missed opportunities.",
    "bridge": "Symbolizes transitions, decisions, or overcoming obstacles.",
    "cat": "Represents independence, mystery, or feminine energy.",
    "dog": "Symbolizes loyalty, protection, or companionship.",
    "tree": "Represents growth, stability, or connection to your roots.",
    "storm": "Indicates emotional turmoil, conflict, or upheaval.",
    "sun": "Symbolizes clarity, energy, or positivity.",
    "moon": "Represents intuition, emotions, or the subconscious mind.",
    "stars": "Symbolize hope, guidance, or aspirations.",
    "ocean": "Represents the vastness of emotions or the unconscious mind.",
    "mountain": "Symbolizes challenges, goals, or obstacles to overcome.",
    "desert": "Indicates feelings of isolation, emptiness, or a need for renewal.",
    "forest": "Represents mystery, exploration, or the unknown.",
    "cave": "Symbolizes introspection, fear, or hidden aspects of the self.",
    "key": "Represents solutions, opportunities, or unlocking potential.",
    "door": "Symbolizes new opportunities, transitions, or choices.",
    "window": "Represents perspective, insight, or a view into the future.",
    "clock": "Indicates time pressure, urgency, or the passage of time.",
    "book": "Symbolizes knowledge, wisdom, or untapped potential.",
    "road": "Represents your life's path, journey, or direction.",
    "airplane": "Symbolizes ambition, freedom, or a desire to rise above challenges.",
    "ship": "Represents emotional journeys, stability, or navigating life's changes.",
    "island": "Indicates feelings of isolation, self-sufficiency, or retreat.",
    "bridge": "Symbolizes transitions, decisions, or overcoming obstacles.",
    "ladder": "Represents progress, ambition, or spiritual growth.",
    "cage": "Symbolizes feeling trapped, restricted, or confined.",
    "butterfly": "Represents transformation, growth, or a new phase in life.",
    "lion": "Symbolizes courage, strength, or leadership.",
    "horse": "Represents freedom, power, or a desire to move forward.",
    "bird": "Symbolizes freedom, perspective, or spiritual aspirations.",
    "fish": "Represents abundance, intuition, or emotional depth.",
    "crow": "Symbolizes mystery, transformation, or a message from the subconscious.",
    "egg": "Represents potential, new beginnings, or creativity.",
    "flower": "Symbolizes beauty, growth, or the blossoming of ideas.",
    "shadow": "Represents hidden fears, insecurities, or the unknown.",
    "light": "Symbolizes clarity, enlightenment, or hope.",
    "darkness": "Indicates fear, confusion, or the unknown.",
    "garden": "Represents growth, nurturing, or the cultivation of ideas.",
    "river": "Symbolizes the flow of life, emotions, or time.",
    "fog": "Indicates confusion, uncertainty, or a lack of clarity.",
    "earthquake": "Represents upheaval, instability, or major life changes.",
    "volcano": "Symbolizes repressed emotions, anger, or explosive energy.",
    "tornado": "Indicates chaos, emotional turmoil, or overwhelming situations.",
    "rainbow": "Represents hope, promise, or a bridge between the conscious and subconscious.",
    "crown": "Symbolizes authority, success, or self-empowerment.",
    "sword": "Represents conflict, power, or the need to cut through obstacles.",
    "shield": "Symbolizes protection, defense, or resilience.",
    "chain": "Represents restriction, bondage, or feeling tied down.",
    "ring": "Symbolizes commitment, unity, or cycles in life.",
    "cross": "Represents sacrifice, faith, or a burden to bear.",
    "angel": "Symbolizes guidance, protection, or divine intervention.",
    "demon": "Represents inner fears, guilt, or negative influences.",
    "ghost": "Indicates unresolved issues, past trauma, or lingering emotions.",
    "vampire": "Symbolizes energy drain, fear, or a need for boundaries.",
    "dragon": "Represents power, fear, or untamed emotions.",
    "unicorn": "Symbolizes magic, purity, or the pursuit of the impossible.",
    "castle": "Represents ambition, security, or a fortress of emotions.",
    "tower": "Symbolizes isolation, ambition, or a need for perspective.",
    "labyrinth": "Indicates confusion, complexity, or a search for meaning.",
    "mask": "Represents hiding one's true self, deception, or social roles.",
    "mirror": "Reflects self-awareness, identity, or how you see yourself.",
    "candle": "Symbolizes hope, guidance, or the light within.",
    "lantern": "Represents illumination, clarity, or finding your way.",
    "bell": "Indicates a wake-up call, alertness, or a message.",
    "anchor": "Symbolizes stability, security, or feeling grounded.",
    "shipwreck": "Represents failure, loss, or emotional devastation.",
    "treasure": "Symbolizes hidden potential, wealth, or self-discovery.",
    "map": "Represents guidance, direction, or a plan for the future.",
    "compass": "Symbolizes finding your way, clarity, or purpose.",
    "flag": "Represents identity, pride, or a sense of belonging.",
    "tent": "Indicates temporary situations, adaptability, or simplicity.",
    "cave": "Symbolizes introspection, fear, or hidden aspects of the self.",
    "crystal": "Represents clarity, healing, or spiritual energy.",
    "mirror": "Reflects self-awareness, identity, or how you see yourself.",
    "ladder": "Represents progress, ambition, or spiritual growth.",
    "chain": "Represents restriction, bondage, or feeling tied down.",
    "ring": "Symbolizes commitment, unity, or cycles in life.",
    "cross": "Represents sacrifice, faith, or a burden to bear.",
    "angel": "Symbolizes guidance, protection, or divine intervention.",
    "demon": "Represents inner fears, guilt, or negative influences.",
    "ghost": "Indicates unresolved issues, past trauma, or lingering emotions.",
    "vampire": "Symbolizes energy drain, fear, or a need for boundaries.",
    "dragon": "Represents power, fear, or untamed emotions.",
    "unicorn": "Symbolizes magic, purity, or the pursuit of the impossible.",
    "castle": "Represents ambition, security, or a fortress of emotions.",
    "tower": "Symbolizes isolation, ambition, or a need for perspective.",
    "labyrinth": "Indicates confusion, complexity, or a search for meaning.",
    "mask": "Represents hiding one's true self, deception, or social roles.",
    "mirror": "Reflects self-awareness, identity, or how you see yourself.",
    "candle": "Symbolizes hope, guidance, or the light within.",
    "lantern": "Represents illumination, clarity, or finding your way.",
    "bell": "Indicates a wake-up call, alertness, or a message.",
    "anchor": "Symbolizes stability, security, or feeling grounded.",
    "shipwreck": "Represents failure, loss, or emotional devastation.",
    "treasure": "Symbolizes hidden potential, wealth, or self-discovery.",
    "map": "Represents guidance, direction, or a plan for the future.",
    "compass": "Symbolizes finding your way, clarity, or purpose.",
    "flag": "Represents identity, pride, or a sense of belonging.",
    "tent": "Indicates temporary situations, adaptability, or simplicity.",
    "cave": "Symbolizes introspection, fear, or hidden aspects of the self.",
    "crystal": "Represents clarity, healing, or spiritual energy."
}
def analyze_dream(dream):
    analysis = []
    for key, meaning in dream_keywords.items():
        if key in dream.lower():
            analysis.append(f"The symbol '{key}' in your dream suggests: {meaning}")
    if not analysis:
        analysis.append("No interpretation found. Try describing your dream differently.")
    return analysis

def create_story(words):
    story = (
        f"Once upon a time, in a land filled with {words[0]} and {words[1]}, there lived a brave adventurer named {words[2]}. "
        f"One day, {words[2]} stumbled upon a mysterious {words[3]} hidden deep within the {words[4]}. "
        f"Curiosity got the better of them, and they decided to explore it. Inside, they found a glowing {words[5]} that seemed to radiate {words[6]}. "
        f"As they reached out to touch it, the ground began to shake, and a loud {words[7]} echoed through the air. "
        f"Suddenly, a {words[8]} appeared, blocking their path. With quick thinking, {words[2]} used their {words[9]} to overcome the obstacle. "
        f"In the end, they discovered that the {words[5]} held the power to bring {words[10]} to the world. "
        f"And so, {words[2]} returned home as a hero, forever changed by their incredible journey."
    )
    return story

@app.route("/dream_analysis", methods=["GET", "POST"])
def home():
    interpretation = None
    story = None
    if request.method == "POST":
        if "dream" in request.form:
            dream = request.form["dream"]
            interpretation = analyze_dream(dream)
        elif "words" in request.form:
            words = request.form["words"].split(",")
            if len(words) >= 11:
                story = create_story(words)
            else:
                story = "Please provide at least 11 words for the story."
    return render_template("index.html", interpretation=interpretation, story=story)

if __name__ == "__main__":
    app.run(debug=True)
