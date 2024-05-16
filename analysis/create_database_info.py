#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sqlite3
from pathlib import Path

import pandas as pd

conn = sqlite3.connect('Oryza_Germs_Info.db')
cursor = conn.cursor()


def insert_data_1():
    TABLE_NAME = "Pantable"

    # Doping EMPLOYEE table if already exists.
    cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")

    with open('1pan/pan.table') as f:
        data = f.read()

    lines = data.split('\n')
    keys = lines[0].split('\t')

    def to_tuple(_v):
        return tuple(_v.split('\t'))

    values = [to_tuple(v) for v in lines[1:] if v.count('\t') == 141]

    def p(_v):
        return f"C_{_v}" if _v.isdigit() else _v

    sql = f"CREATE TABLE {TABLE_NAME} ({','.join([f'{p(k)} CHAR(32) ' for k in keys])})"
    cursor.execute(sql)

    sql = f"INSERT INTO {TABLE_NAME} VALUES ({','.join('?' for _ in keys)})"
    cursor.executemany(sql, values)

    conn.commit()


def insert_data_2():
    dir_path = Path(os.path.join(os.getcwd(), '0gff'))
    tables = []

    def p(v):
        _values = v.split('\t')
        geneid = _values[-1].split(';')[0].split('=')[-1]
        _values[1] = geneid
        _new_values = _values[:5]
        _new_values.append(_values[6])
        return _new_values

    for file in dir_path.iterdir():
        if file.suffix != ".gff":
            continue

        with open(file) as f:
            data = f.read()

        TABLE_NAME = f"info_{file.name.split('.')[0]}"
        tables.append(file.name.split('.')[0])
        lines = data.split('\n')

        df = pd.DataFrame(
            data=[p(l) for l in lines if 'gene' in l],
            columns=['chr', 'geneid', 'type', 'gene_start', 'gene_end', 'strand']
        )
        df['gene_start'] = df['gene_start'].fillna(0).astype(int)
        df['gene_end'] = df['gene_end'].fillna(0).astype(int)
        df['id'] = range(1, len(df) + 1)

        # 将DataFrame写入SQLite数据库的表中
        df.to_sql(TABLE_NAME, sqlite3.connect('Oryza_Germs_Info.db'), if_exists='replace', index=False)

    with open('1pan/pan.info') as f:
        data = f.read()
        lines = data.split('\n')
        df = pd.DataFrame(
            data=[l.split('\t')[:6] for l in lines],
            columns=['name', 'geneid', 'groups', 'gene_type']
        )
        df.to_sql("genetype", sqlite3.connect('Oryza_genetype.db'), if_exists='replace', index=False)


if __name__ == '__main__':
    insert_data_1()
    insert_data_2()
