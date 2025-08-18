import sys
import json
from music21 import converter, note, chord, instrument, tempo

def parse_midi(path: str):
    s = converter.parse(path)

    # tempo mặc định
    qpm = 120.0
    try:
        mmb = s.metronomeMarkBoundaries()
        if mmb and getattr(mmb[0][2], "number", None):
            qpm = float(mmb[0][2].number)
    except Exception:
        pass
    ql2s = lambda ql: float(ql) * 60.0 / qpm

    events = []
    for el in s.recurse().notesAndRests:
        event = {
            "class": el.classes,                    # kiểu phần tử (Note, Chord, Rest,…)
            "offset": float(el.offset),             # vị trí trong score (theo quarterLength)
            "measure": getattr(el, "measureNumber", None),
            "quarterLength": float(el.duration.quarterLength),
            "seconds": ql2s(el.duration.quarterLength),
        }

        if isinstance(el, note.Note):
            event.update({
                "type": "note",
                "pitch": el.pitch.nameWithOctave,
                "midi": int(el.pitch.midi),
                "velocity": getattr(el, "volume", None) and el.volume.velocity,
            })
        elif isinstance(el, chord.Chord):
            event.update({
                "type": "chord",
                "pitches": [p.nameWithOctave for p in el.pitches],
                "midi": [int(p.midi) for p in el.pitches],
            })
        else:
            event.update({"type": "rest"})

        events.append(event)

    # metadata
    metadata = {
        "parts": [str(p) for p in s.parts],
        "instruments": [str(i) for i in s.recurse().getElementsByClass(instrument.Instrument)],
        "tempos": [str(t) for t in s.recurse().getElementsByClass(tempo.MetronomeMark)],
    }

    return {"metadata": metadata, "events": events}


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python ga.py <input.mid> <output_number>")
        sys.exit(1)

    midi_file = sys.argv[1]
    out_number = sys.argv[2]  # ví dụ: 1, 2, 3...

    result = parse_midi(midi_file)

    out_filename = f"A{out_number}.json"
    with open(out_filename, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved to {out_filename}")
