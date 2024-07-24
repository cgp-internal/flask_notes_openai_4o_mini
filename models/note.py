from flask import jsonify
import csv
import os

class Note:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

def initialize_csv(filepath='data/notes.csv'):
    if not os.path.exists(filepath):
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'title', 'content'])
            writer.writerow([1, 'First Note', 'This is the content of the first note.'])
            writer.writerow([2, 'Second Note', 'This is the content of the second note.'])
            writer.writerow([3, 'Third Note', 'This is the content of the third note.'])

def get_all_notes(filepath='data/notes.csv'):
    notes = []
    with open(filepath, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            notes.append(Note(int(row['id']), row['title'], row['content']))
    return notes

def get_note_by_id(note_id, filepath='data/notes.csv'):
    with open(filepath, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['id']) == note_id:
                return Note(int(row['id']), row['title'], row['content'])
    return None

def add_note(title, content, filepath='data/notes.csv'):
    notes = get_all_notes(filepath)
    new_id = max(note.id for note in notes) + 1 if notes else 1
    new_note = Note(new_id, title, content)
    with open(filepath, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([new_note.id, new_note.title, new_note.content])
    return new_note

def update_note(note_id, title, content, filepath='data/notes.csv'):
    notes = get_all_notes(filepath)
    updated_notes = []
    note_found = False
    for note in notes:
        if note.id == note_id:
            note.title = title
            note.content = content
            note_found = True
        updated_notes.append(note)
    if note_found:
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'title', 'content'])
            for note in updated_notes:
                writer.writerow([note.id, note.title, note.content])
    return note_found

def delete_note(note_id, filepath='data/notes.csv'):
    notes = get_all_notes(filepath)
    updated_notes = [note for note in notes if note.id != note_id]
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'title', 'content'])
        for note in updated_notes:
            writer.writerow([note.id, note.title, note.content])
    return len(notes) != len(updated_notes)