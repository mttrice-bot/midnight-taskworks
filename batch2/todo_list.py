#!/usr/bin/env python3
"""Simple CLI todo list manager."""
import json, os, sys

TODO_FILE = os.path.expanduser("~/.todo.json")

def load():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE) as f: return json.load(f)
    return []

def save(todos):
    with open(TODO_FILE, 'w') as f: json.dump(todos, f, indent=2)

def main():
    todos = load()
    if len(sys.argv) < 2:
        print("📋 Todo List")
        print("="*30)
        if not todos: print("No tasks!")
        for i, t in enumerate(todos, 1):
            status = "✅" if t.get("done") else "⬜"
            print(f"{i}. {status} {t['task']}")
    elif sys.argv[1] == "add":
        todos.append({"task": " ".join(sys.argv[2:]), "done": False})
        save(todos)
        print("✅ Added!")
    elif sys.argv[1] == "done":
        i = int(sys.argv[2]) - 1
        todos[i]["done"] = True
        save(todos)
        print("✅ Marked done!")
    elif sys.argv[1] == "clear":
        save([])
        print("🗑️ Cleared!")

if __name__ == "__main__":
    main()
