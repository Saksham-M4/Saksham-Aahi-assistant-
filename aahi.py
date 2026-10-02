import streamlit as st
import re
import os

# =========================================================
# 1. MAC NATIVE VOICE ENGINE
# =========================================================
def speak_text(text):
    try:
        clean_text = (
            text[:10000000]
            .replace("'", "")
            .replace('"', "")
            .replace("\n", " ")
        )

        # Mac Voice
        os.system(f"say '{clean_text}' &")

    except:
        pass

# =========================================================
# 2. PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="AAHI | Singularity Console",
    layout="wide"
)

# =========================================================
# 3. FUTURISTIC UI DESIGN
# =========================================================
st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle at top, #0d1117, #02040a);
    color: #e6edf3;
    font-family: 'Segoe UI', sans-serif;
}

h1 {
    color: #00e5ff !important;
    text-shadow: 0 0 20px #00e5ff;
    text-align: center;
    font-size: 70px !important;
    font-weight: 800;
}

.stTextInput > div > div > input {
    background-color: #111827;
    color: white;
    border-radius: 12px;
    border: 1px solid #00e5ff;
    padding: 14px;
    font-size: 16px;
}

.response-card {
    background: rgba(0, 229, 255, 0.05);
    border-left: 5px solid #00e5ff;
    padding: 25px;
    border-radius: 15px;
    margin-top: 20px;
    line-height: 1.9;
    font-size: 18px;
    box-shadow: 0 0 15px rgba(0,229,255,0.2);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# 4. KNOWLEDGE VAULT
# =========================================================
VAULT = [

    # =====================================================
    # PYTHON
    # =====================================================

    {
        "triggers": r"\b(what is python|python|why python)\b",
        "title": "WHAT IS PYTHON?",
        "desc": """
Python is a powerful programming language used by millions of developers worldwide.
It is famous because its syntax is very simple and easy to understand.
Python is used in Artificial Intelligence, Web Development, Cybersecurity, and Data Science.
Unlike older languages, Python code looks very close to normal English.
Beginners can learn Python faster than most programming languages.
That is why Python is one of the best languages for students and engineers.
"""
    },

    {
        "triggers": r"\b(print|output|display)\b",
        "title": "PRINT STATEMENT",
        "desc": """
The print() function is used to display output on the screen.
It is one of the first commands every programmer learns.
For example, print("Hello") will display Hello on the screen.
The print statement helps programmers test and debug their code.
Without print(), it becomes difficult to know what the program is doing.
It is a simple but extremely important command in programming.
"""
    },

    {
        "triggers": r"\b(variable|variables|store data)\b",
        "title": "VARIABLES",
        "desc": """
Variables are used to store information inside a program.
You can think of them like containers that hold data.
For example, age = 18 stores the number 18 inside a variable named age.
Variables make programs flexible and reusable.
Different types of data like numbers and text can be stored in variables.
They are one of the most basic concepts in programming.
"""
    },

    {
        "triggers": r"\b(string|strings|text)\b",
        "title": "STRINGS",
        "desc": """
A string is any text written inside quotation marks.
For example, "Hello World" is a string in Python.
Strings are used to store names, messages, and sentences.
Python allows us to combine multiple strings together.
We can also find the length of a string or change its format.
Strings are very important because most applications use text data.
"""
    },

    {
        "triggers": r"\b(integer|integers|float|numbers)\b",
        "title": "NUMBERS IN PYTHON",
        "desc": """
Python mainly uses two number types called integers and floats.
Integers are whole numbers like 10, 50, or 100.
Floats are decimal numbers like 3.14 or 99.9.
Python can perform mathematical operations very quickly.
Numbers are used in calculations, games, banking systems, and AI.
Understanding number types is essential for every programmer.
"""
    },

    {
        "triggers": r"\b(if|condition|decision)\b",
        "title": "IF STATEMENTS",
        "desc": """
If statements help computers make decisions.
The program checks whether a condition is true or false.
If the condition is true, Python runs the code inside the if block.
For example, if age > 18 means the program checks the age value.
If statements are used in login systems, games, and AI logic.
They are one of the most important concepts in coding.
"""
    },

    {
        "triggers": r"\b(list|lists|brackets)\b",
        "title": "LISTS",
        "desc": """
Lists are used to store multiple items in one variable.
Lists are created using square brackets.
For example, fruits = ['Apple', 'Banana', 'Mango'].
Lists allow us to add, remove, or update items easily.
They are commonly used in real-world applications and databases.
Lists make handling large amounts of data very simple.
"""
    },

    {
        "triggers": r"\b(for|loop|loops|repeat)\b",
        "title": "FOR LOOPS",
        "desc": """
For loops are used to repeat a task multiple times automatically.
Instead of writing the same code again and again, loops save time.
A loop can go through every item inside a list one by one.
Loops are used in games, websites, AI systems, and automation.
They improve efficiency and reduce code length.
Loops are a very powerful feature in programming.
"""
    },

    {
        "triggers": r"\b(def|function|functions)\b",
        "title": "FUNCTIONS",
        "desc": """
Functions are reusable blocks of code.
They help programmers avoid writing the same code repeatedly.
Functions are created using the def keyword in Python.
A function performs a specific task whenever it is called.
Large applications use thousands of functions internally.
Functions make programs organized, efficient, and easier to manage.
"""
    },

    {
        "triggers": r"\b(error|bug|syntax)\b",
        "title": "BUGS & ERRORS",
        "desc": """
Errors occur when there is a mistake in the code.
Syntax errors happen when Python grammar rules are broken.
Logical errors happen when the code runs but gives wrong output.
Debugging is the process of finding and fixing errors.
Every programmer faces bugs while coding.
Fixing bugs improves coding skills and problem-solving ability.
"""
    },

    # =====================================================
    # DSA
    # =====================================================

    {
        "triggers": r"\b(dsa|algorithm|data structure)\b",
        "title": "WHAT IS DSA?",
        "desc": """
DSA stands for Data Structures and Algorithms.
A data structure is a way to organize and store data.
An algorithm is a step-by-step method to solve problems.
DSA helps programs run faster and more efficiently.
Big tech companies ask DSA questions in interviews.
It is one of the most important subjects in Computer Science.
"""
    },

    {
        "triggers": r"\b(array|arrays)\b",
        "title": "ARRAYS",
        "desc": """
Arrays store multiple values in a single structure.
Each item inside an array has its own index number.
Arrays allow quick access to stored data.
They are commonly used in searching and sorting algorithms.
Arrays are simple but extremely useful data structures.
Most programming languages support arrays.
"""
    },

    {
        "triggers": r"\b(stack|stacks|lifo)\b",
        "title": "STACK",
        "desc": """
A stack follows the Last In First Out principle.
The last item added is the first item removed.
Stacks work like a pile of plates.
They are used in browsers, undo systems, and recursion.
Push adds data and pop removes data from the stack.
Stacks are very useful in computer science.
"""
    },

    {
        "triggers": r"\b(queue|queues|fifo)\b",
        "title": "QUEUE",
        "desc": """
A queue follows the First In First Out principle.
The first item added is removed first.
Queues work like lines in a ticket counter.
They are used in scheduling and operating systems.
Enqueue adds items while dequeue removes them.
Queues help manage tasks efficiently.
"""
    },

    {
        "triggers": r"\b(big o|time complexity)\b",
        "title": "BIG O NOTATION",
        "desc": """
Big O notation measures algorithm efficiency.
It tells us how fast or slow an algorithm performs.
Efficient algorithms save time and memory.
For example, O(1) is very fast while O(n²) is slower.
Big O is important for software optimization.
Programmers use it to compare different algorithms.
"""
    },

    # =====================================================
    # AI
    # =====================================================

    {
        "triggers": r"\b(machine learning|ml)\b",
        "title": "MACHINE LEARNING",
        "desc": """
Machine Learning is a branch of Artificial Intelligence.
It allows computers to learn from data automatically.
Instead of manually writing rules, the machine finds patterns itself.
Machine Learning is used in recommendations, chatbots, and predictions.
Companies like Google and Netflix heavily use Machine Learning.
It is one of the fastest-growing technologies in the world.
"""
    },
    {
    "triggers": r"\b(why aahi|aahi better|aahi vs other ai|advantages of aahi|why choose aahi)\b",
    "title": "WHY IS AAHI BETTER?",
    "desc": """
AAHI is designed to be fast, lightweight, and reliable.
Unlike many AI assistants that depend completely on internet connectivity,
AAHI can continue working using its built-in local knowledge vault.

If your Wi-Fi or mobile data connection is lost,
AAHI will not crash because its core knowledge is stored locally.
This allows users to continue learning and accessing information
without depending on external servers.

AAHI provides instant responses, improved privacy,
low resource consumption, and a smooth user experience.
It is especially useful for students who need quick access
to programming, DSA, AI, and technical concepts.

Key Advantages:
• Works with local knowledge
• Faster response times
• Reliable performance
• Student-friendly explanations
• Better privacy
• Lightweight design
• Easy to use

AAHI is built to help users learn efficiently,
even in environments with limited or unstable internet access.
"""
},
{
    "triggers": r"\b(can aahi work|can ai work|work without internet|offline|wifi off|wifi disconnected|mobile data off|internet connection|without internet)\b",
    "title": "CAN AAHI WORK WITHOUT INTERNET?",
    "desc": """
Yes.

AAHI can continue working even when Wi-Fi or mobile data is unavailable,
provided the requested information exists in its built-in knowledge vault.

Unlike many cloud-based AI systems that depend entirely on internet access,
AAHI stores knowledge locally. This means it can continue providing answers
without crashing when the internet connection is lost.

If your Wi-Fi disconnects or your mobile data runs out,
AAHI can still respond to supported queries from its local knowledge base.

This makes AAHI reliable, fast, and useful in environments with poor or
unstable internet connectivity.
"""
},


    {
        "triggers": r"\b(supervised|labeled)\b",
        "title": "SUPERVISED LEARNING",
        "desc": """
Supervised Learning uses labeled data for training AI models.
The machine learns by studying examples with correct answers.
For example, showing cat images labeled as 'cat'.
It is commonly used in image recognition and spam detection.
The AI improves accuracy after learning from many examples.
Supervised Learning is widely used in modern AI systems.
"""
    },

    {
        "triggers": r"\b(unsupervised|clustering)\b",
        "title": "UNSUPERVISED LEARNING",
        "desc": """
Unsupervised Learning works with unlabeled data.
The AI tries to find hidden patterns automatically.
It groups similar data together using clustering techniques.
This method is used in customer analysis and recommendations.
No correct answers are provided during training.
It helps discover insights from massive datasets.
"""
    },

    {
        "triggers": r"\b(reinforcement|trial and error)\b",
        "title": "REINFORCEMENT LEARNING",
        "desc": """
Reinforcement Learning teaches AI using rewards and penalties.
The AI learns through trial and error.
Correct actions receive rewards while wrong actions receive penalties.
This method is used in robotics and self-driving cars.
AI systems gradually improve after repeated practice.
It is inspired by how humans learn from experience.
"""
    }

]

# =========================================================
# 5. TITLE
# =========================================================
st.title("AAHI | SINGULARITY")

# =========================================================
# 6. INPUT BOX
# =========================================================
query = st.text_input(
    "ACCESS KNOWLEDGE ARCHIVE:",
    placeholder="Ask anything about Python, DSA, or AI..."
)

# =========================================================
# 7. SEARCH ENGINE
# =========================================================
if query:

    found = False

    for entry in VAULT:

        if re.search(entry["triggers"], query.lower()):

            st.markdown(f"## {entry['title']}")

            st.markdown(
                f"""
                <div class="response-card">
                    {entry["desc"]}
                </div>
                """,
                unsafe_allow_html=True
            )

            # Voice Output
            speak_text(entry["desc"])

            found = True
            break

    # =====================================================
    # 8. IF NOTHING FOUND
    # =====================================================
    if not found:

        st.warning(
            "Query not found. Try Python, Arrays, Machine Learning, Stack, Queue, etc."
        )