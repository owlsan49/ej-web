# -*- coding: utf-8 -*-
# Copyright (c) 2022, Shang Luo
# All rights reserved.
# 
# Author: 罗尚
# Building Time: 2024/3/3
# Reference: None
# Description: None
import json
import math
import matplotlib.pyplot as plt

from datetime import datetime, timedelta, date

data_path = './recorder.json'
data_bk_path = './recorder-bk.json'
plot_path = 'plot.png'


def read_json(data_path):
    try:
        with open(data_path, 'r', encoding='utf-8') as jf:
            data = json.load(jf)
    except Exception as e:
        print(e)
        print(f'{data_path} is Null')
        data = {}
    return data


def write_json(file_name, json_dict, mode='w'):
    with open(file_name, mode, encoding='utf-8') as jf:
        json.dump(json_dict, jf)


def jot_plus(recorder):
    write_json(data_bk_path, recorder)

    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d')

    recorder['jod'].append(formatted_datetime)
    if len(recorder['jod']) > 1:
        date_gap = current_datetime - datetime.strptime(recorder['jod'][-2], '%Y-%m-%d')
        recorder['gap'].append(date_gap.days)
        # recorder['gap'].append(4)
    write_json(data_path, recorder)


def plot_jog(recorder):
    if len(recorder['gap']) > 0:
        plt.plot(recorder['gap'], color='blue')
        former_ph = sum(recorder['pharse'][:recorder['ptr']])
        b = len(recorder['gap'][former_ph:])
        a = sum([1 for ga in recorder['gap'][former_ph:] if ga >= (recorder['ptr'] + recorder['cold_days'])])
        min_x = cal_min_x(a, b, recorder['threshold'])
        if (b + min_x) > recorder['pharse'][recorder['ptr']]:
            recorder['pharse'][recorder['ptr']] = b + min_x
        elif b + min_x == recorder['pharse'][recorder['ptr']]:
            recorder['ptr'] += 1
    # print(recorder['pharse'])
    points = []
    for i, bb in enumerate(recorder['pharse'][:(recorder['ptr'] + 1)]):
        points += [i + recorder['cold_days']] * bb
    plt.plot(points, linestyle='--', color='lightblue')
    plt.savefig(plot_path, dpi=300)
    write_json(data_path, recorder)


def cal_min_x(a, b, beta):
    tmp = math.ceil((beta * b - a) / (1 - beta))
    return tmp if tmp > 0 else 0


def recommend_day(recorder):
    gap_days = recorder["ptr"] + recorder["cold_days"]
    future_date = (datetime.strptime(recorder["jod"][-1], '%Y-%m-%d') + timedelta(days=gap_days)).date()
    current_date = date.today()
    if current_date > future_date:
        gap_days = 0
    else:
        gap_days = (future_date - current_date).days
    return f'we recommend that you do it after {gap_days} days at least, on {future_date}!!! Yooo!'


ej_recorder = read_json(data_path)

if __name__ == '__main__':
    ...
