import tkinter as tk
from tkinter import ttk
import pandas as pd
import joblib, json
import numpy as np
import sklearn

def score_to_letter(numb):
    thresholds = {
        "<D": [-1000, 2300],
        "D": [2300, 2900],
        "D+": [2900, 3500],
        "C": [3500, 4900],
        "C+": [4900, 6500],
        "B": [6500, 8200],
        "B+": [8200, 10000],
        "A": [10000, 12100],
        "A+": [12100, 14500],
        "S": [14500, 15900],
        "S+": [15900, 17500],
        "SS": [17500, 19200],
        "SS+": [19200, 19600],
        "Ug": [19600, 100000],
    }
    for key, value in thresholds.items():
        if value[0] <= numb < value[1]:
            return key

def load_model():
    model = joblib.load('base/best_elasticnet_20260522_1847.joblib')
    prep = joblib.load('base/preprocessor_20260522_1847.joblib')
    meta = json.load(open('base/model_meta_20260522_1847.json'))

    return model, prep, meta

def estimate_score():
    dataframe = compile_row_for_model()
    model, prep, meta = load_model()

    raw = dataframe[meta['feature_names']]
    score = model.predict(prep.transform(raw))[0]
    letter = score_to_letter(score)
    score = str(score)
    score_result.set(score)
    letter_result.set(letter)

def compile_row_for_model():
    apt_map = {
        "S": 8,
        "A": 7,
        "B": 6,
        "C": 5,
        "D": 4,
        "E": 3,
        "F": 2,
        "G": 1,
    }

    spd = int(spd_entry.get())
    sta = int(sta_entry.get())
    pwr = int(pwr_entry.get())
    guts = int(guts_entry.get())
    wit = int(wit_entry.get())
    ult_lvl = int(ult_lvl_entry.get())
    inh_ult = int(inherited_ult_entry.get())

    fans = int(fans_entry.get())
    g1w = int(g1w_spin.get())
    g1p = int(g1p_spin.get())
    g2w = int(g2w_spin.get())
    g2p = int(g2p_spin.get())
    g3w = int(g3w_spin.get())
    g3p = int(g3p_spin.get())
    opw = int(opw_spin.get())
    preopw = int(preopw_spin.get())
    exw = int(exw_spin.get())
    exp = int(exp_spin.get())

    turf_apt = apt_map[turf_spin.get()]
    dirt_apt = apt_map[dirt_spin.get()]
    sprint_apt = apt_map[sprint_spin.get()]
    mile_apt = apt_map[mile_spin.get()]
    medium_apt = apt_map[medium_spin.get()]
    long_apt = apt_map[long_spin.get()]
    front_apt = apt_map[front_spin.get()]
    pace_apt = apt_map[pacer_spin.get()]
    late_apt = apt_map[late_spin.get()]
    end_apt = apt_map[end_spin.get()]

    green_skills = float(green_skills_spin.get())
    sprint_skills = float(sprint_skills_spin.get())
    mile_skills = float(mile_skills_spin.get())
    medium_skills = float(medium_skills_spin.get())
    long_skills = float(long_skills_spin.get())
    front_skills = float(front_skills_spin.get())
    pace_skills = float(pacer_skills_spin.get())
    late_skills = float(late_skills_spin.get())
    end_skills = float(end_skills_spin.get())
    common_skills = float(common_skills_spin.get())

    temp_dict = {
        "SPD": spd,
        "STA": sta,
        "PWR": pwr,
        "GUTS": guts,
        "WIT": wit,
        "ult_lvl": ult_lvl,
        "inherited_ult": inh_ult,
        "G1_wins": g1w,
        "G1_prize": g1p,
        "G2_wins": g2w,
        "G2_prize": g2p,
        "G3_wins": g3w,
        "G3_prize": g3p,
        "OP_wins": opw,
        "PreOP_wins": preopw,
        "Ex_wins": exw,
        "Ex_prize": exp,
        "Fans": fans,
        "turf_apt": turf_apt,
        "dirt_apt": dirt_apt,
        "sprint_apt": sprint_apt,
        "mile_apt": mile_apt,
        "medium_apt": medium_apt,
        "long_apt": long_apt,
        "front_apt": front_apt,
        "pace_apt": pace_apt,
        "late_apt": late_apt,
        "end_apt": end_apt,
        "green_skills": green_skills,
        "skills_sprint": sprint_skills,
        "skills_mile": mile_skills,
        "skills_medium": medium_skills,
        "skills_long": long_skills,
        "skills_front": front_skills,
        "skills_pace": pace_skills,
        "skills_late": late_skills,
        "skills_end": end_skills,
        "skills_universal": common_skills,
    }
    df = pd.DataFrame(temp_dict, index=[0])
    return df

root = tk.Tk()
root.title("Umazing calculator")
root.geometry("1100x500")
#root.configure(bg="dark sea green")
icon = tk.PhotoImage(file='icon.png')
root.iconphoto(False, icon)
score_result = tk.StringVar(root, value='XXXXX')
letter_result = tk.StringVar(root, value='G+')

root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=2)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=2)
root.grid_columnconfigure(5, weight=1)
root.grid_columnconfigure(6, weight=2)
root.grid_columnconfigure(7, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_rowconfigure(8, weight=1)
root.grid_rowconfigure(9, weight=1)
root.grid_rowconfigure(10, weight=1)

spd_label = ttk.Label(root, text="SPD")
spd_label.grid(column=0, row=1, sticky='nsew')
sta_label = ttk.Label(root, text="STA")
sta_label.grid(column=0, row=2, sticky='nsew')
pwr_label = ttk.Label(root, text="PWR")
pwr_label.grid(column=0, row=3, sticky='nsew')
guts_label = ttk.Label(root, text="GUTS")
guts_label.grid(column=0, row=4, sticky='nsew')
wit_label = ttk.Label(root, text="WIT")
wit_label.grid(column=0, row=5, sticky='nsew')
ult_lvl_label = ttk.Label(root, text="LVL of Ult")
ult_lvl_label.grid(column=0, row=6, sticky='nsew')
inherited_ult_label = ttk.Label(root, text="Inherited Ults Count")
inherited_ult_label.grid(column=0, row=7, sticky='nsew')
fans_label = ttk.Label(root, text="№ of FANS")
fans_label.grid(column=0, row=8, sticky='nsew')
preopw_label = ttk.Label(root, text="Побед в PreOP")
preopw_label.grid(column=0, row=9, sticky='nsew')

spd_entry = ttk.Entry(root)
spd_entry.insert(0, "100")
spd_entry.grid(column=1, row=1, sticky='nsew')
sta_entry = ttk.Entry(root)
sta_entry.insert(0, "100")
sta_entry.grid(column=1, row=2, sticky='nsew')
pwr_entry = ttk.Entry(root)
pwr_entry.insert(0, "100")
pwr_entry.grid(column=1, row=3, sticky='nsew')
guts_entry = ttk.Entry(root)
guts_entry.insert(0, "100")
guts_entry.grid(column=1, row=4, sticky='nsew')
wit_entry = ttk.Entry(root)
wit_entry.insert(0, "100")
wit_entry.grid(column=1, row=5, sticky='nsew')
ult_lvl_entry = ttk.Entry(root)
ult_lvl_entry.insert(0, "1")
ult_lvl_entry.grid(column=1, row=6, sticky='nsew')
inherited_ult_entry = ttk.Entry(root)
inherited_ult_entry.insert(0, "2")
inherited_ult_entry.grid(column=1, row=7, sticky='nsew')
fans_entry = ttk.Entry(root)
fans_entry.insert(0, "10000")
fans_entry.grid(column=1, row=8, sticky='nsew')
preopw_spin = ttk.Spinbox(root, from_=0, to=60, state='readonly')
preopw_spin.grid(column=1, row=9, sticky='nsew')

g1w_label = ttk.Label(root, text="Побед в G1")
g1w_label.grid(column=2, row=1, sticky='nsew')
g2w_label = ttk.Label(root, text="Побед в G2")
g2w_label.grid(column=2, row=2, sticky='nsew')
g3w_label = ttk.Label(root, text="Побед в G3")
g3w_label.grid(column=2, row=3, sticky='nsew')
opw_label = ttk.Label(root, text="Побед в OP")
opw_label.grid(column=2, row=4, sticky='nsew')
exw_label = ttk.Label(root, text="Побед в EX")
exw_label.grid(column=2, row=5, sticky='nsew')
g1p_label = ttk.Label(root, text="Призовых (2-5) в G1")
g1p_label.grid(column=2, row=6, sticky='nsew')
g2p_label = ttk.Label(root, text="Призовых (2-5) в G2")
g2p_label.grid(column=2, row=7, sticky='nsew')
g3p_label = ttk.Label(root, text="Призовых (2-5) в G3")
g3p_label.grid(column=2, row=8, sticky='nsew')
exp_label = ttk.Label(root, text="Призовых (2-5) в EX")
exp_label.grid(column=2, row=9, sticky='nsew')

g1w_spin = ttk.Spinbox(root, from_=0, to=60, state='readonly')
g1w_spin.grid(column=3, row=1, sticky='nsew')
g2w_spin = ttk.Spinbox(root, from_=0, to=60, state='readonly')
g2w_spin.grid(column=3, row=2, sticky='nsew')
g3w_spin = ttk.Spinbox(root, from_=0, to=60, state='readonly')
g3w_spin.grid(column=3, row=3, sticky='nsew')
opw_spin = ttk.Spinbox(root, from_=0, to=60, state='readonly')
opw_spin.grid(column=3, row=4, sticky='nsew')
exw_spin = ttk.Spinbox(root, from_=0, to=3, state='readonly')
exw_spin.grid(column=3, row=5, sticky='nsew')
g1p_spin = ttk.Spinbox(root, from_=0, to=60, state='readonly')
g1p_spin.grid(column=3, row=6, sticky='nsew')
g2p_spin = ttk.Spinbox(root, from_=0, to=60, state='readonly')
g2p_spin.grid(column=3, row=7, sticky='nsew')
g3p_spin = ttk.Spinbox(root, from_=0, to=60, state='readonly')
g3p_spin.grid(column=3, row=8, sticky='nsew')
exp_spin = ttk.Spinbox(root, from_=0, to=3, state='readonly')
exp_spin.grid(column=3, row=9, sticky='nsew')

apt_frame = ttk.LabelFrame(root, text='Aptitudes')
apt_frame.grid(column=4, row=0, rowspan=1, columnspan=4)
apt_frame.grid_columnconfigure(0, weight=1)
apt_frame.grid_columnconfigure(1, weight=1)
apt_frame.grid_columnconfigure(2, weight=1)
apt_frame.grid_columnconfigure(3, weight=1)
apt_frame.grid_rowconfigure(0, weight=1)


turf_label = ttk.Label(apt_frame, text="Turf Aptitude")
turf_label.grid(column=0, row=0, sticky='nsew')
sprint_label = ttk.Label(root, text="Sprint Aptitude")
sprint_label.grid(column=4, row=1, sticky='nsew')
mile_label = ttk.Label(root, text="Mile Aptitude")
mile_label.grid(column=4, row=2, sticky='nsew')
medium_label = ttk.Label(root, text="Medium Aptitude")
medium_label.grid(column=4, row=3, sticky='nsew')
long_label = ttk.Label(root, text="Long Aptitude")
long_label.grid(column=4, row=4, sticky='nsew')

dirt_label = ttk.Label(apt_frame, text="Dirt Aptitude")
dirt_label.grid(column=2, row=0, sticky='nsew')
front_label = ttk.Label(root, text="Front Runner Aptitude")
front_label.grid(column=6, row=1, sticky='nsew')
pacer_label = ttk.Label(root, text="Pace Chaser Aptitude")
pacer_label.grid(column=6, row=2, sticky='nsew')
late_label = ttk.Label(root, text="Late Surger Aptitude")
late_label.grid(column=6, row=3, sticky='nsew')
end_label = ttk.Label(root, text="End Closer Aptitude")
end_label.grid(column=6, row=4, sticky='nsew')

aptitudes_list = ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'S']

turf_spin = ttk.Spinbox(apt_frame, values=aptitudes_list, state='readonly')
turf_spin.grid(column=1, row=0, sticky='nsew')
sprint_spin = ttk.Spinbox(root, values=aptitudes_list, state='readonly')
sprint_spin.grid(column=5, row=1, sticky='nsew')
mile_spin = ttk.Spinbox(root, values=aptitudes_list, state='readonly')
mile_spin.grid(column=5, row=2, sticky='nsew')
medium_spin = ttk.Spinbox(root, values=aptitudes_list, state='readonly')
medium_spin.grid(column=5, row=3, sticky='nsew')
long_spin = ttk.Spinbox(root, values=aptitudes_list, state='readonly')
long_spin.grid(column=5, row=4, sticky='nsew')

dirt_spin = ttk.Spinbox(apt_frame, values=aptitudes_list, state='readonly')
dirt_spin.grid(column=3, row=0, sticky='nsew')
front_spin = ttk.Spinbox(root, values=aptitudes_list, state='readonly')
front_spin.grid(column=7, row=1, sticky='nsew')
pacer_spin = ttk.Spinbox(root, values=aptitudes_list, state='readonly')
pacer_spin.grid(column=7, row=2, sticky='nsew')
late_spin = ttk.Spinbox(root, values=aptitudes_list, state='readonly')
late_spin.grid(column=7, row=3, sticky='nsew')
end_spin = ttk.Spinbox(root, values=aptitudes_list, state='readonly')
end_spin.grid(column=7, row=4, sticky='nsew')

green_skills_label = ttk.Label(root, text="Green Skills")
green_skills_label.grid(column=4, row=5, sticky='nsew')
sprint_skills_label = ttk.Label(root, text="Sprint Skills")
sprint_skills_label.grid(column=4, row=6, sticky='nsew')
mile_skills_label = ttk.Label(root, text="Mile Skills")
mile_skills_label.grid(column=4, row=7, sticky='nsew')
medium_skills_label = ttk.Label(root, text="Medium Skills")
medium_skills_label.grid(column=4, row=8, sticky='nsew')
long_skills_label = ttk.Label(root, text="Long Skills")
long_skills_label.grid(column=4, row=9, sticky='nsew')

common_skills_label = ttk.Label(root, text="Common Skills")
common_skills_label.grid(column=6, row=5, sticky='nsew')
front_skills_label = ttk.Label(root, text="Front Runner Skills")
front_skills_label.grid(column=6, row=6, sticky='nsew')
pacer_skills_label = ttk.Label(root, text="Pace Chaser Skills")
pacer_skills_label.grid(column=6, row=7, sticky='nsew')
late_skills_label = ttk.Label(root, text="Late Surger Skills")
late_skills_label.grid(column=6, row=8, sticky='nsew')
end_skills_label = ttk.Label(root, text="End Closer Skills")
end_skills_label.grid(column=6, row=9, sticky='nsew')

green_skills_spin = ttk.Spinbox(root, from_=0.0, to=20.0, increment=0.5, state='readonly')
green_skills_spin.grid(column=5, row=5, sticky='nsew')
sprint_skills_spin = ttk.Spinbox(root, from_=0.0, to=20.0, increment=0.5, state='readonly')
sprint_skills_spin.grid(column=5, row=6, sticky='nsew')
mile_skills_spin = ttk.Spinbox(root, from_=0.0, to=20.0, increment=0.5, state='readonly')
mile_skills_spin.grid(column=5, row=7, sticky='nsew')
medium_skills_spin = ttk.Spinbox(root, from_=0.0, to=20.0, increment=0.5, state='readonly')
medium_skills_spin.grid(column=5, row=8, sticky='nsew')
long_skills_spin = ttk.Spinbox(root, from_=0.0, to=20.0, increment=0.5, state='readonly')
long_skills_spin.grid(column=5, row=9, sticky='nsew')

common_skills_spin = ttk.Spinbox(root, from_=0.0, to=20.0, increment=0.5, state='readonly')
common_skills_spin.grid(column=7, row=5, sticky='nsew')
front_skills_spin = ttk.Spinbox(root, from_=0.0, to=20.0, increment=0.5, state='readonly')
front_skills_spin.grid(column=7, row=6, sticky='nsew')
pacer_skills_spin = ttk.Spinbox(root, from_=0.0, to=20.0, increment=0.5, state='readonly')
pacer_skills_spin.grid(column=7, row=7, sticky='nsew')
late_skills_spin = ttk.Spinbox(root, from_=0.0, to=20.0, increment=0.5, state='readonly')
late_skills_spin.grid(column=7, row=8, sticky='nsew')
end_skills_spin = ttk.Spinbox(root, from_=0.0, to=20.0, increment=0.5, state='readonly')
end_skills_spin.grid(column=7, row=9, sticky='nsew')

deco_frame = ttk.LabelFrame(root, text='Inference')
deco_frame.grid(column=0, row=0, columnspan=4, sticky='nsew')
deco_frame.grid_columnconfigure(0, weight=1)
deco_frame.grid_columnconfigure(1, weight=1)
deco_frame.grid_columnconfigure(2, weight=1)
deco_frame.grid_columnconfigure(3, weight=1)
deco_frame.grid_rowconfigure(0, weight=1)

est_button = ttk.Button(deco_frame, text='Рассчитать!', command=estimate_score, underline=0)
est_button.grid(column=0, row=0, sticky='nsew')

res_label = ttk.Label(deco_frame, text='Ожидаемый результат:')
res_label.grid(column=1, row=0, sticky='nsew')

score_label = ttk.Label(deco_frame, textvariable=score_result)
score_label.grid(column=2, row=0, sticky='nsew')

letter_label = ttk.Label(deco_frame, textvariable=letter_result)
letter_label.grid(column=3, row=0, sticky='nsew')

root.mainloop()